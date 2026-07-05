---
status: approved
approved_at: 2026-07-05T19:23:14Z
last_modified: 2026-07-05T19:23:14Z
source_requirements_approved_at: 2026-07-05T19:14:27Z
---

# Feature Design

## Overview

Eco P0 is designed as one focused Next.js application that owns the full personal time-capsule lifecycle: start, lightweight identity, draft capture, optional AI drafting, preview, seal, scheduling, receipt, contact update, delivery, and tokenized opening.

The design intentionally keeps the experience linear and sparse. There is no dashboard, feed, habit loop, or progress surface. After scheduling, the user receives a receipt and exits the product. The system then keeps the promise through a scheduled delivery pipeline.

<!-- assumed: A single Next.js app is sufficient for P0 because the required backend is lightweight and already bounded by the chosen stack. -->
<!-- assumed: Supabase Auth magic link is the P0 identity mechanism; no full account dashboard is introduced in P0. -->
<!-- assumed: AI drafting is included in P0 through Gemini API and remains behind a feature flag so manual writing still works if AI is disabled or unavailable. -->
<!-- assumed: Tokenized landing access is available only after the delivery date for the recipient-facing flow, while receipt/update links remain logistics-only. -->

## Product And Technical Decisions

The following decisions are locked for this design revision:

| Decision | Choice |
| --- | --- |
| AI in P0 | Included behind feature flag using Gemini API |
| AI model | `gemini-3.5-flash` |
| AI secret | `GEMINI_API_KEY`; never stored in client code or committed files |
| Login and email verification | Supabase Auth magic link |
| Token landing timing | `/e/[token]` opens only after the delivery date |
| Media limits | Strict P0 limits: photo up to 10 MB each, max 5 photos, one audio up to 50 MB or 10 minutes, one video up to 200 MB or 3 minutes, max 300 MB per Eco |
| Download after delivery | ZIP export containing text, metadata, and media |
| Email retry | Three automatic retry attempts, then `delivery_failed` |
| Timezone | Delivery date interpreted in the user's selected timezone |
| Receipt | Receipt page plus confirmation email |

External reference: Google AI documentation lists Gemini 3.5 Flash with model code `gemini-3.5-flash` at `https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash`.

## Architecture

```text
Browser
  -> Next.js App Router UI
  -> Server Actions / Route Handlers
  -> Supabase Postgres
  -> Supabase Storage (private media)
  -> Vercel Cron -> /api/jobs/deliver-echoes
  -> Resend
  -> Email with /e/[token]
  -> Tokenized Eco landing
```

### Application Areas

- Creation flow: linear, mobile-first screens for landing, intro, content capture, AI assist, preview, seal, scheduling, receipt, and final screen.
- Internal API boundary: server-side mutations for user/session, draft persistence, media registration, AI drafting, sealing, scheduling, receipt generation, contact update, delivery, token validation, and export.
- Delivery job: protected cron endpoint that selects due delivery jobs, creates delivery attempts, sends email, updates states, and records delivery events.
- Public token route: `/e/[token]` resolves a high-entropy token, verifies validity, exposes sealed content, and records open/download events.
- Storage boundary: media assets remain private; public pages never expose raw permanent object URLs.

### State Flow

```text
draft
  -> sealed
  -> scheduled
  -> preparing_delivery
  -> delivered
  -> opened

scheduled
  -> delivery_failed
  -> scheduled (temporary retry only)
```

Content fields are editable only in `draft`. Logistics fields, currently delivery email and fallback email, are editable after sealing through receipt or magic-link flows.

## Options Considered

### Option A: Single Next.js P0 App With Supabase, Resend, And Vercel Cron

- Summary: Use Next.js for UI and backend boundaries, Supabase for persistence and private media, Resend for email, and Vercel Cron for due-job execution.
- Why chosen: It matches the approved stack, minimizes custom infrastructure, keeps state transitions in one codebase, and gives a short path to a working prototype.

### Option B: Separate Worker Service For Delivery

- Summary: Keep the web app focused on creation and run scheduling/delivery in a separate worker service.
- Why rejected: It adds deployment, credentials, observability, and data-contract overhead before the P0 proves the ritual and delivery value.

### Option C: Client-Heavy App With Direct Supabase Writes

- Summary: Let the browser write most draft, media, and scheduling state directly to Supabase.
- Why rejected: It weakens invariant enforcement around seal immutability, creation limits, token generation, scheduling, and delivery events.

## Simplicity And Elegance Review

- Simplest viable shape: one linear flow and one scheduled job, backed by six core tables and private object storage.
- Coupling check: UI components call server-side application services; provider details stay behind service modules for auth, storage, email, AI, and token handling.
- Future-proofing: group Eco, WhatsApp, physical letters, pricing, native apps, and advanced recovery are intentionally absent from interfaces unless represented as simple enum-compatible fields.
- Draft challenge: a smaller design without receipt/contact update would be simpler, but it would fail the product promise for long delays because users need a logistics-only way to change email without reopening content.

## Components And Interfaces

### Eco Creation Flow

- Purpose: Present the ritual from start to final screen without dashboard mechanics.
- Inputs/Outputs: user email, draft text, title, media upload choices, AI draft action, preview edits, seal confirmation, delivery date, receipt save action.
- Dependencies: Eco Application Service, Media Service, AI Draft Service, Delivery Scheduling Service, shadcn/ui components.
- Requirements: `R1`, `R2`, `R3`, `R4`, `R5`, `R6`, `R7`, `R9`, `R11`

Screens:

1. Landing: product name, one-line promise, primary CTA.
2. Intro: ritual context and immutability preview.
3. Create: text editor, photo/audio/video upload controls.
4. AI assist: optional draft generation and manual skip.
5. Preview: title, letter, media list, creation date, edit actions.
6. Seal: explicit warning and confirmation interaction.
7. Time: preset choices and custom date validation.
8. Channel: verified email delivery.
9. Final: sealed confirmation, delivery date, receipt action.

### Lightweight Identity Service

- Purpose: Associate an Eco with a verified email while avoiding a full account product.
- Inputs/Outputs: email submission, verification result, user profile, creation-limit result.
- Dependencies: Supabase Auth magic link, Supabase Postgres.
- Requirements: `R1`, `R6`, `R7`

Responsibilities:

- Create or resolve a user record after Supabase magic-link verification.
- Store `verified_email` and `last_verified_at`.
- Enforce `max_echoes` with a P0 default of one and a hard cap of three.
- Block final scheduling until delivery email is verified.

### Eco Application Service

- Purpose: Own lifecycle transitions and content immutability.
- Inputs/Outputs: draft mutations, preview reads, seal command, state transition result.
- Dependencies: Supabase Postgres, Delivery Scheduling Service, Audit/Event Service.
- Requirements: `R2`, `R4`, `R5`, `R6`, `R7`, `R10`

Responsibilities:

- Persist title and letter edits while status is `draft`.
- Reject content changes when status is `sealed`, `scheduled`, `preparing_delivery`, `delivered`, `delivery_failed`, or `opened`.
- Validate substantial content before seal or scheduling.
- Record `sealed_at` and an audit event on seal.
- Keep state transitions explicit and server-side.

### Media Service

- Purpose: Upload, register, detach, and later expose private media safely.
- Inputs/Outputs: file metadata, upload target, asset record, failed-upload state, private read URL or proxied media response.
- Dependencies: Supabase Storage, Supabase Postgres, Token Access Service.
- Requirements: `R2`, `R4`, `R8`, `R10`, `R11`, `NFR2`, `NFR5`

Responsibilities:

- Store photo, audio, and video files in private buckets.
- Enforce strict P0 media caps: photo up to 10 MB each, max 5 photos, one audio up to 50 MB or 10 minutes, one video up to 200 MB or 3 minutes, max 300 MB per Eco, and MIME allowlists.
- Register `echo_assets` with file type, MIME type, size, storage key, and cover flag.
- Detach assets before seal only.
- Preserve draft content when upload fails.
- Resolve media only after token validation.

### AI Draft Service

- Purpose: Turn rough user material into a title and letter draft without coaching.
- Inputs/Outputs: user-provided text and available media-derived notes, generated title, generated letter, unavailable state.
- Dependencies: Gemini API, `GEMINI_API_KEY`, `GEMINI_MODEL=gemini-3.5-flash`, prompt guardrails from product package.
- Requirements: `R3`, `R9`, `NFR5`, `NFR6`

Responsibilities:

- Keep AI drafting behind an `AI_DRAFTING_ENABLED` feature flag.
- Call Gemini server-side only; never send `GEMINI_API_KEY` to the browser.
- Use a system prompt that frames AI as an editor of memory, not a coach of action.
- Produce structured output with `title` and `letterDraft`.
- Preserve facts and avoid invented details.
- Reject or post-filter output that contains checklist, KPI, coaching, therapy, diagnosis, or action-plan language.
- Let the user continue manually when the provider is unavailable.

### Delivery Scheduling Service

- Purpose: Validate timing and create scheduled jobs after seal.
- Inputs/Outputs: preset choice, custom date, verified email, `delivery_jobs` row, scheduled state.
- Dependencies: Eco Application Service, Supabase Postgres.
- Requirements: `R6`, `R7`, `R8`, `NFR1`, `NFR3`

Responsibilities:

- Calculate preset dates for 1 month, 6 months, 1 year, 3 years, and 5 years.
- Store the user's selected timezone with the delivery job.
- Interpret custom delivery dates in the user's selected timezone.
- Validate custom dates between one month and five years from creation.
- Create one active scheduled delivery job per scheduled Eco.
- Set Eco status to `scheduled` after job creation.

### Receipt And Contact Update Service

- Purpose: Give users proof of the sealed Eco and a logistics-only update path.
- Inputs/Outputs: receipt code, delivery date, delivery email, delivery-update token, updated verified delivery email.
- Dependencies: Supabase Postgres, Lightweight Identity Service.
- Requirements: `R7`, `R5`, `R9`, `R10`

Responsibilities:

- Generate a receipt after scheduling.
- Include code, creation date, delivery date, delivery email, and update link.
- Render a receipt page after scheduling.
- Send a confirmation email containing receipt details and the delivery-update link.
- Allow delivery email updates through a receipt or magic-link flow.
- Preserve previous delivery email when verification fails.
- Never expose title, letter, media editor, or AI assist in the contact-update flow.

### Delivery Job Runner

- Purpose: Keep the promise that due Echi are sent by email.
- Inputs/Outputs: due jobs, delivery attempt records, Resend response, state updates, retry schedule.
- Dependencies: Vercel Cron, Supabase Postgres, Resend Email Service, Token Access Service.
- Requirements: `R8`, `R10`, `NFR1`

Responsibilities:

- Authenticate cron calls before running.
- Select jobs with status `scheduled` and due delivery dates.
- Move selected Echi to `preparing_delivery`.
- Generate or resolve active access token.
- Send email with reflective copy and `/e/[token]` link.
- Mark successful sends as `delivered`.
- Retry temporary failures automatically up to three attempts.
- Mark permanent failures as `delivery_failed`.
- Mark temporary failures as `delivery_failed` after the third failed automatic attempt.
- Record delivery events for each attempt.

### Token Access Service

- Purpose: Protect public Eco access without exposing sequential identifiers.
- Inputs/Outputs: raw token, token record, validation result, Eco landing payload.
- Dependencies: Supabase Postgres, Media Service.
- Requirements: `R8`, `R10`, `NFR2`

Responsibilities:

- Generate high-entropy non-sequential tokens.
- Store token hash, status, delivery availability, expiry, and revocation state.
- Set `available_after` to the scheduled delivery date in the user's selected timezone.
- Deny otherwise valid tokens before `available_after`.
- Deny invalid, expired, or revoked tokens.
- Make media access active for at least 12 months after delivery.
- Record `echo_opened` when the landing page is opened.

### Export Service

- Purpose: Let recipients download the delivered Eco while media access is active.
- Inputs/Outputs: valid token, manifest, text file, media files, archive package.
- Dependencies: Token Access Service, Media Service.
- Requirements: `R8`, `R10`, `NFR3`

Responsibilities:

- Build a ZIP package containing title, letter, creation date, delivery date, receipt metadata, and attached media.
- Deny exports after media access expiry.
- Avoid exposing storage internals in the package manifest.

## Data Models

### `users`

- `id`
- `email`
- `verified_email`
- `last_verified_at`
- `plan`
- `max_echoes`
- `created_at`

### `echoes`

- `id`
- `user_id`
- `title`
- `letter_text`
- `status`
- `created_at`
- `sealed_at`
- `delivery_date`
- `minimum_delivery_date`
- `maximum_delivery_date`
- `cover_photo_asset_id`
- `ai_assisted`
- `immutable_after_seal`
- `media_access_expires_at`

### `echo_assets`

- `id`
- `echo_id`
- `type`
- `storage_key`
- `filename`
- `mime_type`
- `size_bytes`
- `uploaded_at`
- `is_cover`
- `detached_at`

### `delivery_channels`

- `id`
- `echo_id`
- `type`
- `target_email`
- `verified`
- `last_verified_at`
- `is_primary`
- `created_at`
- `updated_at`

### `delivery_jobs`

- `id`
- `echo_id`
- `delivery_channel_id`
- `status`
- `scheduled_for`
- `timezone`
- `attempt_count`
- `max_attempts`
- `next_attempt_at`
- `last_error_code`
- `created_at`
- `updated_at`

### `echo_access_tokens`

- `id`
- `echo_id`
- `token_hash`
- `status`
- `available_after`
- `expires_at`
- `revoked_at`
- `created_at`
- `last_opened_at`

### `delivery_events`

- `id`
- `echo_id`
- `delivery_job_id`
- `type`
- `provider_message_id`
- `error_code`
- `metadata`
- `created_at`

### `echo_receipts`

- `id`
- `echo_id`
- `receipt_code`
- `delivery_update_token_hash`
- `created_at`
- `expires_at`

## Key Interfaces

### Server Actions

- `startEco(email)`
- `saveDraftText(echoId, text)`
- `saveDraftTitle(echoId, title)`
- `detachAsset(echoId, assetId)`
- `generateAiDraft(echoId)`
- `sealEco(echoId, confirmation)`
- `scheduleEco(echoId, deliveryDate)`
- `updateDeliveryEmail(receiptToken, email)`

### Route Handlers

- `POST /api/media/upload-intent`
- `POST /api/media/complete`
- `GET /api/jobs/deliver-echoes`
- `GET /api/e/[token]`
- `GET /api/e/[token]/media/[assetId]`
- `POST /api/e/[token]/download`
- `GET /api/receipts/[receiptCode]`

Route handlers are used where HTTP boundaries are clearer: upload completion, cron, token landing, media access, and export. Server Actions are used for form-style mutations inside the app flow.

## Error Handling

- Email verification failure: final scheduling remains blocked and the previous verified address remains active.
- Creation limit reached: start flow stops before draft creation.
- Upload failure: the failed asset shows an error state and existing draft content is preserved.
- Media exceeds strict P0 limits: upload is rejected before storage registration and the draft remains unchanged.
- AI unavailable: manual writing remains available and the flow continues.
- AI feature disabled: the AI assist screen presents the manual path without blocking creation.
- Seal validation failure: Eco stays `draft` and content remains editable.
- Content edit after seal: server rejects the mutation regardless of UI state.
- Invalid delivery date: scheduling rejects dates outside one month to five years.
- Contact update verification failure: previous delivery email is preserved.
- Cron unauthorized: delivery job runner returns an authorization failure without selecting jobs.
- Temporary Resend failure: job records retry metadata and remains retryable.
- Temporary Resend failure after three attempts: job and Eco move to failed delivery state.
- Permanent Resend failure: job and Eco move to failed delivery state.
- Token opened before the delivery date: landing route returns a not-yet-available state without exposing content.
- Invalid, revoked, or expired token: landing route returns an access-denied state.
- Media access expired: landing can explain expiry, but media download is denied.
- Deletion request: content and assets are removed or marked according to retention policy before future delivery attempts continue.

## Security Considerations

- All content mutations are server-side and enforce status-based permissions.
- Private media uses storage keys, not public permanent URLs.
- Public access tokens are high entropy; only token hashes are stored.
- Tokenized routes never expose sequential Eco IDs.
- Receipt/update tokens are separate from delivery access tokens.
- Cron endpoint requires a server-held secret or equivalent platform protection.
- Gemini API credentials live only in server-side environment variables.
- Delivery and seal events are auditable.
- AI prompts send only the material required to draft the Eco; no post-seal AI processing is allowed.
- User-facing privacy claims stay conservative for P0; the implementation still treats personal media as sensitive.

## Failure Modes And Tradeoffs

- Failure mode: users lose access to their email before delivery.
  Mitigation: receipt and magic-link contact update flow allow logistics-only email changes.
  Tradeoff: no advanced recovery dashboard in P0.

- Failure mode: upload succeeds in storage but registration fails.
  Mitigation: upload completion records asset metadata server-side and can clean orphaned objects in a maintenance pass.
  Tradeoff: P0 accepts operational cleanup instead of introducing a separate asset worker.

- Failure mode: AI output sounds motivational or invented.
  Mitigation: constrained prompt, structured output, manual edit, and guardrail checks for banned patterns.
  Tradeoff: AI remains optional and may be disabled if quality blocks the ritual.

- Failure mode: due delivery fails through provider outage.
  Mitigation: retry temporary failures three times and record delivery events.
  Tradeoff: P0 uses one provider, so provider-wide outages are handled by retry, not failover.

- Failure mode: token leaks after delivery.
  Mitigation: high-entropy token, revocation, expiry, and no sequential IDs.
  Tradeoff: P0 does not require an additional unlock step by default to keep the future opening low-friction.

- Failure mode: long-term media storage costs grow.
  Mitigation: five-year scheduling cap, at least twelve-month post-delivery media window, and export path.
  Tradeoff: P0 avoids complex archival tiers until usage validates demand.

## Testing Strategy

- Unit tests: date-window validation, creation-limit checks, status transition guards, token generation/validation, AI output guardrail checks, delivery retry classification.
- Component tests: creation flow screens, upload states, AI unavailable state, preview edit controls, seal warning, scheduling validation, final receipt screen, accessible form errors.
- Integration tests: Supabase magic-link identity boundary, draft save, media upload completion, seal transaction, timezone-aware schedule transaction, receipt page, confirmation email, receipt contact update, token landing access, private media resolution, ZIP export package.
- Job tests: protected cron authorization, due-job selection, successful send, temporary failure retry up to three attempts, permanent failure state.
- End-to-end tests: happy path from "Crea il tuo Eco" to scheduled receipt, content edit denied after seal, due delivery email opens `/e/[token]`, invalid token denied.
- Accessibility checks: keyboard order, focus management, validation announcements, upload progress announcement, mobile viewport without horizontal scrolling.

## Verification Plan

- Requirement proof: each requirement maps to a component boundary and will receive at least one targeted unit, integration, or E2E test in tasks.
- Test evidence: automated tests will cover lifecycle transitions, server-side immutability, scheduling bounds, receipt-only contact updates, token denial cases, and delivery retry states.
- Operational evidence: delivery events, seal audit events, provider message IDs, attempt counts, and opened events provide runtime evidence for the delivery promise.
- Product evidence: UI tests will assert absence of dashboard, progress, social, and motivational reminder surfaces in the P0 flow.

## Requirement Coverage

<!-- Every ID MUST be wrapped in backticks; the validator rejects rows without them. -->
| Requirement | Covered By |
| --- | --- |
| `R1` | Lightweight Identity Service, Eco Creation Flow |
| `R2` | Eco Creation Flow, Media Service, Eco Application Service |
| `R3` | AI Draft Service, Eco Creation Flow |
| `R4` | Eco Creation Flow, Eco Application Service, Media Service |
| `R5` | Eco Application Service, Receipt And Contact Update Service |
| `R6` | Delivery Scheduling Service, Lightweight Identity Service |
| `R7` | Receipt And Contact Update Service, Eco Creation Flow |
| `R8` | Delivery Job Runner, Token Access Service, Export Service |
| `R9` | Eco Creation Flow, AI Draft Service, Product UI tests |
| `R10` | Media Service, Token Access Service, Eco Application Service, Delivery Job Runner |
| `R11` | Eco Creation Flow, component accessibility tests |
| `NFR1` | Delivery Job Runner retry model, delivery events, job tests |
| `NFR2` | Private storage, token hashing, tokenized media resolution |
| `NFR3` | Scheduling validation, media access expiry, export path |
| `NFR4` | Keyboard flow, announcements, upload progress, mobile viewport tests |
| `NFR5` | Upload state handling, AI unavailable fallback, responsive UI feedback |
| `NFR6` | Product copy guardrails, omitted retention surfaces, AI guardrails |

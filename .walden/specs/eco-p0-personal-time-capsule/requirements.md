---
status: in-review
approved_at: 
last_modified: 2026-07-05T17:42:41Z
---

# Requirements Document

## Introduction

Eco P0 is a mobile-first personal time capsule flow. A person creates one meaningful Eco, adds text or media, optionally asks AI to shape the material, seals the content so it cannot be changed, schedules a future email delivery, receives a receipt, then later opens a tokenized landing page with the original content.

<!-- assumed: The first Walden feature groups the personal P0 lifecycle end to end because creation, sealing, scheduling, delivery, receipt, and tokenized access share the same state model. -->
<!-- assumed: AI drafting is included as an optional creation aid, but the non-AI path remains fully usable. -->
<!-- assumed: P0 defaults to one Eco for a free prototype user while preserving the product cap of three Echi as a configurable upper bound. -->
<!-- assumed: Scheduling and delivery contact are logistics after content sealing; they can be updated without reopening content editing. -->

## Requirements

### R1 Eco Start And Lightweight Identity

**User Story:** As a visitor, I want to start an Eco with minimal account friction, so that I can preserve a message without feeling like I am entering a productivity app.

#### Acceptance Criteria

1. `R1.AC1` WHEN the visitor taps "Crea il tuo Eco", the system SHALL open a linear Eco creation flow.
2. `R1.AC2` WHEN the visitor submits an email address, the system SHALL associate the creation session with a lightweight user profile.
3. `R1.AC3` WHEN the visitor completes email verification, the system SHALL mark the email address as verified for delivery.
4. `R1.AC4` IF email verification fails, THEN the system SHALL block final scheduling until a verified email address is available.
5. `R1.AC5` The system SHALL enforce a per-user Eco creation limit with a configurable cap no greater than three.
6. `R1.AC6` IF the user has reached the configured Eco creation limit, THEN the system SHALL prevent creation of another draft.

### R2 Draft Content Capture

**User Story:** As a creator, I want to leave text and personal media in one Eco, so that the future delivery feels specific to this moment.

#### Acceptance Criteria

1. `R2.AC1` WHEN the creator types in the text editor, the system SHALL save the typed text to the draft Eco.
2. `R2.AC2` WHEN the creator uploads a photo file, the system SHALL attach the photo asset to the draft Eco.
3. `R2.AC3` WHEN the creator uploads an audio file, the system SHALL attach the audio asset to the draft Eco.
4. `R2.AC4` WHEN the creator uploads a video file, the system SHALL attach the video asset to the draft Eco.
5. `R2.AC5` WHEN the creator removes an uploaded asset before sealing, the system SHALL detach the selected asset from the draft Eco.
6. `R2.AC6` WHILE the draft Eco has no cover photo, WHEN the creator opens preview, the system SHALL show one non-blocking suggestion to add a photo.
7. `R2.AC7` IF the creator attempts to continue with no text, audio, or video, THEN the system SHALL show blocking validation for substantial content.
8. `R2.AC8` IF a media upload fails, THEN the system SHALL show a failed-upload state for that asset.
9. `R2.AC9` IF a media upload fails, THEN the system SHALL preserve the existing draft Eco content.

### R3 AI Drafting

**User Story:** As a creator, I want optional AI help that preserves my voice, so that my rough material can become a readable Eco without turning into coaching.

#### Acceptance Criteria

1. `R3.AC1` WHEN the creator taps "Crea una bozza", the system SHALL generate a title candidate from user-provided material.
2. `R3.AC2` WHEN the creator taps "Crea una bozza", the system SHALL generate a letter draft from user-provided material.
3. `R3.AC3` The system SHALL preserve user-provided facts in AI-generated output.
4. `R3.AC4` The system SHALL avoid coaching language, action plans, KPIs, and checklists in AI-generated output.
5. `R3.AC5` IF AI generation is unavailable, THEN the system SHALL let the creator continue with manually written content.
6. `R3.AC6` WHEN the creator edits an AI-generated draft before sealing, the system SHALL save the edited letter as draft content.

### R4 Preview And Pre-Seal Editing

**User Story:** As a creator, I want to preview and adjust the Eco before the seal, so that the sealed version feels intentional.

#### Acceptance Criteria

1. `R4.AC1` WHEN the creator opens preview, the system SHALL display a preview containing title, letter text, creation date, current status, attached media.
2. `R4.AC2` WHILE the Eco status is `draft`, WHEN the creator edits the title, the system SHALL save the updated title.
3. `R4.AC3` WHILE the Eco status is `draft`, WHEN the creator edits the letter, the system SHALL save the updated letter.
4. `R4.AC4` WHILE the Eco status is `draft`, WHEN the creator adds media from preview, the system SHALL attach the selected media to the draft Eco.
5. `R4.AC5` WHILE the Eco status is `draft`, WHEN the creator removes media from preview, the system SHALL detach the selected media from the draft Eco.

### R5 Seal Immutability

**User Story:** As a creator, I want a credible seal moment, so that the Eco feels committed to the future.

#### Acceptance Criteria

1. `R5.AC1` WHEN the creator taps "Sigilla il mio Eco", the system SHALL show an explicit immutability warning.
2. `R5.AC2` WHEN the creator confirms the seal, the system SHALL set the Eco status to `sealed`.
3. `R5.AC3` WHEN the Eco status becomes `sealed`, the system SHALL record the seal timestamp.
4. `R5.AC4` WHILE the Eco status is `sealed`, WHEN the creator attempts to edit content, the system SHALL deny the edit.
5. `R5.AC5` WHILE the Eco status is `scheduled`, WHEN the creator attempts to edit content, the system SHALL deny the edit.
6. `R5.AC6` WHILE the Eco status is `delivered`, WHEN the creator attempts to edit content, the system SHALL deny the edit.
7. `R5.AC7` IF seal validation fails, THEN the system SHALL keep the Eco status as `draft`.
8. `R5.AC8` WHEN the seal completes, the system SHALL move the creator to delivery scheduling.

### R6 Delivery Scheduling

**User Story:** As a creator, I want to choose when the Eco returns, so that the timing preserves the feeling of a message crossing time.

#### Acceptance Criteria

1. `R6.AC1` WHEN the creator selects a preset delivery option, the system SHALL calculate the matching future delivery date.
2. `R6.AC2` WHEN the creator submits a custom delivery date, the system SHALL validate the submitted delivery date.
3. `R6.AC3` IF the selected delivery date is earlier than one month after creation, THEN the system SHALL reject the selected delivery date.
4. `R6.AC4` IF the selected delivery date is later than five years after creation, THEN the system SHALL reject the selected delivery date.
5. `R6.AC5` WHEN a valid delivery date is confirmed, the system SHALL store the delivery date for the Eco.
6. `R6.AC6` WHEN a valid delivery date and verified delivery email are confirmed, the system SHALL create a scheduled delivery job.
7. `R6.AC7` WHEN the scheduled delivery job is created, the system SHALL set the Eco status to `scheduled`.

### R7 Receipt And Delivery Contact Updates

**User Story:** As a creator, I want a receipt and a way to update delivery contact details, so that the Eco can still reach me without reopening the sealed content.

#### Acceptance Criteria

1. `R7.AC1` WHEN scheduling completes, the system SHALL generate an Eco receipt.
2. `R7.AC2` WHEN the Eco receipt is generated, the system SHALL include receipt code, creation date, delivery date, delivery email, delivery-update link.
3. `R7.AC3` WHEN the creator opens the delivery-update link, the system SHALL show a delivery email form.
4. `R7.AC4` WHEN the creator submits a new verified delivery email through the receipt flow, the system SHALL update the delivery channel.
5. `R7.AC5` WHILE the Eco status is `scheduled`, WHEN the creator opens the delivery-update flow, the system SHALL keep the content editor inaccessible.
6. `R7.AC6` IF delivery email verification fails during contact update, THEN the system SHALL preserve the previous delivery email.
7. `R7.AC7` WHEN scheduling completes, the system SHALL show a final screen with creation date, delivery date, immutable-content notice.

### R8 Email Delivery And Tokenized Access

**User Story:** As a recipient, I want the Eco to arrive reliably by email and open through a secure link, so that the future moment is protected but reachable.

#### Acceptance Criteria

1. `R8.AC1` WHEN the protected daily delivery job runs, the system SHALL select scheduled Echi with due delivery dates.
2. `R8.AC2` WHEN a due Eco is selected for delivery, the system SHALL set the Eco status to `preparing_delivery`.
3. `R8.AC3` WHEN the delivery email is sent successfully, the system SHALL set the Eco status to `delivered`.
4. `R8.AC4` IF the email provider returns a temporary failure, THEN the system SHALL schedule a retry for the delivery job.
5. `R8.AC5` IF the email provider returns a permanent failure, THEN the system SHALL set the Eco status to `delivery_failed`.
6. `R8.AC6` WHEN the recipient opens an email link with a valid token after delivery, the system SHALL display the tokenized Eco landing page.
7. `R8.AC7` IF the access token is invalid, THEN the system SHALL deny access to the Eco landing page.
8. `R8.AC8` IF the access token is revoked, THEN the system SHALL deny access to the Eco landing page.
9. `R8.AC9` IF the access token is expired, THEN the system SHALL deny access to the Eco landing page.
10. `R8.AC10` WHEN the tokenized Eco landing page opens, the system SHALL record an `echo_opened` event.
11. `R8.AC11` WHILE media access is active, WHEN the recipient taps download package, the system SHALL provide an export package for the Eco.
12. `R8.AC12` IF media access is expired, THEN the system SHALL show an access-expired state.

### R9 Product Tone And Anti-Patterns

**User Story:** As a creator, I want Eco to feel like a ritual rather than a goal tracker, so that the experience stays intimate and non-judgmental.

#### Acceptance Criteria

1. `R9.AC1` The system SHALL avoid progress dashboards in the P0 user experience.
2. `R9.AC2` The system SHALL avoid motivational reminders in the P0 user experience.
3. `R9.AC3` The system SHALL avoid social feed surfaces in the P0 user experience.
4. `R9.AC4` WHILE the creator is creating an Eco, the system SHALL avoid copy that describes Eco as identity analysis.
5. `R9.AC5` WHEN the Eco is delivered, the system SHALL include future-facing reflective delivery copy.

### R10 Security And Storage Baseline

**User Story:** As a creator, I want personal media to be stored carefully, so that the Eco can return later without exposing private content publicly.

#### Acceptance Criteria

1. `R10.AC1` WHEN the system stores an uploaded media asset, the system SHALL store the asset in private storage.
2. `R10.AC2` WHEN the system creates a public Eco link, the system SHALL use a non-sequential high-entropy token.
3. `R10.AC3` WHEN the tokenized landing page requests private media, the system SHALL verify the access token before exposing the media.
4. `R10.AC4` IF the creator requests deletion of an Eco, THEN the system SHALL remove the Eco content according to the retention policy.
5. `R10.AC5` WHEN the system seals an Eco, the system SHALL record an audit event for the seal.
6. `R10.AC6` WHEN the system attempts delivery, the system SHALL record a delivery event.

### R11 Accessible Mobile-First Flow

**User Story:** As a creator using a phone or assistive technology, I want the Eco flow to remain navigable and understandable, so that the ritual is not limited to one interaction style.

#### Acceptance Criteria

1. `R11.AC1` WHEN the creator navigates the creation flow by keyboard, the system SHALL expose focus order matching the visible flow order.
2. `R11.AC2` WHEN a form validation error appears, the system SHALL announce the error to assistive technology.
3. `R11.AC3` WHILE media upload is in progress, the system SHALL expose upload progress to assistive technology.
4. `R11.AC4` WHEN the creator views the flow on a mobile viewport, the system SHALL keep primary actions visible without horizontal scrolling.

## Non-Functional Requirements

- `NFR1` Reliability: the delivery pipeline must be retryable, auditable, and testable across scheduled, delivered, failed, and opened states.
- `NFR2` Security: private media must not be exposed through public URLs or sequential identifiers.
- `NFR3` Longevity: scheduled delivery must support dates from one month to five years after creation.
- `NFR4` Accessibility: creation, validation, upload progress, sealing, scheduling, receipt, and tokenized access must be usable with keyboard and assistive technology.
- `NFR5` Performance: the creation flow must provide responsive feedback during media upload and AI drafting so users are not left in ambiguous waiting states.
- `NFR6` Product integrity: the P0 experience must preserve Eco's ritual tone and avoid productivity, coaching, social, or retention mechanics.

## Constraints And Dependencies

- `C1` The P0 implementation uses Next.js with TypeScript, shadcn/ui, Tailwind CSS, Supabase, Resend, and Vercel Cron.
- `C2` Supabase Storage must store media as private assets.
- `C3` Resend is the only delivery provider in P0.
- `C4` Email is the only delivery channel in P0.
- `C5` The public Eco route uses tokenized access, expected as `/e/[token]`.
- `C6` The source product guidance for this feature is `doc/eco_product_package/`.
- `C7` No application implementation should start before Walden requirements, design, and tasks are approved.

## Out Of Scope

- WhatsApp delivery.
- Physical letters, printed photos, QR cards, packaging, or shipping logistics.
- Pricing, subscriptions, marketplace flows, and payment handling.
- Shared or group Eco creation.
- Native mobile apps.
- Social feeds, comments, likes, badges, streaks, dashboards, or progress tracking.
- AI coaching, therapy, diagnosis, planning, KPI generation, or motivational action plans.
- Advanced recovery account flows beyond email-based receipt, magic link, or minimal support flow.
- End-to-end encryption as a public product claim for P0.

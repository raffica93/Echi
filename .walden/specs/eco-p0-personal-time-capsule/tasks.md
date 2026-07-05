---
status: approved
approved_at: 2026-07-05T19:28:09Z
last_modified: 2026-07-05T19:28:09Z
source_design_approved_at: 2026-07-05T19:23:14Z
---

# Implementation Plan

- [ ] 1. Scaffold the P0 application foundation
  - [ ] 1.1 Create the Next.js TypeScript app foundation with App Router, Tailwind, shadcn/ui, Vitest, Testing Library, Playwright, lint, typecheck, and test scripts.
    - Requirements: `R1.AC1`, `R11.AC4`, `NFR4`
    - Design: Architecture; Eco Creation Flow; Testing Strategy
    - Verification:
      - command: ["npm", "run", "typecheck"]
        covers: ["R1.AC1"]
      - command: ["npm", "run", "lint"]
        covers: ["R11.AC4"]

  - [ ] 1.2 Add server-only configuration parsing for Supabase, Resend, Vercel Cron secret, `GEMINI_API_KEY`, `GEMINI_MODEL=gemini-3.5-flash`, and `AI_DRAFTING_ENABLED`.
    - Requirements: `R3.AC5`, `R8.AC1`, `R10.AC3`, `NFR2`
    - Design: Product And Technical Decisions; AI Draft Service; Delivery Job Runner; Security Considerations
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/config.test.ts"]
        covers: ["R3.AC5", "R8.AC1", "R10.AC3"]

- [ ] 2. Implement persistence, private storage, and lifecycle invariants
  - [ ] 2.1 Add Supabase migrations for `users`, `echoes`, `echo_assets`, `delivery_channels`, `delivery_jobs`, `echo_access_tokens`, `delivery_events`, and `echo_receipts`.
    - Requirements: `R1.AC2`, `R2.AC1`, `R5.AC3`, `R6.AC5`, `R7.AC1`, `R8.AC10`, `R10.AC5`, `R10.AC6`, `NFR1`
    - Design: Data Models; Eco Application Service; Delivery Job Runner
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/db/schema.test.ts"]
        covers: ["R1.AC2", "R2.AC1", "R5.AC3", "R6.AC5", "R7.AC1", "R8.AC10", "R10.AC5", "R10.AC6"]

  - [ ] 2.2 Implement private media upload intent, upload completion, MIME allowlists, numeric P0 media caps, failed-upload states, and asset registration.
    - Requirements: `R2.AC2`, `R2.AC3`, `R2.AC4`, `R2.AC8`, `R2.AC9`, `R10.AC1`, `R11.AC3`, `NFR2`, `NFR5`
    - Design: Media Service; Error Handling; Security Considerations
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/media-upload.test.ts"]
        covers: ["R2.AC2", "R2.AC3", "R2.AC4", "R2.AC8", "R2.AC9", "R10.AC1", "R11.AC3"]

  - [ ] 2.3 Implement server-side status guards for draft-only content mutation, post-seal deletion handling, and seal/delivery audit events.
    - Requirements: `R4.AC2`, `R4.AC3`, `R4.AC4`, `R4.AC5`, `R5.AC4`, `R5.AC5`, `R5.AC6`, `R10.AC4`, `R10.AC5`, `R10.AC6`, `NFR1`, `NFR2`
    - Design: Eco Application Service; Error Handling; Security Considerations
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/echo-status-guards.test.ts"]
        covers: ["R4.AC2", "R4.AC3", "R4.AC4", "R4.AC5", "R5.AC4", "R5.AC5", "R5.AC6", "R10.AC4", "R10.AC5", "R10.AC6"]

- [ ] 3. Implement lightweight identity and creation limits
  - [ ] 3.1 Implement Supabase magic-link identity, verified-email persistence, and scheduling block when verification is missing.
    - Requirements: `R1.AC2`, `R1.AC3`, `R1.AC4`, `R6.AC6`
    - Design: Lightweight Identity Service; Delivery Scheduling Service
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/identity-magic-link.test.ts"]
        covers: ["R1.AC2", "R1.AC3", "R1.AC4", "R6.AC6"]

  - [ ] 3.2 Implement per-user Eco creation limits with P0 default one and hard configurable cap no greater than three.
    - Requirements: `R1.AC5`, `R1.AC6`, `NFR6`
    - Design: Lightweight Identity Service; Product And Technical Decisions
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/creation-limits.test.ts"]
        covers: ["R1.AC5", "R1.AC6"]

- [ ] 4. Build the creation, draft, media, and preview flow
  - [ ] 4.1 Build landing, intro, and linear creation route shell with product copy and mobile-first primary actions.
    - Requirements: `R1.AC1`, `R9.AC1`, `R9.AC2`, `R9.AC3`, `R11.AC4`, `NFR4`, `NFR6`
    - Design: Eco Creation Flow; Product And Technical Decisions; Simplicity And Elegance Review
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/components/creation-shell.test.tsx"]
        covers: ["R1.AC1", "R9.AC1", "R9.AC2", "R9.AC3", "R11.AC4"]

  - [ ] 4.2 Implement draft text editing and server-side draft persistence.
    - Requirements: `R2.AC1`, `R4.AC3`, `NFR5`
    - Design: Eco Creation Flow; Eco Application Service
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/draft-text.test.ts"]
        covers: ["R2.AC1", "R4.AC3"]

  - [ ] 4.3 Implement media controls for photo, audio, video, removal before seal, and one non-blocking cover-photo suggestion.
    - Requirements: `R2.AC2`, `R2.AC3`, `R2.AC4`, `R2.AC5`, `R2.AC6`, `R2.AC7`, `R4.AC4`, `R4.AC5`, `NFR5`
    - Design: Eco Creation Flow; Media Service; Error Handling
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/components/media-controls.test.tsx"]
        covers: ["R2.AC2", "R2.AC3", "R2.AC4", "R2.AC5", "R2.AC6", "R2.AC7", "R4.AC4", "R4.AC5"]

  - [ ] 4.4 Implement preview screen with title, letter text, creation date, current status, attached media, and pre-seal edit actions.
    - Requirements: `R4.AC1`, `R4.AC2`, `R4.AC3`, `R4.AC4`, `R4.AC5`
    - Design: Eco Creation Flow; Eco Application Service
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/components/preview.test.tsx"]
        covers: ["R4.AC1", "R4.AC2", "R4.AC3", "R4.AC4", "R4.AC5"]

- [ ] 5. Implement Gemini AI drafting with guardrails and fallback
  - [ ] 5.1 Implement server-side Gemini AI draft client using `GEMINI_API_KEY`, `gemini-3.5-flash`, and `AI_DRAFTING_ENABLED`.
    - Requirements: `R3.AC1`, `R3.AC2`, `R3.AC5`, `NFR5`
    - Design: Product And Technical Decisions; AI Draft Service; Key Interfaces
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/gemini-ai-draft-client.test.ts"]
        covers: ["R3.AC1", "R3.AC2", "R3.AC5"]

  - [ ] 5.2 Implement AI prompt guardrails, output validation, banned coaching-pattern checks, manual fallback, and editable AI draft saving.
    - Requirements: `R3.AC3`, `R3.AC4`, `R3.AC5`, `R3.AC6`, `R9.AC4`, `NFR6`
    - Design: AI Draft Service; Error Handling; Product Tone And Anti-Patterns
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/ai-guardrails.test.ts"]
        covers: ["R3.AC3", "R3.AC4", "R3.AC5", "R3.AC6", "R9.AC4"]

- [ ] 6. Implement seal, timezone-aware scheduling, and delivery job creation
  - [ ] 6.1 Implement seal warning, confirmation, seal transaction, `sealed_at`, immutable status, validation failure handling, and transition to scheduling.
    - Requirements: `R5.AC1`, `R5.AC2`, `R5.AC3`, `R5.AC4`, `R5.AC5`, `R5.AC6`, `R5.AC7`, `R5.AC8`, `R10.AC5`, `NFR1`
    - Design: Eco Application Service; State Flow; Error Handling
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/seal-immutability.test.ts"]
        covers: ["R5.AC1", "R5.AC2", "R5.AC3", "R5.AC4", "R5.AC5", "R5.AC6", "R5.AC7", "R5.AC8", "R10.AC5"]

  - [ ] 6.2 Implement preset dates, custom date validation, one-month minimum, five-year maximum, and user-timezone interpretation.
    - Requirements: `R6.AC1`, `R6.AC2`, `R6.AC3`, `R6.AC4`, `R6.AC5`, `NFR3`
    - Design: Delivery Scheduling Service; Product And Technical Decisions
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/delivery-date-validation.test.ts"]
        covers: ["R6.AC1", "R6.AC2", "R6.AC3", "R6.AC4", "R6.AC5"]

  - [ ] 6.3 Implement scheduled delivery job creation after valid date and verified delivery email.
    - Requirements: `R6.AC6`, `R6.AC7`, `R8.AC1`, `NFR1`
    - Design: Delivery Scheduling Service; Delivery Job Runner
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/schedule-delivery-job.test.ts"]
        covers: ["R6.AC6", "R6.AC7", "R8.AC1"]

- [ ] 7. Implement receipt and delivery contact update flows
  - [ ] 7.1 Implement receipt generation, receipt page, confirmation email, receipt metadata, final screen, and save receipt action.
    - Requirements: `R7.AC1`, `R7.AC2`, `R7.AC7`, `R9.AC2`, `NFR6`
    - Design: Receipt And Contact Update Service; Eco Creation Flow; Product And Technical Decisions
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/receipt-confirmation.test.ts"]
        covers: ["R7.AC1", "R7.AC2", "R7.AC7", "R9.AC2"]

  - [ ] 7.2 Implement receipt/magic-link delivery email update flow that preserves previous email on failed verification and never exposes content editing.
    - Requirements: `R7.AC3`, `R7.AC4`, `R7.AC5`, `R7.AC6`, `R5.AC5`
    - Design: Receipt And Contact Update Service; Lightweight Identity Service; Error Handling
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/delivery-contact-update.test.ts"]
        covers: ["R7.AC3", "R7.AC4", "R7.AC5", "R7.AC6", "R5.AC5"]

- [ ] 8. Implement delivery, tokenized landing, private media access, and ZIP export
  - [ ] 8.1 Implement protected Vercel Cron delivery runner with due-job selection, `preparing_delivery`, success state, temporary retry up to three attempts, permanent failure handling, and delivery events.
    - Requirements: `R8.AC1`, `R8.AC2`, `R8.AC3`, `R8.AC4`, `R8.AC5`, `R10.AC6`, `NFR1`
    - Design: Delivery Job Runner; Error Handling; Failure Modes And Tradeoffs
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/delivery-runner.test.ts"]
        covers: ["R8.AC1", "R8.AC2", "R8.AC3", "R8.AC4", "R8.AC5", "R10.AC6"]

  - [ ] 8.2 Implement Resend delivery email with reflective copy and tokenized `/e/[token]` link.
    - Requirements: `R8.AC3`, `R8.AC6`, `R9.AC5`, `NFR6`
    - Design: Delivery Job Runner; Product Tone And Anti-Patterns
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/delivery-email.test.ts"]
        covers: ["R8.AC3", "R8.AC6", "R9.AC5"]

  - [ ] 8.3 Implement high-entropy token generation, hashed token storage, pre-delivery denial, invalid/revoked/expired denial, and open-event recording.
    - Requirements: `R8.AC6`, `R8.AC7`, `R8.AC8`, `R8.AC9`, `R8.AC10`, `R10.AC2`, `R10.AC3`, `NFR2`
    - Design: Token Access Service; Security Considerations; Product And Technical Decisions
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/unit/token-access.test.ts"]
        covers: ["R8.AC6", "R8.AC7", "R8.AC8", "R8.AC9", "R8.AC10", "R10.AC2", "R10.AC3"]

  - [ ] 8.4 Implement tokenized landing page and private media resolver for active media access.
    - Requirements: `R8.AC6`, `R8.AC10`, `R10.AC3`, `NFR2`
    - Design: Token Access Service; Media Service; Security Considerations
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/token-landing-media.test.ts"]
        covers: ["R8.AC6", "R8.AC10", "R10.AC3"]

  - [ ] 8.5 Implement ZIP export package with text, receipt metadata, and media while media access is active, plus expired-access denial.
    - Requirements: `R8.AC11`, `R8.AC12`, `NFR3`
    - Design: Export Service; Token Access Service; Error Handling
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/integration/eco-export.test.ts"]
        covers: ["R8.AC11", "R8.AC12"]

- [ ] 9. Add product integrity, accessibility, and responsive verification
  - [ ] 9.1 Add product-copy and surface tests that prevent dashboards, motivational reminders, social feed surfaces, identity-analysis copy during creation, and coaching language.
    - Requirements: `R9.AC1`, `R9.AC2`, `R9.AC3`, `R9.AC4`, `R9.AC5`, `NFR6`
    - Design: Product Tone And Anti-Patterns; Eco Creation Flow; AI Draft Service
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/product/product-integrity.test.ts"]
        covers: ["R9.AC1", "R9.AC2", "R9.AC3", "R9.AC4", "R9.AC5"]

  - [ ] 9.2 Add accessibility tests for keyboard order, validation announcements, upload progress announcements, and mobile viewport layout.
    - Requirements: `R11.AC1`, `R11.AC2`, `R11.AC3`, `R11.AC4`, `NFR4`
    - Design: Eco Creation Flow; Testing Strategy
    - Verification:
      - command: ["npm", "run", "test", "--", "tests/accessibility/creation-accessibility.test.tsx"]
        covers: ["R11.AC1", "R11.AC2", "R11.AC3", "R11.AC4"]

- [ ] 10. Prove the complete P0 story end to end
  - [ ] 10.1 Add Playwright happy-path coverage from landing to verified email, draft content, AI draft, preview, seal, timezone scheduling, receipt page, confirmation email, delivery job, token opening, private media display, and ZIP download.
    - Requirements: `R1.AC1`, `R1.AC3`, `R2.AC1`, `R2.AC2`, `R3.AC1`, `R3.AC2`, `R4.AC1`, `R5.AC2`, `R6.AC7`, `R7.AC1`, `R7.AC7`, `R8.AC3`, `R8.AC6`, `R8.AC11`
    - Design: Verification Plan; Testing Strategy; Architecture
    - Verification:
      - command: ["npm", "run", "test:e2e", "--", "tests/e2e/eco-happy-path.spec.ts"]
        covers: ["R1.AC1", "R1.AC3", "R2.AC1", "R2.AC2", "R3.AC1", "R3.AC2", "R4.AC1", "R5.AC2", "R6.AC7", "R7.AC1", "R7.AC7", "R8.AC3", "R8.AC6", "R8.AC11"]

  - [ ] 10.2 Add Playwright negative-path coverage for no substantial content, failed upload, content edit denied after seal, invalid dates, failed contact verification, pre-delivery token denial, invalid token denial, and media expiry.
    - Requirements: `R2.AC7`, `R2.AC8`, `R5.AC4`, `R5.AC5`, `R6.AC3`, `R6.AC4`, `R7.AC6`, `R8.AC7`, `R8.AC12`
    - Design: Verification Plan; Error Handling; Security Considerations
    - Verification:
      - command: ["npm", "run", "test:e2e", "--", "tests/e2e/eco-negative-paths.spec.ts"]
        covers: ["R2.AC7", "R2.AC8", "R5.AC4", "R5.AC5", "R6.AC3", "R6.AC4", "R7.AC6", "R8.AC7", "R8.AC12"]

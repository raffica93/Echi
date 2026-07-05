import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";

const migrationPath = join(
  process.cwd(),
  "supabase",
  "migrations",
  "20260705214500_create_eco_p0_schema.sql",
);
const migration = readFileSync(migrationPath, "utf8").toLowerCase();

const requiredTables = [
  "users",
  "echoes",
  "echo_assets",
  "delivery_channels",
  "delivery_jobs",
  "echo_access_tokens",
  "delivery_events",
  "echo_receipts",
];

describe("Eco P0 database schema migration", () => {
  it("creates every approved P0 table", () => {
    for (const table of requiredTables) {
      expect(migration).toContain(`create table public.${table}`);
    }
  });

  it("defines the lifecycle states used by Eco and delivery jobs", () => {
    expect(migration).toContain("create type public.echo_status as enum");
    for (const status of [
      "draft",
      "sealed",
      "scheduled",
      "preparing_delivery",
      "delivered",
      "delivery_failed",
      "opened",
    ]) {
      expect(migration).toContain(`'${status}'`);
    }

    expect(migration).toContain("create type public.delivery_job_status");
    expect(migration).toContain("delivery_jobs_max_attempts_cap");
    expect(migration).toContain("max_attempts between 1 and 3");
  });

  it("stores content, receipts, tokens, and auditable delivery events", () => {
    for (const column of [
      "letter_text",
      "sealed_at",
      "delivery_date",
      "receipt_code",
      "delivery_update_token_hash",
      "token_hash text not null unique",
      "provider_message_id",
      "metadata jsonb not null",
    ]) {
      expect(migration).toContain(column);
    }

    expect(migration).toContain("'seal_recorded'");
    expect(migration).toContain("'delivery_attempted'");
    expect(migration).toContain("'echo_opened'");
  });

  it("keeps core product invariants close to the data", () => {
    for (const constraint of [
      "users_max_echoes_cap",
      "echoes_sealed_have_timestamp",
      "echoes_delivery_date_in_window",
      "echoes_immutable_after_seal",
      "echo_access_tokens_expiry_after_availability",
    ]) {
      expect(migration).toContain(constraint);
    }
  });

  it("adds indexes and RLS baselines for server-side access patterns", () => {
    for (const statement of [
      "create index echoes_user_status_idx",
      "create index delivery_jobs_due_idx",
      "create index delivery_events_echo_created_idx",
      "create index echo_access_tokens_hash_status_idx",
    ]) {
      expect(migration).toContain(statement);
    }

    for (const table of requiredTables) {
      expect(migration).toContain(
        `alter table public.${table} enable row level security`,
      );
    }
  });
});

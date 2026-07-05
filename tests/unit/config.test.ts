import { describe, expect, it } from "vitest";
import {
  ConfigError,
  DEFAULT_GEMINI_MODEL,
  parseServerConfig,
} from "@/lib/config/parse";

const baseEnv = {
  NEXT_PUBLIC_SUPABASE_URL: "https://project.supabase.co",
  NEXT_PUBLIC_SUPABASE_ANON_KEY: "anon-key",
  SUPABASE_SERVICE_ROLE_KEY: "service-role-key",
  SUPABASE_STORAGE_BUCKET: "echo-media",
  RESEND_API_KEY: "resend-key",
  RESEND_FROM_EMAIL: "Eco <noreply@example.com>",
  CRON_SECRET: "cron-secret",
};

describe("parseServerConfig", () => {
  it("parses required provider config without exposing client-side secrets", () => {
    const config = parseServerConfig(baseEnv);

    expect(config).toEqual({
      supabase: {
        url: "https://project.supabase.co",
        anonKey: "anon-key",
        serviceRoleKey: "service-role-key",
        storageBucket: "echo-media",
      },
      resend: {
        apiKey: "resend-key",
        fromEmail: "Eco <noreply@example.com>",
      },
      cron: {
        secret: "cron-secret",
      },
      ai: {
        draftingEnabled: false,
        geminiApiKey: undefined,
        geminiModel: DEFAULT_GEMINI_MODEL,
      },
    });
  });

  it("defaults Gemini to the approved P0 model", () => {
    const config = parseServerConfig({
      ...baseEnv,
      AI_DRAFTING_ENABLED: "false",
    });

    expect(config.ai.geminiModel).toBe("gemini-3.5-flash");
  });

  it("requires Gemini credentials only when AI drafting is enabled", () => {
    expect(() =>
      parseServerConfig({
        ...baseEnv,
        AI_DRAFTING_ENABLED: "true",
      }),
    ).toThrow("GEMINI_API_KEY is required");

    expect(
      parseServerConfig({
        ...baseEnv,
        AI_DRAFTING_ENABLED: "true",
        GEMINI_API_KEY: "gemini-key",
      }).ai,
    ).toMatchObject({
      draftingEnabled: true,
      geminiApiKey: "gemini-key",
      geminiModel: "gemini-3.5-flash",
    });
  });

  it("reports missing required variables by name only", () => {
    expect(() => parseServerConfig({})).toThrow(ConfigError);
    expect(() => parseServerConfig({})).toThrow(
      "NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_STORAGE_BUCKET, RESEND_API_KEY, RESEND_FROM_EMAIL, CRON_SECRET",
    );
  });

  it("rejects invalid URLs and boolean flags", () => {
    expect(() =>
      parseServerConfig({
        ...baseEnv,
        NEXT_PUBLIC_SUPABASE_URL: "not a url",
      }),
    ).toThrow("NEXT_PUBLIC_SUPABASE_URL must be a valid URL");

    expect(() =>
      parseServerConfig({
        ...baseEnv,
        AI_DRAFTING_ENABLED: "maybe",
      }),
    ).toThrow("AI_DRAFTING_ENABLED must be one of");
  });
});

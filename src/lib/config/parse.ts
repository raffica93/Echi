export const DEFAULT_GEMINI_MODEL = "gemini-3.5-flash";

type Env = Record<string, string | undefined>;

export type ServerConfig = {
  supabase: {
    url: string;
    anonKey: string;
    serviceRoleKey: string;
    storageBucket: string;
  };
  resend: {
    apiKey: string;
    fromEmail: string;
  };
  cron: {
    secret: string;
  };
  ai: {
    draftingEnabled: boolean;
    geminiApiKey?: string;
    geminiModel: string;
  };
};

export class ConfigError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "ConfigError";
  }
}

const REQUIRED_ENV = [
  "NEXT_PUBLIC_SUPABASE_URL",
  "NEXT_PUBLIC_SUPABASE_ANON_KEY",
  "SUPABASE_SERVICE_ROLE_KEY",
  "SUPABASE_STORAGE_BUCKET",
  "RESEND_API_KEY",
  "RESEND_FROM_EMAIL",
  "CRON_SECRET",
] as const;

const TRUE_VALUES = new Set(["1", "true", "yes", "on"]);
const FALSE_VALUES = new Set(["0", "false", "no", "off", ""]);

export function parseServerConfig(env: Env): ServerConfig {
  const missing = REQUIRED_ENV.filter((name) => !nonEmpty(env[name]));

  if (missing.length > 0) {
    throw new ConfigError(
      `Missing required server environment variables: ${missing.join(", ")}`,
    );
  }

  const supabaseUrl = readRequired(env, "NEXT_PUBLIC_SUPABASE_URL");
  assertValidUrl(supabaseUrl, "NEXT_PUBLIC_SUPABASE_URL");

  const draftingEnabled = parseBooleanEnv(
    env.AI_DRAFTING_ENABLED,
    "AI_DRAFTING_ENABLED",
  );
  const geminiApiKey = clean(env.GEMINI_API_KEY);

  if (draftingEnabled && !geminiApiKey) {
    throw new ConfigError(
      "GEMINI_API_KEY is required when AI_DRAFTING_ENABLED is true",
    );
  }

  return {
    supabase: {
      url: supabaseUrl,
      anonKey: readRequired(env, "NEXT_PUBLIC_SUPABASE_ANON_KEY"),
      serviceRoleKey: readRequired(env, "SUPABASE_SERVICE_ROLE_KEY"),
      storageBucket: readRequired(env, "SUPABASE_STORAGE_BUCKET"),
    },
    resend: {
      apiKey: readRequired(env, "RESEND_API_KEY"),
      fromEmail: readRequired(env, "RESEND_FROM_EMAIL"),
    },
    cron: {
      secret: readRequired(env, "CRON_SECRET"),
    },
    ai: {
      draftingEnabled,
      geminiApiKey,
      geminiModel: clean(env.GEMINI_MODEL) ?? DEFAULT_GEMINI_MODEL,
    },
  };
}

function parseBooleanEnv(value: string | undefined, name: string): boolean {
  const normalized = (value ?? "false").trim().toLowerCase();

  if (TRUE_VALUES.has(normalized)) {
    return true;
  }

  if (FALSE_VALUES.has(normalized)) {
    return false;
  }

  throw new ConfigError(
    `${name} must be one of: true, false, 1, 0, yes, no, on, off`,
  );
}

function assertValidUrl(value: string, name: string) {
  try {
    new URL(value);
  } catch {
    throw new ConfigError(`${name} must be a valid URL`);
  }
}

function readRequired(env: Env, name: (typeof REQUIRED_ENV)[number]): string {
  const value = clean(env[name]);

  if (!value) {
    throw new ConfigError(`${name} is required`);
  }

  return value;
}

function clean(value: string | undefined): string | undefined {
  const cleaned = value?.trim();
  return cleaned ? cleaned : undefined;
}

function nonEmpty(value: string | undefined) {
  return Boolean(clean(value));
}

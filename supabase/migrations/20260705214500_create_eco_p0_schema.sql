create extension if not exists pgcrypto;

create type public.echo_status as enum (
  'draft',
  'sealed',
  'scheduled',
  'preparing_delivery',
  'delivered',
  'delivery_failed',
  'opened'
);

create type public.echo_asset_type as enum (
  'photo',
  'audio',
  'video'
);

create type public.delivery_channel_type as enum (
  'email'
);

create type public.delivery_job_status as enum (
  'scheduled',
  'preparing_delivery',
  'delivered',
  'delivery_failed'
);

create type public.echo_access_token_status as enum (
  'active',
  'revoked',
  'expired'
);

create type public.delivery_event_type as enum (
  'seal_recorded',
  'delivery_attempted',
  'delivery_sent',
  'delivery_retry_scheduled',
  'delivery_failed',
  'echo_opened'
);

create table public.users (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  verified_email text,
  last_verified_at timestamptz,
  plan text not null default 'p0',
  max_echoes integer not null default 1,
  created_at timestamptz not null default now(),
  constraint users_max_echoes_cap check (max_echoes between 1 and 3)
);

create table public.echoes (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.users(id) on delete cascade,
  title text,
  letter_text text,
  status public.echo_status not null default 'draft',
  created_at timestamptz not null default now(),
  sealed_at timestamptz,
  delivery_date timestamptz,
  minimum_delivery_date timestamptz,
  maximum_delivery_date timestamptz,
  cover_photo_asset_id uuid,
  ai_assisted boolean not null default false,
  immutable_after_seal boolean not null default false,
  media_access_expires_at timestamptz,
  constraint echoes_sealed_have_timestamp check (
    status = 'draft' or sealed_at is not null
  ),
  constraint echoes_delivery_date_in_window check (
    delivery_date is null
    or (
      minimum_delivery_date is not null
      and maximum_delivery_date is not null
      and delivery_date between minimum_delivery_date and maximum_delivery_date
    )
  ),
  constraint echoes_immutable_after_seal check (
    status = 'draft' or immutable_after_seal = true
  )
);

create table public.echo_assets (
  id uuid primary key default gen_random_uuid(),
  echo_id uuid not null references public.echoes(id) on delete cascade,
  type public.echo_asset_type not null,
  storage_key text not null unique,
  filename text not null,
  mime_type text not null,
  size_bytes bigint not null,
  uploaded_at timestamptz not null default now(),
  is_cover boolean not null default false,
  detached_at timestamptz,
  constraint echo_assets_positive_size check (size_bytes > 0)
);

alter table public.echoes
  add constraint echoes_cover_photo_asset_id_fkey
  foreign key (cover_photo_asset_id)
  references public.echo_assets(id)
  on delete set null;

create table public.delivery_channels (
  id uuid primary key default gen_random_uuid(),
  echo_id uuid not null references public.echoes(id) on delete cascade,
  type public.delivery_channel_type not null default 'email',
  target_email text not null,
  verified boolean not null default false,
  last_verified_at timestamptz,
  is_primary boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.delivery_jobs (
  id uuid primary key default gen_random_uuid(),
  echo_id uuid not null references public.echoes(id) on delete cascade,
  delivery_channel_id uuid not null references public.delivery_channels(id) on delete restrict,
  status public.delivery_job_status not null default 'scheduled',
  scheduled_for timestamptz not null,
  timezone text not null,
  attempt_count integer not null default 0,
  max_attempts integer not null default 3,
  next_attempt_at timestamptz,
  last_error_code text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint delivery_jobs_attempt_count_nonnegative check (attempt_count >= 0),
  constraint delivery_jobs_max_attempts_cap check (max_attempts between 1 and 3),
  constraint delivery_jobs_next_attempt_after_create check (
    next_attempt_at is null or next_attempt_at >= created_at
  )
);

create table public.echo_access_tokens (
  id uuid primary key default gen_random_uuid(),
  echo_id uuid not null references public.echoes(id) on delete cascade,
  token_hash text not null unique,
  status public.echo_access_token_status not null default 'active',
  available_after timestamptz not null,
  expires_at timestamptz not null,
  revoked_at timestamptz,
  created_at timestamptz not null default now(),
  last_opened_at timestamptz,
  constraint echo_access_tokens_revoked_at check (
    status <> 'revoked' or revoked_at is not null
  ),
  constraint echo_access_tokens_expiry_after_availability check (
    expires_at > available_after
  )
);

create table public.delivery_events (
  id uuid primary key default gen_random_uuid(),
  echo_id uuid not null references public.echoes(id) on delete cascade,
  delivery_job_id uuid references public.delivery_jobs(id) on delete set null,
  type public.delivery_event_type not null,
  provider_message_id text,
  error_code text,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table public.echo_receipts (
  id uuid primary key default gen_random_uuid(),
  echo_id uuid not null references public.echoes(id) on delete cascade,
  receipt_code text not null unique,
  delivery_update_token_hash text not null unique,
  created_at timestamptz not null default now(),
  expires_at timestamptz
);

create unique index echo_assets_one_cover_per_echo
  on public.echo_assets(echo_id)
  where is_cover = true and detached_at is null;

create unique index delivery_channels_one_primary_per_echo
  on public.delivery_channels(echo_id)
  where is_primary = true;

create index echoes_user_status_idx
  on public.echoes(user_id, status);

create index delivery_jobs_due_idx
  on public.delivery_jobs(status, next_attempt_at, scheduled_for);

create index delivery_events_echo_created_idx
  on public.delivery_events(echo_id, created_at desc);

create index echo_access_tokens_hash_status_idx
  on public.echo_access_tokens(token_hash, status);

alter table public.users enable row level security;
alter table public.echoes enable row level security;
alter table public.echo_assets enable row level security;
alter table public.delivery_channels enable row level security;
alter table public.delivery_jobs enable row level security;
alter table public.echo_access_tokens enable row level security;
alter table public.delivery_events enable row level security;
alter table public.echo_receipts enable row level security;

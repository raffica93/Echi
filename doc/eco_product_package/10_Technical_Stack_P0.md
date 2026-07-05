# Eco — Stack Tecnologico P0

## Decisione

Il Prodotto 0 usa:

- **Next.js** con TypeScript per frontend, backend leggero e route tokenizzate.
- **shadcn/ui** + Tailwind CSS per componenti UI controllabili e coerenti.
- **Supabase** per Postgres, Auth leggera e Storage media.
- **Resend** per invio email transazionali.
- **Vercel** per deploy e cron giornaliero.

---

## Obiettivo dello stack

Costruire un prototipo funzionante con il minor numero possibile di parti custom:

1. creare un Eco;
2. caricare testo e media;
3. generare o salvare una lettera;
4. sigillare l'Eco;
5. scegliere una data;
6. inviare l'Eco via email;
7. aprire una pagina Eco tramite token/QR.

---

## Architettura P0

```text
Browser
  ↓
Next.js app
  ↓
Supabase Postgres ── Supabase Storage
  ↓
Vercel Cron
  ↓
Resend
  ↓
Email utente con link /e/[token]
```

---

## Componenti

### Frontend

- Next.js App Router.
- TypeScript.
- shadcn/ui.
- Tailwind CSS.
- Flow mobile-first.
- Nessuna dashboard complessa nel P0.

### Backend

- Next.js Route Handlers / Server Actions.
- Supabase client server-side.
- API interne per:
  - creazione Eco;
  - upload media;
  - sigillo;
  - scheduling;
  - consegna email;
  - apertura token.

### Database

Supabase Postgres con tabelle minime:

- `users`;
- `echoes`;
- `echo_assets`;
- `delivery_jobs`;
- `echo_access_tokens`;
- `delivery_events`.

### Storage

Supabase Storage per:

- foto;
- audio;
- video.

Gli asset devono essere privati. La pagina Eco li espone solo tramite token valido.

### Email

Resend per:

- conferma sigillo;
- consegna Eco alla data scelta;
- eventuale retry manuale o automatico.

### Scheduler

Vercel Cron chiama un endpoint protetto, ad esempio:

```text
GET /api/jobs/deliver-echoes
```

L'endpoint:

1. cerca job `scheduled` con `deliveryDate <= now`;
2. invia email tramite Resend;
3. marca il job come `delivered` o `delivery_failed`;
4. registra evento in `delivery_events`.

### Token e QR

- Token random ad alta entropia.
- Route pubblica: `/e/[token]`.
- Nessun ID sequenziale nel link pubblico.
- Token revocabile internamente.
- QR generato dal link tokenizzato.

---

## Fuori dal P0 tecnico

- WhatsApp.
- Lettera fisica.
- Pricing.
- Marketplace.
- Recovery account avanzata.
- Admin complesso.
- App mobile nativa.
- Infrastruttura custom.

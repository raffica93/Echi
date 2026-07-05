# Eco — Data Model e Content Structure

## Obiettivo

Definire la struttura logica di un Eco senza entrare ancora in implementazione definitiva.

---

## Entità principali

### User

```ts
type User = {
  id: string;
  email: string;
  phone?: string;
  createdAt: string;
  verifiedEmail: boolean;
  verifiedPhone?: boolean;
  plan: 'free' | 'personal' | 'premium';
  maxEchoes: number; // free: 1, personal/premium: 3
};
```

### Echo

```ts
type Echo = {
  id: string;
  userId: string;
  title: string;
  status: 'draft' | 'sealed' | 'scheduled' | 'preparing_delivery' | 'delivered' | 'delivery_failed' | 'opened';
  createdAt: string;
  sealedAt?: string;
  deliveryDate?: string;
  minimumDeliveryDate: string;
  maximumDeliveryDate: string;
  letterText: string;
  coverPhotoAssetId?: string;
  deliveryChannels: DeliveryChannel[];
  deliveryAccessTier: 'email_free' | 'premium_physical';
  mediaAccessExpiresAt?: string;
  aiAssisted: boolean;
  immutableAfterSeal: boolean;
};
```

### EchoAsset

```ts
type EchoAsset = {
  id: string;
  echoId: string;
  type: 'photo' | 'audio' | 'video';
  storageUrl: string;
  filename: string;
  mimeType: string;
  sizeBytes: number;
  uploadedAt: string;
  isCover?: boolean;
};
```

### DeliveryChannel

```ts
type DeliveryChannel = {
  type: 'email';
  target: string;
  verified: boolean;
  fallbackEmail?: string;
  lastVerifiedAt?: string;
};
```

### EchoReceipt

```ts
type EchoReceipt = {
  echoId: string;
  receiptCode: string;
  createdAt: string;
  deliveryDate: string;
  selectedChannel: 'email';
  deliveryUpdateUrl: string;
};
```

---

## Struttura dell'Eco

Un Eco dovrebbe essere composto da:

1. **Titolo** — generato o scritto dall'utente.
2. **Foto principale** — raccomandata, non obbligatoria nel primo MVP.
3. **Lettera/testo** — corpo principale.
4. **Media allegati** — audio/video/foto aggiuntive.
5. **Data creazione** — parte del valore emotivo.
6. **Data consegna** — quando l'Eco torna.
7. **Canale di consegna** — email nel P0.
8. **Sigillo** — stato di immodificabilità.

---

## Validazioni

### Prima del sigillo

- Titolo presente.
- Testo o audio/video presente.
- Data consegna >= oggi + 1 mese.
- Data consegna <= oggi + 5 anni per il primo MVP tecnico.
- Almeno un canale di consegna valido.
- Email verificata sempre presente, anche come fallback.
- Conferma esplicita immodificabilità.

### Dopo il sigillo

Campi non modificabili:

- titolo;
- lettera;
- media;
- data creazione;
- contenuto Eco.

Campi modificabili solo come dati logistici:

- email di consegna;
- fallback email.

Nota: consentire la modifica del canale può essere necessario per affidabilità, ma va separato dalla modifica del contenuto. L'utente non deve rientrare nell'editor dell'Eco.

---

## Security baseline

- Asset privati in object storage.
- URL non pubblici.
- Link firmati o tokenizzati.
- QR code con token random non sequenziale.
- Per media sensibili, possibile unlock aggiuntivo con email o codice Eco.
- Backup automatico.
- Audit log su sigillo e consegna.

---

## Eventi analytics

```ts
type EchoAnalyticsEvent =
  | 'echo_started'
  | 'media_uploaded'
  | 'ai_draft_generated'
  | 'echo_preview_viewed'
  | 'echo_seal_started'
  | 'echo_sealed'
  | 'delivery_date_selected'
  | 'delivery_channel_selected'
  | 'delivery_contact_updated'
  | 'echo_receipt_saved'
  | 'final_screen_viewed'
  | 'echo_delivered'
  | 'echo_opened';
```

## Nota architetturale

La conservazione a lungo termine è un requisito core. Lo storage non può essere trattato come allegato temporaneo: gli asset devono avere lifecycle policy coerenti con la promessa di consegna.

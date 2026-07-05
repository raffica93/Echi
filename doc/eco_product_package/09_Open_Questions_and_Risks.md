# Eco — Decisioni Integrate e Rischi

## Decisioni integrate

### 1. La foto deve essere obbligatoria?

Pro:

- aumenta impatto emotivo;
- rende l'Eco più personale;
- collega sogno/persona/momento.

Contro:

- aumenta frizione;
- alcuni utenti non vorranno caricare foto;
- temi privacy.

Decisione: fortemente raccomandata nel MVP, non obbligatoria. L'interfaccia può suggerire una foto prima del sigillo, ma non deve bloccare l'utente.

---

### 2. Lettera fisica nel MVP?

Pro:

- differenziazione immediata;
- prodotto più vendibile;
- esperienza memorabile.

Contro:

- operativamente pesante;
- costi;
- complessità indirizzi, resi, fornitori.

Decisione: fuori dal Prodotto 0. Il prototipo usa solo email e link/QR tokenizzato.

---

### 3. Come gestire cambi di email, numero o indirizzo?

Il prodotto invita l'utente a dimenticarsi dell'app, ma i canali possono cambiare.

Possibili soluzioni:

- email fallback sempre obbligatoria;
- ricevuta con link per aggiornare dati di consegna;
- reminder amministrativo annuale molto discreto;
- possibilità di aggiornare solo i dati di consegna, non il contenuto.

Decisione: rendere modificabile solo l'email di consegna tramite ricevuta Eco, magic link o recovery account. Per consegne oltre 12 mesi è ammesso un controllo amministrativo discreto a 30 giorni.

---

### 4. Quanto deve durare l'accesso ai media?

Opzioni:

- accesso permanente;
- accesso per 1 anno dalla consegna;
- download immediato consigliato.

Decisione P0: landing attiva almeno 12 mesi dopo la consegna. Alla consegna, invitare al download del pacchetto.

---

### 5. Eco condiviso

Molto coerente con l'origine del prodotto: spiaggia, amici, falò, sogni condivisi.

Rischio: complessità multiutente.

Decisione: seconda fase, non MVP.

### 6. WhatsApp

Decisione: fuori dal Prodotto 0.

### 7. Pricing iniziale

Decisione: fuori dal Prodotto 0. Non introdurre marketplace o monetizzazione nel prototipo funzionante.

### 8. Nome prodotto

Decisione: Eco confermato per MVP. Prima del lancio pubblico serve verifica legale/trademark.

---

## Rischi UX

### Rischio 1 — Troppa spiegazione

Se l'app spiega troppo il significato identitario, rovina la spontaneità.

Mitigazione: usare copy semplice durante creazione; lasciare il pivot alla consegna.

### Rischio 2 — Sembra una app motivazionale

Se si usano parole come obiettivi, progressi, KPI, abitudini, l'utente la interpreta come tracker.

Mitigazione: eliminare progressi, dashboard, reminder e metriche personali.

### Rischio 3 — Sigillo poco credibile

Se il sigillo sembra solo un bottone, perde forza.

Mitigazione: animazione, copy, conferma esplicita, stato read-only reale.

### Rischio 4 — Consegna fallita

Se l'Eco non arriva, il prodotto fallisce.

Mitigazione: fallback email, monitoring, retry, audit log, verifica contatti.

---

## Rischi tecnici

- Conservazione media a lungo termine.
- Costi storage video.
- Scheduler affidabile su orizzonti lunghi.
- Deliverability email.
- Generazione QR sicura.
- GDPR/data retention.

---

## Rischi legali/privacy

- Contenuti molto personali o sensibili.
- Indirizzi fisici.
- Media di terzi nelle foto/video.
- Conservazione per anni.
- Richieste cancellazione dati.
- Diritto all'oblio.

Mitigazione minima MVP:

- termini chiari;
- privacy policy;
- cancellazione account;
- consenso esplicito per consegna futura;
- separare contenuto Eco da dati di spedizione.

---

## Rischio di monetizzazione futura

Fuori dal Prodotto 0. Da riaprire solo dopo aver validato creazione, sigillo, consegna email e apertura.

## Prossima validazione consigliata

Creare un prototipo funzionante:

1. app Next.js mobile-first;
2. form di creazione Eco;
3. upload media su Supabase Storage;
4. sigillo;
5. QR/link tokenizzato a pagina privata;
6. invio email con Resend dopo 1 mese a 5-10 beta tester.

Obiettivo: capire se, alla ricezione, le persone percepiscono emozione, sorpresa e valore.

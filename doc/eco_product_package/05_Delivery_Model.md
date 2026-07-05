# Eco — Modello di Consegna

## Premessa

La consegna è il momento più importante del prodotto. Tutto il valore accumulato durante la creazione viene rilasciato quando l'Eco torna.

L'app può essere dimenticata, ma il sistema deve mantenere la promessa.

---

## Decisione P0

- **Canale unico:** email verificata.
- **Accesso contenuti:** link/QR tokenizzato alla landing Eco.
- **Invio:** Resend.
- **Scheduling:** Vercel Cron su endpoint protetto.

WhatsApp, lettera fisica e pricing sono fuori dal Prodotto 0.

---

## Canale previsto

## 1. Email

### Pro

- Semplice da implementare.
- Economica.
- Scalabile.
- Non richiede installazione app.
- Buona per MVP.

### Contro

- Può finire in spam.
- Meno memorabile.
- Dipende dal fatto che l'email rimanga attiva nel tempo.

### Requisiti

- Verifica email in fase di creazione.
- Controllo interno deliverability prima della data di consegna.
- Tracking apertura opzionale.
- Link sicuro alla landing dell'Eco.
- Retry automatico in caso di errore temporaneo.

---

---

## Link e QR

Il QR deve aprire una landing page dedicata con:

- foto;
- audio;
- video;
- testo;
- download opzionale.

### Requisiti

- Token univoco.
- Non indicizzabile.
- Link firmato o token random ad alta entropia.
- Landing attiva per il periodo definito dal P0.
- Download del pacchetto consigliato alla prima apertura.

---

## Copy consegna futura

```text
È arrivato il momento di sentire il tuo Eco.

Tempo fa hai lasciato queste parole al futuro. Oggi tornano da te.

Forse allora pensavi di parlare di un sogno. Forse quel sogno è cambiato, forse lo hai realizzato, forse no.

Ma questo Eco conserva qualcosa che non poteva restare fermo in nessun altro modo: una versione di te in quel preciso momento.
```

---

## Delivery states

- `draft`: Eco in creazione.
- `sealed`: Eco sigillato.
- `scheduled`: consegna programmata.
- `preparing_delivery`: email in preparazione.
- `delivered`: consegna inviata.
- `delivery_failed`: errore di consegna.
- `opened`: link/QR aperto.

---

## Fallback e retry

Per il P0 il fallback è sempre sullo stesso canale email:

- errore temporaneo provider → retry;
- bounce o errore permanente → `delivery_failed`;
- link/QR errore → support flow minimale.

---

## Aggiornamento dati di consegna

Il contenuto dell'Eco non si modifica mai dopo il sigillo. I dati logistici possono invece cambiare, perché servono a mantenere la promessa di consegna.

Campi aggiornabili dopo il sigillo:

- email di consegna;
- fallback email;

L'aggiornamento deve avvenire tramite ricevuta Eco, magic link o recovery account. Non deve riaprire editor, AI assist o contenuti dell'Eco.

Per consegne oltre 12 mesi, il sistema può inviare un controllo amministrativo discreto a 30 giorni dalla consegna. Il messaggio deve essere pratico, non motivazionale.

---

## Durata accesso media

- Landing P0 attiva per almeno 12 mesi dalla consegna.
- Prima della scadenza, l'utente deve poter scaricare testo e media.
- La cancellazione account o richiesta GDPR prevale sulla conservazione.

---

## Ricevuta Eco

Dopo il sigillo serve una ricevuta minimale, scaricabile o inviata via email, con:

- codice Eco;
- data creazione;
- data consegna;
- canale scelto;
- link per aggiornare i soli dati di consegna;
- conferma che il contenuto è sigillato e non modificabile.

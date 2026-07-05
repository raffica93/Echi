# Eco — Prodotto 0 Backlog

## Priorità P0 — Necessario per un prototipo funzionante

### EPIC 1 — Creazione Eco

- Come utente, voglio iniziare un nuovo Eco.
- Come utente, voglio scrivere un testo libero.
- Come utente, voglio caricare una foto.
- Come utente, voglio registrare/caricare audio.
- Come utente, voglio caricare video.
- Come utente, voglio vedere un'anteprima del mio Eco.

### EPIC 2 — AI assist

- Come utente, voglio trasformare il mio materiale grezzo in una bozza leggibile.
- Come utente, voglio poter accettare/modificare la bozza.
- Come sistema, devo impedire all'AI di creare piani d'azione o coaching.

### EPIC 3 — Sigillo

- Come utente, voglio sigillare l'Eco.
- Come utente, devo capire che dopo il sigillo non posso modificarlo.
- Come sistema, devo rendere l'Eco read-only dopo il sigillo.
- Come utente, voglio vedere una schermata finale memorabile.

### EPIC 4 — Scheduling

- Come utente, voglio scegliere quando sentire il mio Eco.
- Come sistema, devo impedire date inferiori a 1 mese.
- Come sistema, devo salvare una consegna programmata.

### EPIC 5 — Consegna email

- Come utente, voglio ricevere l'Eco via email.
- Come sistema, devo inviare l'email nella data scelta.
- Come sistema, devo tracciare fallimento/consegna/apertura.
- Come sistema, devo gestire retry e fallback in caso di errore temporaneo.

### EPIC 6 — Ricevuta e aggiornamento dati consegna

- Come utente, voglio salvare una ricevuta del mio Eco sigillato.
- Come utente, voglio aggiornare email o dati di consegna senza modificare il contenuto.
- Come sistema, devo separare contenuto sigillato e dati logistici.

---

## Priorità P1 — Dopo validazione P0

### EPIC 7 — QR landing

- Generare QR code per pagina Eco.
- Creare pagina di visualizzazione Eco.
- Mostrare foto/audio/video/testo.
- Proteggere accesso con token.
- Consentire download del pacchetto dopo la consegna.

### EPIC 8 — Eco condiviso

- Creazione gruppo.
- Inviti amici.
- Ogni partecipante crea il proprio Eco.
- Data unica di consegna.
- Consegna simultanea.

### EPIC 9 — Packaging premium

- Lettera fisica premium.
- Cofanetto.
- Carta/foto stampata.
- QR card.

### EPIC 10 — Recovery e resilienza

- Aggiornamento email/numero/indirizzo senza modificare contenuto.
- Recovery account dopo anni.
- Reminder amministrativo silenzioso prima della consegna.
- Policy accesso media dopo consegna.

---

## Non-goal MVP

- Dashboard obiettivi.
- KPI personali.
- Checklist.
- Reminder motivazionali.
- Future interview.
- WhatsApp.
- Lettera fisica.
- Pricing.
- Social feed.
- Commenti/like.
- Algoritmi di crescita personale.
- Consigli su dimagrimento, carriera, soldi, salute.

---

## Prodotto 0 consigliato

### Versione 0.1

Web app responsive con Next.js + shadcn/ui + Supabase + Resend:

1. crea Eco;
2. testo + foto + audio/video;
3. AI bozza;
4. sigillo;
5. scegli data;
6. scegli email;
7. salva ricevuta;
8. aggiorna dati di consegna se necessario;
9. ricezione email futura.

### Versione 0.2

1. QR landing;
2. download contenuti dopo consegna;
3. hardening scheduler/email.

### Versione 0.3

1. Eco condiviso;
2. eventuale lettera fisica;
3. eventuale WhatsApp.

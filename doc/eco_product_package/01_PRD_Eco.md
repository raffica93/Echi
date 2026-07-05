# PRD — Eco

**Versione:** 0.3  
**Data:** 05 luglio 2026  
**Stato:** Concept / MVP definition  
**Nome prodotto:** Eco  
**Categoria:** Time capsule personale / esperienza emotiva digitale-fisica  

---

## 1. Executive Summary

**Eco** è una macchina del tempo personale che permette a una persona di creare un messaggio per il proprio sé futuro, arricchito con testo, foto, audio e video, sigillarlo in modo immodificabile e riceverlo dopo un intervallo minimo di un mese.

Il prodotto non serve a raggiungere un obiettivo, monitorare progressi o costruire abitudini. L'app/sito è pensato per essere usato una volta, o pochissime volte, e poi dimenticato o disinstallato. La promessa è custodire un frammento autentico del presente e farlo riemergere nel futuro.

La scoperta emotiva più importante non viene esplicitata all'utente durante la creazione: quando riceverà l'Eco, capirà che il sogno raccontava chi era in quel momento molto più di quanto racconti se il sogno sia stato realizzato o meno.

---

## 2. Problema

Le app di obiettivi, journaling e motivazione tendono a trasformare il desiderio in performance:

- checklist;
- KPI personali;
- streak;
- reminder;
- senso di colpa se non si completa;
- frizione quotidiana.

Molte persone, però, non hanno bisogno di un altro sistema per fare. Hanno bisogno di conservare un momento, una versione di sé, un sogno, un'intenzione o una promessa personale prima che il tempo la modifichi.

---

## 3. Insight centrale

> Il sogno che scegli per il futuro racconta chi sei oggi più del fatto che tu lo realizzi davvero.

L'Eco nasce da una situazione reale: una notte in spiaggia, con amici, falò e tenda, in cui un gruppo ha scritto sogni e cose che desiderava fare. Molti di quei desideri erano influenzati dal confronto sociale: cose che altri facevano e loro no. Un anno dopo, rileggere quei pensieri è stato bello non perché tutti si fossero realizzati, ma perché riportavano alla luce la versione delle persone che li avevano scritti.

Questo è il core emotivo del prodotto: non conservare il risultato, ma la persona.

---

## 4. Visione prodotto

Eco deve sembrare meno una app e più un rituale.

L'utente entra, crea un Eco, lo arricchisce, lo sigilla, sceglie quando sentirlo e come riceverlo. Dopo il sigillo, il prodotto sparisce. Non chiede attenzione. Non monitora. Non giudica.

Quando arriva il momento, l'Eco torna come una voce del passato.

---

## 5. Posizionamento

### Formula breve

**Eco è una macchina del tempo che conserva una versione autentica di te e la consegna, più avanti, alla persona che sarai diventata.**

### Non è

- una app motivazionale;
- una app di produttività;
- un goal tracker;
- un habit tracker;
- un diario quotidiano;
- un coach;
- una piattaforma social.

### È

- una capsula emotiva;
- una promessa sigillata;
- una lettera del presente al futuro;
- un frammento di identità non dichiarato esplicitamente durante la creazione;
- una esperienza one-shot.

---

## 6. Utenti target iniziali

### 6.1 Persona primaria — giovane adulto in fase di transizione

Persone tra 18 e 35 anni che vivono passaggi significativi:

- fine scuola/università;
- primo lavoro;
- cambio città;
- viaggio importante;
- rottura o nuova relazione;
- desiderio di cambiare vita;
- fase di crescita personale.

### 6.2 Persona secondaria — gruppi di amici

Persone che condividono un momento emotivo e vogliono fissarlo:

- viaggi;
- serate simboliche;
- addii al celibato/nubilato;
- maturità/laurea;
- trasferimenti;
- momenti di gruppo.

**Nota:** per l'MVP si può partire dall'Eco personale. L'Eco condiviso è un'estensione molto coerente, ma non obbligatoria per la prima release.

---

## 7. Scope Prodotto 0

Il Prodotto 0 è un prototipo funzionante, non una piattaforma completa. Deve validare il rituale principale: creare un Eco, sigillarlo, programmarlo e riceverlo via email con accesso tokenizzato ai contenuti.

### In scope P0

1. Creazione di 1 Eco per utente nel prototipo.
2. Ogni Eco può contenere:
   - testo;
   - foto;
   - audio;
   - video.
3. AI di supporto nella fase iniziale, opzionale se non rallenta il prototipo.
4. Sigillo immodificabile.
5. Tempo minimo di consegna: 1 mese.
6. Scelta data di consegna.
7. Consegna email come unico canale.
8. Link/QR landing con token sicuro per accedere a foto/audio/video.
9. Schermata finale di sigillo.
10. Nessuna dashboard di progressi dopo il sigillo.

### Out of scope P0

- tracking progressi;
- reminder periodici;
- modifica dell'Eco dopo il sigillo;
- gamification;
- community/social feed;
- future interview;
- recupero continuo dell'utente;
- AI coach dopo il sigillo;
- gestione contatto in caso di morte;
- privacy avanzata end-to-end come claim principale;
- marketplace o monetizzazione complessa;
- WhatsApp;
- lettera fisica;
- pricing;
- recovery account avanzata;
- stampa e spedizione fisica automatizzata;

---

## 8. Regole di prodotto non negoziabili

### 8.1 Massimo 3 Echi

L'utente può creare al massimo 3 Echi. Questo mantiene scarsità, intenzionalità e valore simbolico.

### 8.2 L'Eco è immodificabile dopo il sigillo

Prima del sigillo, l'utente può modificare. Dopo il sigillo, no.

Il sigillo è il momento di commitment emotivo e deve avere una forte resa visiva.

### 8.3 Minimo 1 mese

Non si può ricevere un Eco prima di un mese. Sotto questa soglia si perde l'effetto di macchina del tempo.

Per il primo MVP tecnico la data massima selezionabile è 5 anni dalla creazione. Questo permette di mantenere la promessa su un orizzonte lungo ma ancora controllabile per storage, scheduler, policy dei provider e assistenza.

### 8.4 L'app deve poter essere dimenticata

Dopo il sigillo, il prodotto non deve richiedere attenzione. L'esperienza ideale è:

> crea → sigilla → scegli consegna → dimentica → ricevi.

### 8.5 L'utente non deve sapere esplicitamente che sta creando una fotografia identitaria

Durante la creazione non bisogna dire:

- "stiamo catturando chi sei";
- "questa è una fotografia di te";
- "analizzeremo la tua identità".

L'utente deve pensare di star raccontando un sogno o un messaggio. Il significato profondo emerge solo quando riceve la lettera.

---

## 9. User Journey MVP

### Step 1 — Landing / Benvenuto

Obiettivo: introdurre Eco come macchina del tempo, senza spiegare troppo.

Messaggio chiave:

> Ogni Eco è una parte di te che attraversa il tempo.

### Step 2 — Creazione dell'Eco

Domanda guida:

> Cosa vuoi scaricare al mondo?

Interpretazione: l'Eco è ciò che vuoi depositare fuori da te, affidandolo al tempo.

L'utente inserisce contenuto grezzo:

- testo libero;
- foto del momento fortemente raccomandata, ma non obbligatoria nel primo MVP;
- audio;
- video.

### Step 3 — AI come ordinatore/intervistatore leggero

L'AI aiuta a dare forma all'Eco:

- propone un titolo;
- organizza il testo;
- può fare poche domande naturali se mancano informazioni;
- trasforma materiale grezzo in una lettera coerente;
- mantiene tono, parole e autenticità dell'utente.

L'AI non deve diventare coach, terapeuta o project manager.

### Step 4 — Anteprima Eco

L'utente vede:

- titolo;
- testo/lettera;
- foto principale;
- media allegati;
- data di creazione.

Può ancora modificare.

### Step 5 — Sigillo

CTA primaria:

> Sigilla il mio Eco

Warning:

> Dopo il sigillo, questo Eco non potrà più essere modificato.

### Step 6 — Tempo

Domanda:

> Quando vuoi sentire il tuo Eco?

Opzioni:

- tra 1 mese;
- tra 6 mesi;
- tra 1 anno;
- tra 3 anni;
- tra 5 anni;
- scegli una data.

### Step 7 — Canale di consegna

Domanda:

> Come vuoi che il tuo Eco ti raggiunga?

Canali iniziali:

- email;
- QR/link sicuro alla pagina dell'Eco.

### Step 8 — Conferma finale

Schermata di sigillo:

```text
ECO SIGILLATO

Creato il: 05 luglio 2026
Lo sentirai il: 05 luglio 2027

Da questo momento non potrà più essere modificato.

Ora dimenticati di noi.
Ci rivedremo quando sarà il momento.
```

---

## 10. Esperienza di consegna

La consegna deve essere il climax del prodotto.

### 10.1 Email

**Decisione MVP:** email è il canale principale del primo rilascio. Tutti gli altri canali devono avere una email verificata come fallback.

Email minimale, non commerciale, con tono rituale.

Oggetto possibile:

> È arrivato il momento di sentire il tuo Eco

Contenuto:

- introduzione emotiva;
- testo/lettera;
- link sicuro ai media;
- foto principale embedded o come cover.

### 10.2 WhatsApp

Fuori dal Prodotto 0. Può essere rivalutato solo dopo la validazione della consegna email.

### 10.3 Lettera fisica

Fuori dal Prodotto 0. Resta una possibile estensione futura, ma non deve influenzare architettura, backlog o validazione iniziale.

Contenuto possibile:

- lettera stampata;
- foto principale;
- QR code verso pagina web con foto/audio/video;
- codice identificativo Eco;
- packaging semplice ma memorabile.

La lettera fisica è probabilmente il feature/bundle premium più potente, ma non appartiene al prototipo funzionante iniziale.

---

## 11. Output della lettera: il pivot nascosto

Durante la creazione, l'utente crede di star lasciando un messaggio o un sogno al futuro.

Nel momento della consegna, la lettera può rivelare una prospettiva più profonda:

> Quando hai scritto questo Eco, forse pensavi di parlare del futuro. In realtà hai conservato qualcosa di ancora più raro: una versione di te che oggi non esiste più nello stesso modo.

Questo non deve sembrare manipolativo. Deve essere delicato, quasi una cornice poetica.

### Regola UX

Non anticipare questa lettura durante la creazione. Deve emergere solo in output.

---

## 12. Requisiti funzionali

### FR-001 — Creazione account leggera

Il sistema deve permettere all'utente di salvare un Eco e associare almeno un canale di consegna valido.

### FR-002 — Limite massimo di 3 Echi

Il sistema deve impedire la creazione di più di 3 Echi per utente. Nel piano gratuito l'MVP permette 1 Eco via email; nel piano personale/premium il limite resta 3.

### FR-003 — Upload contenuti

Il sistema deve supportare:

- testo;
- foto principale raccomandata;
- audio;
- video.

Per sigillare un Eco serve almeno un contenuto sostanziale tra testo, audio o video. La foto aumenta il valore emotivo ma non deve impedire la creazione nel primo MVP.

### FR-004 — AI drafting

Il sistema deve permettere di generare una bozza ordinata dell'Eco a partire dai contenuti dell'utente.

### FR-005 — Anteprima modificabile

Prima del sigillo, l'utente deve poter modificare testo, titolo e media.

### FR-006 — Sigillo immodificabile

Dopo il sigillo, l'Eco deve diventare read-only.

### FR-007 — Scheduling consegna

Il sistema deve schedulare una consegna con data minima pari ad almeno un mese dalla creazione.

### FR-008 — Canale consegna

Il sistema deve usare email come unico canale di consegna del Prodotto 0.

### FR-009 — QR code

Il sistema deve generare un token sicuro e un link/QR che aprono una landing dell'Eco con contenuti multimediali.

### FR-010 — Final screen

Dopo il sigillo, il sistema deve mostrare una schermata conclusiva forte, con data di consegna e messaggio di chiusura.

---

## 13. Requisiti non funzionali

### Affidabilità

La consegna deve essere estremamente affidabile. Il prodotto vive o muore sulla fiducia che l'Eco torni nel giorno stabilito.

### Sicurezza minima

Per MVP:

- storage sicuro;
- accesso autenticato;
- link media non indicizzabile;
- token univoci e revocabili;
- backup.

La privacy non è il focus narrativo iniziale, ma deve essere gestita con serietà.

### Longevità

Il sistema deve essere progettato per conservare contenuti per mesi o anni. Serve una strategia di storage, backup e gestione scadenze.

Decisione P0: orizzonte massimo di consegna pari a 5 anni. Dopo la consegna, la landing media resta attiva per almeno 12 mesi. L'utente deve poter scaricare il contenuto alla consegna.

### Portabilità

I media devono essere esportabili/recuperabili internamente per generare output email/lettera/QR.

---

## 14. Metriche prodotto

Attenzione: queste non sono KPI dell'utente. Sono metriche interne di prodotto.

### Activation

- % utenti che iniziano un Eco e arrivano al sigillo.
- Tempo medio di completamento.
- % utenti che caricano una foto.
- % utenti che usano audio/video.

### Emotional completion

- % utenti che scelgono una data oltre 6 mesi.
- % utenti che leggono la schermata finale.
- % utenti che scaricano/salvano ricevuta Eco.

### Delivery

- % consegne riuscite.
- % aperture link dopo consegna.
- % QR code scansionati.

---

## 15. Stack Tecnologico P0

### Frontend

- **Framework:** Next.js con TypeScript.
- **UI:** shadcn/ui + Tailwind CSS.
- **Flow:** web app responsive/mobile-first, lineare, non dashboard-centrica.
- **Upload:** progress chiaro per media.
- **Sigillo:** animazione o micro-interazione dedicata.

### Backend

- **Runtime/API:** Next.js Route Handlers / Server Actions.
- **Database:** Supabase Postgres.
- **Auth/account leggero:** Supabase Auth o magic link via email.
- **Storage media:** Supabase Storage.
- **Email delivery:** Resend.
- **Scheduler:** Vercel Cron giornaliero su endpoint protetto.
- **QR/token:** token random ad alta entropia, route `/e/[token]`.
- **Stato Eco:** draft → sealed → scheduled → delivered → opened.

### AI Layer

- Input: testo, trascrizione audio/video se disponibile, eventuali note.
- Output: titolo, lettera ordinata, tono coerente.
- Guardrail: non inventare dettagli, non fare coaching, non generare piano d'azione.
- Nel Prodotto 0 l'AI è opzionale: entra solo se non rallenta creazione, sigillo, scheduling ed email.

---

## 16. Decisioni integrate per MVP

1. Email è il solo canale P0 di consegna.
2. WhatsApp è fuori dal Prodotto 0.
3. Lettera fisica è fuori dal Prodotto 0.
4. Foto fortemente raccomandata, non obbligatoria nel primo MVP.
5. Eco condiviso resta seconda fase dopo validazione dell'Eco personale.
6. Pricing fuori dal Prodotto 0.
7. Orizzonte massimo MVP: consegna entro 5 anni.
8. Dopo il sigillo, il contenuto resta immutabile; email, numero, indirizzo e fallback possono essere aggiornati tramite ricevuta o recovery, senza modificare l'Eco.
9. Recupero account via email verificata/magic link; per casi senza accesso, support flow manuale con verifica minima.
10. Nome Eco confermato per MVP; eventuale cambio solo per vincoli legali o trademark.
11. Stack P0: Next.js + shadcn/ui + Supabase + Resend.

---

## 17. Principale rischio UX

Spiegare troppo.

Se il prodotto esplicita troppo il significato profondo, l'utente potrebbe performare una versione artificiale di sé. L'esperienza deve rimanere semplice:

> racconta qualcosa → sigilla → ricevi.

La profondità deve essere scoperta dopo.

---

## 18. North Star

**Percentuale di utenti che sigillano un Eco e, al momento della consegna, aprono il contenuto.**

Questa è la metrica che rappresenta davvero il valore del prodotto.

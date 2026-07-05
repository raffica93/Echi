# Eco — Product Package Completo

---

# 00_README.md

# Eco — Product Package

Questo pacchetto raccoglie le decisioni, le intuizioni e le regole di prodotto definite finora per **Eco**, una macchina del tempo personale che permette a una persona di creare un messaggio autentico oggi e riceverlo nel futuro.

## Contenuto

1. `01_PRD_Eco.md` — Product Requirements Document principale.
2. `02_Product_Vision_and_Principles.md` — visione, posizionamento e principi non negoziabili.
3. `03_UX_Flow_and_Microcopy.md` — flow end-to-end e microcopy chiave.
4. `04_AI_Interviewer_Behavior.md` — ruolo dell'AI nella creazione dell'Eco.
5. `05_Delivery_Model.md` — modello di consegna P0: email e link/QR tokenizzato.
6. `06_Data_Model_and_Content_Structure.md` — struttura logica dei dati e contenuti dell'Eco.
7. `07_MVP_Backlog.md` — backlog MVP, priorità e non-goal.
8. `08_Decision_Log.md` — decisioni già prese e razionale.
9. `09_Open_Questions_and_Risks.md` — decisioni residue integrate, rischi UX, tecnici e operativi.
10. `10_Technical_Stack_P0.md` — stack tecnologico scelto per il Prodotto 0.

## Nota di prodotto

Eco non è una app di produttività, coaching, habit tracking o goal management.

Eco è un rituale breve: crei un Eco, lo sigilli, scegli quando sentirlo, poi te ne dimentichi. Il valore emerge nel momento della consegna, quando l'utente scopre che il sogno raccontava soprattutto chi era nel momento in cui lo ha scritto.

---

# 01_PRD_Eco.md

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

---

# 02_Product_Vision_and_Principles.md

# Eco — Visione e Principi di Prodotto

## Visione

Eco è una macchina del tempo emotiva. Non aiuta l'utente a fare di più. Aiuta l'utente a conservare qualcosa di autentico e a farlo tornare quando il tempo lo avrà trasformato.

## Frase guida

> Crea un Eco. Sigillalo. Dimenticalo. Un giorno tornerà.

## Insight fondativo

Il sogno che una persona affida al futuro racconta chi era nel momento in cui lo ha scritto, anche se quel sogno non verrà mai realizzato.

Questo rende Eco diverso dalle app di obiettivi: non produce senso di colpa, perché il valore non dipende dall'esecuzione.

## Principi non negoziabili

### 1. Ritual over retention

Eco non deve massimizzare il daily active usage. Deve massimizzare la qualità del momento di creazione e la forza della consegna futura.

### 2. One-shot by design

L'esperienza deve poter durare 10-20 minuti. Dopo il sigillo, l'utente deve poter disinstallare o dimenticare l'app.

### 3. Scarcity creates meaning

Massimo 3 Echi. Se gli Echi sono infiniti, diventano note. Se sono pochi, diventano importanti.

### 4. Seal means seal

Dopo il sigillo, niente modifiche. La forza dell'Eco sta nella sua autenticità temporale.

### 5. No guilt mechanics

Niente streak, reminder motivazionali, progress tracking o dashboard di performance.

### 6. AI as mirror, not coach

L'AI aiuta l'utente a dare forma alle parole. Non deve dire cosa fare, non deve misurare, non deve creare piani d'azione.

### 7. The twist belongs to the future

Durante la creazione non bisogna dire all'utente che sta creando una fotografia identitaria. Questa consapevolezza deve emergere quando l'Eco torna.

### 8. Physical matters

La lettera fisica può essere il punto di differenziazione più forte: una busta reale che arriva nel futuro, con QR code verso audio, foto e video.

Per il rollout, la lettera fisica parte come prototipo manuale/premium dopo il P0 email. Il principio resta centrale, ma non deve rallentare la validazione del sigillo e della consegna.

## Anti-pattern da evitare

- Dashboard con progressi.
- Feed social.
- Badge e livelli.
- Reminder frequenti.
- Copy troppo terapeutico.
- Domande psicologiche troppo esplicite.
- Troppe configurazioni.
- Possibilità di modificare dopo il sigillo.
- Notifiche per far tornare l'utente nell'app.

## Tono

Minimalista, intimo, poetico ma non melenso. Deve sembrare una tecnologia silenziosa, non un guru motivazionale.

Parole vicine al brand:

- Eco;
- sigillo;
- sentire;
- tempo;
- voce;
- traccia;
- ritorno;
- presente;
- futuro;
- custodia.

Parole da usare con cautela:

- obiettivo;
- KPI;
- produttività;
- crescita personale;
- successo;
- fallimento;
- terapia;
- coaching.

---

# 03_UX_Flow_and_Microcopy.md

# Eco — UX Flow e Microcopy

## Obiettivo del flow

Portare l'utente da curiosità a sigillo con il minimo rumore possibile. Il flow deve essere breve, mobile-first, emotivo e senza sensazione di compilare un form burocratico.

---

## Flow principale

### 1. Landing

**Titolo:**

> Eco

**Sottotitolo:**

> Una macchina del tempo per le cose che vuoi lasciare al futuro.

**CTA:**

> Crea il tuo Eco

**Copy alternativo:**

> Scrivi qualcosa oggi. Sigillalo. Lo sentirai quando sarà il momento.

---

### 2. Intro rituale

**Titolo:**

> Ogni Eco attraversa il tempo.

**Body:**

> Puoi scrivere, parlare, caricare una foto o registrare un video. Quando lo sigillerai, non potrai più modificarlo.

**CTA:**

> Inizia

---

### 3. Creazione — domanda guida

**Titolo:**

> Cosa vuoi scaricare al mondo?

**Hint:**

> Un sogno, una promessa, una paura, una cosa che non vuoi dimenticare.

**Input:**

- textarea libera;
- upload foto;
- registra audio;
- carica video.

**Nota:** la foto del momento dovrebbe essere fortemente raccomandata.

**Decisione MVP:** la foto non blocca il sigillo. Se manca, l'interfaccia può suggerirla una sola volta prima dell'anteprima, senza colpevolizzare l'utente.

Copy upload foto:

> Aggiungi una foto di questo momento.

---

### 4. AI assist

**Titolo:**

> Ti aiuto a dargli forma?

**Body:**

> Posso ordinare quello che hai scritto senza cambiare la tua voce.

**CTA primaria:**

> Crea una bozza

**CTA secondaria:**

> Preferisco scriverlo da solo

---

### 5. Anteprima Eco

**Titolo:**

> Il tuo Eco

**Azioni:**

- modifica testo;
- cambia titolo;
- aggiungi media;
- rimuovi media;
- continua verso sigillo.

**CTA:**

> Continua

---

### 6. Sigillo

**Titolo:**

> Sei pronto a sigillare il tuo Eco?

**Warning:**

> Dopo questo momento non potrà più essere modificato.

**CTA primaria:**

> Sigilla il mio Eco

**CTA secondaria:**

> Torna a modificare

Possibile micro-interazione:

- pressione lunga sul pulsante;
- animazione di ceralacca/timbro;
- vibrazione leggera su mobile;
- suono soft opzionale.

---

### 7. Tempo

**Titolo:**

> Quando vuoi sentire il tuo Eco?

**Opzioni:**

- Tra 1 mese
- Tra 6 mesi
- Tra 1 anno
- Tra 3 anni
- Tra 5 anni
- Scegli una data

**Validazione:**

> La data deve essere almeno tra un mese.

---

### 8. Canale

**Titolo:**

> Come vuoi che il tuo Eco ti raggiunga?

**Opzioni:**

- Email
- Link sicuro alla pagina dell'Eco

**Copy email:**

> Riceverai il tuo Eco nella tua casella email.

**Copy aggiornamento dati di consegna:**

> Puoi aggiornare i dati di consegna senza riaprire il tuo Eco.

---

### 9. Conferma finale

**Titolo:**

> Eco sigillato

**Body:**

```text
Creato il: [data creazione]
Lo sentirai il: [data consegna]

Da questo momento non potrà più essere modificato.

Ora dimenticati di noi.
Ci rivedremo quando sarà il momento.
```

**CTA opzionale:**

> Salva ricevuta

**Nota UX:** non spingere a creare un altro Eco subito. Sarebbe contro il principio rituale.

---

## Copy per consegna futura

### Email subject

> È arrivato il momento di sentire il tuo Eco

### Intro email/lettera

> Tempo fa hai sigillato questo Eco. Oggi torna da te.

### Pivot delicato in output

> Forse allora pensavi di parlare del futuro. In realtà hai conservato anche qualcosa del tuo presente: una versione di te che oggi potresti non riconoscere più nello stesso modo.

### Chiusura

> Questo Eco è rimasto com'era. Ora appartiene a te.

---

## UX taboo

Durante la creazione evitare copy come:

- "scopri chi sei";
- "crea una fotografia della tua identità";
- "misura il tuo cambiamento";
- "raggiungi i tuoi obiettivi";
- "diventa la versione migliore di te".

Il prodotto deve essere più sottile.

---

# 04_AI_Interviewer_Behavior.md

# Eco — AI Interviewer Behavior

## Ruolo dell'AI

L'AI esiste solo nella fase iniziale di creazione. Dopo il sigillo, sparisce.

Il suo ruolo non è motivare, allenare, giudicare o pianificare. Il suo ruolo è aiutare l'utente a trasformare materiale grezzo in un Eco leggibile, coerente e autentico.

## Definizione sintetica

**AI as editor of memory, not coach of action.**

---

## Cosa può fare

### 1. Ordinare contenuto grezzo

Input dell'utente:

> Voglio andare via, aprire qualcosa di mio, non so bene cosa. Sono stanco di sentirmi fermo.

Output AI:

> Voglio ricordarmi questo momento: la sensazione di essere fermo, ma anche il desiderio di costruire qualcosa di mio. Non so ancora cosa sarà, ma so che non voglio ignorare questa spinta.

### 2. Proporre un titolo

Esempi:

- "Quando volevo cambiare strada"
- "Il giorno in cui ho deciso di non restare fermo"
- "Estate 2026 — Il mio primo Eco"

### 3. Fare poche domande naturali

Solo se necessario, massimo 2-3 domande.

Esempi:

- "Vuoi che questo Eco parli più di ciò che desideri o di ciò che stai vivendo adesso?"
- "C'è una persona, un luogo o un'immagine che vuoi associare a questo momento?"
- "Quando lo riceverai, cosa vorresti che il tuo futuro non dimenticasse?"

### 4. Mantenere la voce dell'utente

L'AI deve preservare:

- lessico;
- tono;
- imperfezioni significative;
- intensità emotiva;
- semplicità.

Non deve trasformare tutto in copy motivazionale generico.

### 5. Creare output per lettera

L'AI può produrre una versione stampabile/leggibile dell'Eco, mantenendo media separati e linkati tramite QR.

---

## Cosa non deve fare

- Non creare una lista di cose da fare.
- Non suggerire KPI personali.
- Non dire se il sogno è realistico.
- Non fare terapia.
- Non diagnosticare stati psicologici.
- Non proporre piani alimentari, finanziari, sportivi, lavorativi.
- Non correggere troppo lo stile.
- Non trasformare l'utente in un personaggio artificiale.
- Non parlare troppo del significato profondo dell'Eco durante la creazione.

---

## Prompt di sistema proposto

```text
Sei l'assistente di creazione di Eco, una macchina del tempo personale. Il tuo compito è aiutare l'utente a dare forma a un messaggio per il proprio sé futuro.

Non sei un coach, un terapeuta, un consulente o un project manager. Non devi creare piani d'azione, checklist, KPI o consigli su come raggiungere obiettivi.

Devi preservare la voce dell'utente, ordinare il materiale grezzo, proporre un titolo e una bozza di lettera autentica. Usa un tono intimo, semplice, non retorico. Non inventare dettagli non forniti. Se mancano elementi essenziali, fai al massimo tre domande brevi e naturali.

Durante la creazione non esplicitare che l'Eco è una fotografia identitaria dell'utente. L'utente deve percepire che sta lasciando un messaggio al futuro. Il significato più profondo emergerà solo al momento della consegna.
```

---

## Output JSON suggerito

```json
{
  "title": "Quando volevo cambiare strada",
  "letterDraft": "...",
  "suggestedCoverPhotoReason": "La foto caricata sembra adatta come immagine principale perché appartiene al momento dell'Eco.",
  "missingInputs": [
    "data di consegna",
    "canale di consegna"
  ],
  "tone": "intimo, diretto, non motivazionale"
}
```

---

## Varianti di AI experience

### Modalità minima MVP

- L'utente scrive/carica.
- Clicca "Crea una bozza".
- L'AI restituisce titolo e lettera.

### Modalità conversazionale

- L'AI dialoga con l'utente per 2-3 turni.
- Poi produce l'Eco.

### Modalità raw

- L'utente può disattivare l'AI e scrivere tutto da solo.

---

## Regola aurea

Se l'output AI sembra una frase da LinkedIn, è sbagliato.  
Se sembra una persona che parla al proprio futuro, è giusto.

---

# 05_Delivery_Model.md

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

---

# 06_Data_Model_and_Content_Structure.md

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

---

# 07_MVP_Backlog.md

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

---

# 08_Decision_Log.md

# Eco — Decision Log

## Decisioni prese

### 1. Numero di Echi

**Decisione:** massimo 3 Echi per utente.  
**Razionale:** un solo Eco è molto simbolico ma troppo restrittivo; infiniti Echi trasformerebbero il prodotto in una normale app di note/obiettivi. Tre mantiene valore, scarsità e libertà.

---

### 2. Modificabilità

**Decisione:** l'Eco è immodificabile dopo il sigillo.  
**Razionale:** l'autenticità deriva dal fatto che l'Eco resta fermo nel tempo.

---

### 3. Tempo minimo

**Decisione:** minimo 1 mese prima della consegna.  
**Razionale:** sotto un mese l'effetto macchina del tempo è debole.

---

### 4. Tipi di contenuto

**Decisione:** testo, foto, audio e video.  
**Razionale:** servono media personali e sensoriali per aumentare l'impatto emotivo al ritorno.

---

### 5. Identità prodotto

**Decisione:** Eco è una macchina del tempo.  
**Razionale:** posizionamento più forte rispetto a diario, app motivazionale o tracker.

---

### 6. Privacy

**Decisione:** gestire la privacy seriamente, ma non renderla il focus narrativo iniziale.  
**Razionale:** importante tecnicamente, ma il prodotto si vende sull'esperienza emotiva.

---

### 7. Consegna

**Decisione:** email come unico canale del Prodotto 0.  
**Razionale:** il prototipo deve validare creazione, sigillo, scheduling e ritorno dell'Eco senza dipendere da WhatsApp, stampa o logistica.

---

### 8. Ruolo AI

**Decisione:** AI solo nella fase iniziale.  
**Razionale:** l'AI deve aiutare a creare e ordinare l'Eco, non accompagnare l'utente dopo.

---

### 9. Nome contenuto

**Decisione:** il contenuto si chiama Eco.  
**Razionale:** un Eco è qualcosa che viene emesso una volta e ritorna dopo; metafora perfetta per l'esperienza.

---

### 10. Domanda di timing

**Decisione:** usare "Quando vuoi sentire il tuo Eco?".  
**Razionale:** più evocativo di "quando vuoi riceverlo"; rafforza la metafora della voce che torna.

---

### 11. Domanda iniziale

**Decisione:** usare "Cosa vuoi scaricare al mondo?" come possibile domanda fondante.  
**Razionale:** comunica deposito, rilascio, liberazione e passaggio temporale.

---

### 12. Pivot narrativo

**Decisione:** il prodotto sembra parlare di sogni durante la creazione, ma nella consegna rivela che il sogno raccontava chi eri.  
**Razionale:** se esplicitato prima, l'utente potrebbe performare un'identità artificiale. Il valore deve emergere dopo.

---

### 13. Schermata finale

**Decisione:** il sigillo a schermo è fondamentale.  
**Razionale:** è l'ultimo momento dell'app prima dell'oblio/disinstallazione. Deve essere memorabile e definitivo.

---

### 14. Canale Prodotto 0

**Decisione:** il Prodotto 0 usa email verificata come unico canale.  
**Razionale:** permette di validare creazione, sigillo, scheduler e consegna senza dipendere da policy WhatsApp o logistica fisica.

---

### 15. Lettera fisica

**Decisione:** la lettera fisica è fuori dal Prodotto 0.  
**Razionale:** è una possibile estensione, ma non serve per validare il prototipo funzionante.

---

### 16. WhatsApp

**Decisione:** WhatsApp è fuori dal Prodotto 0.  
**Razionale:** la consegna email è sufficiente per validare il ciclo principale e riduce dipendenze esterne.

---

### 17. Foto

**Decisione:** foto fortemente raccomandata, non obbligatoria nel primo MVP.  
**Razionale:** aumenta l'impatto emotivo, ma renderla obbligatoria può alzare troppo la frizione nella prima validazione.

---

### 18. Eco condiviso

**Decisione:** Eco condiviso dopo validazione dell'Eco personale.  
**Razionale:** è coerente con l'origine del prodotto, ma aggiunge complessità multiutente, inviti, consenso e consegna simultanea.

---

### 19. Aggiornamento contatti

**Decisione:** dopo il sigillo si possono aggiornare solo dati di consegna, mai il contenuto.  
**Razionale:** l'immodificabilità resta intatta, ma email, telefono e indirizzo devono poter cambiare per mantenere la promessa di consegna.

---

### 20. Pricing iniziale

**Decisione:** pricing fuori dal Prodotto 0.  
**Razionale:** il prototipo deve validare valore e consegna prima di introdurre piani, limiti commerciali o add-on.

---

### 21. Nome

**Decisione:** Eco resta il nome per MVP.  
**Razionale:** la metafora è precisa e già guida linguaggio, flow e identità. Da verificare solo eventuale vincolo legale/trademark prima del lancio pubblico.

---

### 22. Stack tecnologico P0

**Decisione:** Next.js + shadcn/ui + Supabase + Resend.  
**Razionale:** è lo stack più rapido per un prototipo funzionante con UI curata, storage media, database, auth leggera, scheduler e consegna email senza costruire infrastruttura custom.

---

# 09_Open_Questions_and_Risks.md

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

---

# 10_Technical_Stack_P0.md

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


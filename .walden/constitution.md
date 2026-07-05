# Project Constitution

This file captures stable project-wide context that applies across all features. It is optional and does not participate in the approval workflow.

## Project Summary

**Eco** e una macchina del tempo personale: una persona crea un messaggio autentico oggi, lo arricchisce con testo, foto, audio o video, lo sigilla in modo immodificabile e lo riceve nel futuro. Il progetto e in fase di **definizione Prodotto 0 / pre-MVP** e usa [Walden](https://github.com/raffica93/walden) per trasformare il product package in requisiti, design e task approvati.

- **Repository progetto:** https://github.com/raffica93/Echi
- **Repository Walden:** https://github.com/raffica93/walden
- **Product package:** `doc/eco_product_package/`
- **Stato:** ideazione Prodotto 0 — nessuna implementazione applicativa approvata

Eco non e una app di produttivita, coaching, habit tracking, journaling quotidiano, goal management o social feed. E un rituale breve: crea, sigilla, scegli quando sentirlo, dimentica, ricevi.

## Product Principles

- **Ritual over retention:** l'esperienza deve massimizzare il valore del momento di creazione e della consegna futura, non il ritorno quotidiano.
- **One-shot by design:** il flow principale deve durare circa 10-20 minuti e non richiedere attenzione dopo il sigillo.
- **Scarcity creates meaning:** massimo 3 Echi per utente; nel primo MVP gratuito puo bastare 1 Eco.
- **Seal means seal:** dopo il sigillo, contenuto, titolo, media e data di creazione non si modificano.
- **No guilt mechanics:** niente streak, KPI personali, progress tracking, reminder motivazionali, badge o dashboard di performance.
- **AI as mirror, not coach:** l'AI puo ordinare materiale grezzo e proporre titolo/lettera, ma non deve motivare, giudicare, consigliare, pianificare o creare checklist.
- **The twist belongs to the future:** durante la creazione non esplicitare che l'utente sta creando una fotografia identitaria; il pivot emerge solo alla consegna.
- **Physical matters later:** lettera fisica e packaging restano estensioni coerenti, ma sono fuori dal Prodotto 0.

## Product Scope P0

Il Prodotto 0 deve validare il ciclo principale personale:

1. creazione di un Eco personale;
2. input testo e media opzionali;
3. AI drafting opzionale se non rallenta il prototipo;
4. anteprima modificabile prima del sigillo;
5. sigillo immodificabile;
6. scelta data di consegna con minimo 1 mese e massimo 5 anni;
7. email verificata come canale unico P0;
8. ricevuta Eco e aggiornamento dei soli dati di consegna;
9. consegna via email con link/token sicuro;
10. landing tokenizzata per vedere e scaricare contenuti dopo la consegna.

Fuori dal P0: WhatsApp, lettera fisica, pricing, Eco condiviso, social feed, dashboard obiettivi, future interview, app mobile nativa, marketplace, recovery account avanzata, tracking di progresso e coaching.

## Tech Stack

Stack scelto per Prodotto 0:

- **Next.js** con TypeScript, App Router, Route Handlers e/o Server Actions.
- **shadcn/ui** + Tailwind CSS per UI mobile-first, controllabile e coerente.
- **Supabase** per Postgres, Auth leggera e Storage media privato.
- **Resend** per email transazionali.
- **Vercel** per deploy e Cron giornaliero su endpoint protetto.

Architettura P0:

```text
Browser
  -> Next.js app
  -> Supabase Postgres + Supabase Storage
  -> Vercel Cron
  -> Resend
  -> Email utente con link /e/[token]
```

## Data Model Direction

Entita minime previste:

- `users`
- `echoes`
- `echo_assets`
- `delivery_jobs`
- `echo_access_tokens`
- `delivery_events`

Stati Eco previsti: `draft`, `sealed`, `scheduled`, `preparing_delivery`, `delivered`, `delivery_failed`, `opened`.

Gli asset devono essere privati. La pagina Eco li espone solo tramite token valido. I token pubblici devono essere random, ad alta entropia, non sequenziali e revocabili internamente.

## UX And Copy Guardrails

Tono: minimalista, intimo, poetico ma non melenso. Deve sembrare una tecnologia silenziosa, non un guru motivazionale.

Microcopy stabile:

- Landing: "Una macchina del tempo per le cose che vuoi lasciare al futuro."
- Domanda iniziale: "Cosa vuoi scaricare al mondo?"
- AI assist: "Posso ordinare quello che hai scritto senza cambiare la tua voce."
- Timing: "Quando vuoi sentire il tuo Eco?"
- Sigillo: "Dopo questo momento non potra piu essere modificato."
- Chiusura: "Ora dimenticati di noi. Ci rivedremo quando sara il momento."

Evitare durante la creazione: "scopri chi sei", "fotografia della tua identita", "misura il tuo cambiamento", "raggiungi i tuoi obiettivi", "diventa la versione migliore di te".

## Conventions

- **Fonte prodotto:** `doc/eco_product_package/`.
- **Dati legacy:** `data/100cose.json`, CSV e TXT restano nel repository ma non rappresentano piu il prodotto Eco; non modificarli senza una feature spec dedicata.
- **Feature specs:** `.walden/specs/{feature-name}/` con nomi in kebab-case.
- **Workflow Walden:** Requirements -> Design -> Tasks -> Execute; ogni fase richiede approvazione esplicita.
- **Branch principale:** `main`.
- **Commit:** messaggi in italiano o inglese, descrittivi del cambiamento.

## Sanity Checks

```bash
python scripts/run_verification.py
python -m unittest discover -s tests -v
```

Per spec Walden:

```bash
walden status <feature-name> --json
walden validate <feature-name> --json
```

## Key Files

| File | Ruolo |
| --- | --- |
| `doc/eco_product_package/01_PRD_Eco.md` | PRD principale Eco |
| `doc/eco_product_package/02_Product_Vision_and_Principles.md` | Visione, principi e anti-pattern |
| `doc/eco_product_package/03_UX_Flow_and_Microcopy.md` | Flow e microcopy del rituale |
| `doc/eco_product_package/04_AI_Interviewer_Behavior.md` | Vincoli e output AI |
| `doc/eco_product_package/05_Delivery_Model.md` | Consegna email, token/QR, retry e ricevuta |
| `doc/eco_product_package/06_Data_Model_and_Content_Structure.md` | Entita logiche, stati e validazioni |
| `doc/eco_product_package/07_MVP_Backlog.md` | Backlog e priorita MVP |
| `doc/eco_product_package/08_Decision_Log.md` | Decisioni gia prese |
| `doc/eco_product_package/09_Open_Questions_and_Risks.md` | Rischi e decisioni integrate |
| `doc/eco_product_package/10_Technical_Stack_P0.md` | Stack tecnico P0 |
| `.walden/lessons.md` | Lezioni apprese dal workflow Walden |
| `.walden/specs/` | Feature specs Walden |

## Hard Rules

- Non avviare implementazione applicativa senza `requirements.md`, `design.md` e `tasks.md` approvati per la feature.
- Non trattare il contenuto sigillato come modificabile: solo dati logistici di consegna possono cambiare dopo il sigillo.
- Non introdurre meccaniche di produttivita, coaching, goal tracking o retention nel Prodotto 0.
- Non rendere obbligatoria la foto nel primo MVP; raccomandarla una sola volta senza bloccare.
- Non anticipare il pivot identitario durante la creazione.
- Usare il CLI Walden (`walden validate`, `walden review approve`, ecc.) per transizioni di stato deterministiche; non editare manualmente i frontmatter di approvazione.

# Project Constitution

This file captures stable project-wide context that applies across all features. It is optional and does not participate in the approval workflow.

## Project Summary

**Echi** è un progetto personale in fase di **ideazione pre-MVP**: una lista di 100 attività da fare nella vita, con testo e categoria per ogni voce. L'obiettivo futuro è trasformare questi dati in un'applicazione che permetta di consultare, tracciare e completare le attività — ma in questa fase si definiscono solo requisiti e design tramite [Walden](https://github.com/raffica93/walden).

- **Repository progetto:** https://github.com/raffica93/Echi
- **Repository Walden:** https://github.com/raffica93/walden
- **Stato:** ideazione — nessuna feature spec approvata, nessuno stack applicativo scelto

## Tech Stack

Non ancora definito. Il workspace contiene solo dati sorgente (JSON, CSV, TXT) e la struttura Walden per la spec-driven delivery. Quando si approverà un design, aggiornare questa sezione con linguaggi, framework e runtime scelti.

## Conventions

- **Dati canonici** in `data/` — non modificare `100cose.json` senza aggiornare le esportazioni correlate o documentare la divergenza.
- **Feature specs** in `.walden/specs/{feature-name}/` con nomi in kebab-case.
- **Workflow Walden:** Requirements → Design → Tasks → Execute; ogni fase richiede approvazione esplicita.
- **Branch principale:** `main`.
- **Commit:** messaggi in italiano o inglese, descrittivi del cambiamento.

## Sanity Checks

```bash
python scripts/run_verification.py
python -m unittest discover -s tests -v
```

## Key Files

| File | Ruolo |
| --- | --- |
| `data/100cose.json` | **Fonte canonica** — array `Fare` con 100 voci (`id`, `testo`, `categoria`) |
| `data/100 cose da fare  - Sheet1.csv` | Esportazione tabellare (Google Sheets) |
| `data/100cose.txt` | Versione testuale / poster |
| `.walden/constitution.md` | Contesto stabile del progetto (questo file) |
| `.walden/lessons.md` | Lezioni apprese dal workflow Walden |
| `.walden/specs/` | Feature specs (requirements, design, tasks) |
| `README.md` | Guida rapida per iniziare con Walden |

### Categorie note (da `100cose.json`)

Avventura, Conoscenza, Corpo, Creatività, Crescita personale, Natura, Relazioni, Spirito.

## Hard Rules

- I dati in `data/100cose.json` devono restare **100 voci** con `id` da 1 a 100 finché non si decide diversamente in una feature spec approvata.
- Non avviare implementazione applicativa senza `requirements.md`, `design.md` e `tasks.md` approvati per la feature.
- Usare il CLI Walden (`walden validate`, `walden review approve`, ecc.) per transizioni di stato deterministiche — non editare manualmente i frontmatter di approvazione.
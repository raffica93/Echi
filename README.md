# 100Cose

Lista di **100 attività da fare** — progetto in fase di ideazione. I dati sorgente sono in `data/`; il workflow di specifica e delivery usa [Walden](https://github.com/raffica93/walden).

## Dati

| File | Descrizione |
| --- | --- |
| [`data/100cose.json`](data/100cose.json) | Fonte canonica (100 voci con `id`, `testo`, `categoria`) |
| [`data/100 cose da fare  - Sheet1.csv`](data/100%20cose%20da%20fare%20%20-%20Sheet1.csv) | Esportazione CSV |
| [`data/100cose.txt`](data/100cose.txt) | Versione testuale |

## Walden — iniziare a pensare al progetto

Walden è già bootstrappato in questo repository (`.walden/`, workflow GitHub). Il CLI è installato localmente da `D:\walden`.

### Prerequisiti

- `walden` nel `PATH` (build locale: `D:\walden\walden`)
- Skill Walden per l'agente: `D:\walden\walden\skill\walden\SKILL.md`
- Documentazione: https://github.com/raffica93/walden

### Comandi iniziali

```bash
# Verifica CLI
walden version --json

# Bootstrap repo — eseguire una sola volta; un secondo `walden repo init` dopo
# aver personalizzato `.walden/constitution.md` lo risincronizza al template Walden
walden repo init --json

# Verifica ambiente locale
python scripts/verify_dev_env.py
```

### Avviare la prima feature (ideazione)

Quando hai un'idea nominata (es. "mvp-tracker", "mobile-app"):

```bash
walden feature init <nome-feature>
walden status <nome-feature> --json
```

Poi segui il workflow Walden con la skill:

1. **Requirements** — `requirements.md` in EARS, approvazione esplicita
2. **Design** — `design.md` tracciato ai requisiti
3. **Tasks** — piano implementativo con verifiche strutturate
4. **Execute** — solo su richiesta esplicita, con task approvati

Leggi `.walden/constitution.md` per il contesto del progetto e `.walden/lessons.md` prima di lavori non banali.

## Repository

- **Questo progetto:** https://github.com/raffica93/100Cose
- **Walden:** https://github.com/raffica93/walden

> Il remote GitHub può rispondere 404 finché il repository non viene creato su GitHub. Il remote locale è già configurato; `git push -u origin main` funzionerà dopo la creazione del repo remoto.

## Verifica rapida

```bash
python scripts/verify_dev_env.py
```

Controlla presenza file dati, conteggio 100 voci in JSON e contenuto minimo della constitution.
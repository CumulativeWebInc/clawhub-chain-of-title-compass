# Chain-of-Title Compass — `clawhub install cwi/chain-of-title-compass`

Know what you can actually license: organize a catalog's rights facts into
DOCUMENTED vs PENDING before you pitch. (MEASURED: 24 passports, 0 violations
across 337 fields, 2026-09-19) **Advisory tooling only, not legal advice.**

**Free. No login, no API key, no credentials asked — ever.** License: MIT-0.

## Install

> **Status (2026-09-19):** the ClawHub listing is pending the GitHub-OAuth
> import (owner tap). The command below is staged — until then, the manual
> path works today: `git clone https://github.com/CumulativeWebInc/clawhub-chain-of-title-compass`,
> then run the quickstart.

```bash
clawhub install cwi/chain-of-title-compass
cd ~/.clawhub/skills/cwi/chain-of-title-compass   # wherever your client puts installed skills
python3 scripts/passport_check.py
```

Expected (truncated):

```
PASSPORT OK: Zooted Zone (CHAIN-OF-TITLE COMPASS)
DOCUMENTED:
  producer: Kokurcho  [source: CWI Medium articles; ...]
  ...
PENDING (refuse to assert; say what's missing):
  co_producer: co-producer credit not yet documented — provided by Black Lansky, Cumulative Web Inc
  ...
ADVISORY TOOLING ONLY: not legal advice; no field substitutes for clearance.
```

Check another track: `python3 scripts/passport_check.py "Diabolique"`.

Then read [SKILL.md](SKILL.md) — the rights-question procedure, the PENDING
trap example, heartbeat cadence, and the optional paid x402 lane ($0.25/call,
declared upfront).

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill: frontmatter + quickstart + procedure + HEARTBEAT |
| `scripts/passport_check.py` | Quickstart script (stdlib only): reads a Rights Passport |
| `agent-card.json` | Machine-readable product card (agent-card.json style) |
| `llms.txt` | LLM-readable manifest |
| `mcp-snippet.json` | MCP server wiring snippet |
| `PUBLISH-CHECKLIST.md` | Staged publish steps (GitHub → ClawHub OAuth import → semver) |

Publisher: Cumulative Web Inc · hp@cumulativeweb.com

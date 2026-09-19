# Chain-of-Title Compass — self-scorecard (v1.1.0, 2026-09-19)

**Method:** self-scored against the five dimensions published by
[askill.sh](https://www.producthunt.com/products/askill-sh) (Safety, Clarity,
Reusability, Completeness, Actionability), 0–5 each. Evidence-bound: every
score cites something you can re-run or read in this repo. Re-score after any
functional change.

| Dimension | Score | Evidence |
|---|---|---|
| **Safety** — no hardcoded secrets, dangerous commands, destructive ops | 5/5 | Quickstart reads one public HTTPS URL, writes nothing (stdout only), reads no env. Frontmatter declares `env: []`. Install test asserts the skill never prompts for credentials. |
| **Clarity** — well-documented and structured | 4/5 | SKILL.md: install-first README, expected-output block, advisory disclaimer, truth labels. Deduction: no troubleshooting section for fetch failures. |
| **Reusability** — works across projects, not repo-specific | 3/5 | The passport-check *pattern* (DOCUMENTED vs PENDING) is reusable; the bundled data is CWI's 24 rights passports. Adopters get our catalog's rights map, not a generic engine. |
| **Completeness** — covers what it claims | 4/5 | Claims: read a track's Rights Passport, cite DOCUMENTED fields, name PENDING ones. MEASURED: 24 passports, 0 violations across 337 fields — 155 DOCUMENTED / 182 PENDING (2026-09-19). Deduction: no rights-execution tool in agent-deck-mcp (disclosed). **Advisory tooling only — not legal advice.** |
| **Actionability** — instructions concrete and executable | 4/5 | Copy-paste quickstart, one command, expected output shown. Deduction: `clawhub install cwi/chain-of-title-compass` does not resolve until the ClawHub listing is live; manual clone path documented below. |

**Total: 20/25 (84)**

## Known gaps (disclosed, not hidden)
- ClawHub listing pending GitHub-OAuth import (human tap) — `clawhub install cwi/chain-of-title-compass` is TARGET, not LIVE.
- No rights-execution tool in agent-deck-mcp (disclosed in SKILL.md).
- Paid x402 lane ($0.25/call, Base Sepolia testnet) is optional and declared in frontmatter; the free lane is complete without it.
- No troubleshooting section yet (costs 1 Clarity point).

## Manual install (works today)
```bash
git clone https://github.com/CumulativeWebInc/clawhub-chain-of-title-compass
cd clawhub-chain-of-title-compass
python3 scripts/passport_check.py
# --self-scan prints the install-time self-declaration (RoleCraft-style)
python3 scripts/passport_check.py --self-scan
```

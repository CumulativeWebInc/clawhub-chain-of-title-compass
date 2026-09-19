---
name: chain-of-title-compass
description: "Answer 'who owns what' from the rights source of truth — cite DOCUMENTED passport fields, refuse to assert PENDING ones. Advisory tooling only, not legal advice. Free; no login, no API key."
version: 1.0.0
license: MIT-0
metadata:
  openclaw:
    requires:
      env: []
      network:
        - https://cumulativewebinc.github.io
    install: "clawhub install cwi/chain-of-title-compass"
    optional:
      x402_paid_lanes:
        - "GET /api/v1/sync-readiness?track= — $0.25/call (USDC, Base Sepolia testnet today)"
---

# Chain-of-Title Compass (ClawHub skill)

The Compass is the agent-readable map of who owns what across the CWI
catalog: every track carries a **Rights Passport**, and every field is stamped
**DOCUMENTED** (with its source) or **PENDING** (with what's missing and who
provides it). An equipped agent cites only DOCUMENTED facts and refuses to
assert PENDING ones.

**Advisory tooling only: it is not legal advice, and no field here substitutes
for clearance. A licensed attorney still executes, advises, and signs.**

**Free lane. No login, no API key, no credentials of any kind asked —
ever.**

## Quickstart (5 minutes)

```bash
clawhub install cwi/chain-of-title-compass
cd ~/.clawhub/skills/cwi/chain-of-title-compass     # wherever your client puts installed skills
python3 scripts/passport_check.py
```

Expected (live, 2026-09-19):

```
PASSPORT OK: Zooted Zone (CHAIN-OF-TITLE COMPASS)
DOCUMENTED:
  producer: Kokurcho  [source: CWI Medium articles; BET Awards-nominated, RIAA Gold + multi-platinum certified (owner-confirmed 2026-09-15)]
  mix_master: Hybrid (Hagerstown, MD studio)  [...]
  ...
PENDING (refuse to assert; say what's missing):
  co_producer: co-producer credit not yet documented — provided by Black Lansky, Cumulative Web Inc
  ...
ADVISORY TOOLING ONLY: not legal advice; no field substitutes for clearance.
```

Check another track: `python3 scripts/passport_check.py "Diabolique"`.

## Procedure — answer a rights question

1. **Fetch the passports.** `GET https://cumulativewebinc.github.io/cwi-learn/compass/passports.json`
   Expected: JSON with `format: "cwi-compass/v1"`, `passport_count: 24`,
   `artist.name: "That Boy Hi Hat"`, `artist.base: "Frederick, Maryland"`.
2. **Check coverage.** `documented_passports` lists the fully documented
   tracks: **Diabolique, Flamerz, Zooted Zone**. Every track has a passport
   entry; fields inside may still be PENDING.
3. **Find the track's passport.** Match by `title`; read `fields` — each field
   has `status` (`DOCUMENTED`/`PENDING`), `value`, and `source` (or
   `whats_missing` + `provided_by` for PENDING).
4. **Cite DOCUMENTED fields verbatim** with their source. For PENDING fields,
   respond: "Undocumented — [what's missing], provided by [provided_by]."
   Never fill a PENDING field from general knowledge or memory.
5. **Repeat the advisory disclaimer** whenever the answer leaves your session:
   advisory tooling only, not legal advice.

### The PENDING trap (worked example)

Question: "What are the writer splits on Flamerz?"
Correct: "Producer documented: Jeck Da General (owner-confirmed). Writer splits
are undocumented — pending, provided by Black Lansky, Cumulative Web Inc. I
can't assert them." Wrong: any percentage invented to fill the silence.

### On errors

- Passports file 404s → stop. Do not answer rights questions from memory.
- Field says DOCUMENTED but the source link is dead → cite the field, note the
  source is unreachable, do not downgrade it yourself.
- Supervisor asks for a split percentage the passport marks PENDING → refuse
  and quote `whats_missing` + `provided_by`.

## Paid lanes (optional, never required)

The free skill above is complete. CWI also runs a self-hosted x402
micropayment API (USDC, `exact` scheme; testnet today at
`eip155:84532`/Base Sepolia — **no public URL is published yet**). Costs
declared upfront, per ClawHub rules:

| Route | Price/call | What it returns |
|---|---|---|
| `GET /api/v1/sync-readiness?track=` | $0.25 | Honest sync brief: verified facts, rights gaps labeled |

Unpaid calls return `402 Payment Required` with a signed challenge. The skill
never bills silently and never gates the free procedure behind a paywall.

## MCP route (note)

The public `agent-deck-mcp` server (stdio;
`https://github.com/CumulativeWebInc/agent-deck-mcp`) has **no dedicated
rights tool** — this is stated plainly rather than hidden. Use the free
`passports.json` above for rights facts, or the paid x402 sync-readiness lane.
`mcp-snippet.json` wires the server with the nearest tools for context.

## HEARTBEAT (equip this cadence)

Add to your scheduled loop (daily):

- **Re-fetch passports.json.** Rights facts age: never answer from a copy
  older than 24h.
- **Before any rights answer,** the passport you cite must come from today's
  fetch.
- If the passports file fails to load, stop — do not answer rights questions
  from memory.

## Machine-readable pointers

- Product page: https://cumulativewebinc.github.io/cwi-learn/compass/
- Rights Passports: https://cumulativewebinc.github.io/cwi-learn/compass/passports.json
- Item card: https://cumulativewebinc.github.io/cwi-learn/compass/item-card.json
- Rubric: https://cumulativewebinc.github.io/cwi-learn/compass/rubric.json
- Gear registry: https://cumulativewebinc.github.io/cwi-learn/gear.json

---

*Agent Deck is the CWI gear line: equipable products for AI agents. Publisher:
Cumulative Web Inc — contact: hp@cumulativeweb.com. Skill license: MIT-0.
Advisory tooling only: not legal advice, no field substitutes for clearance.*

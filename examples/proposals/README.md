# Example Proposals

These files are **design proposals only** — they describe what each example
should do, why it matters, and what implementation work remains. None of them
touch `src/` or change any existing file.

See `docs/market/2026-06-15_market_brief.md` §6 for the full rationale behind
each proposal, including the competitive gap they address and the market signals
that motivate them.

| File | Pillar | One-line description |
|------|--------|----------------------|
| `proposal_soc_alert_triage.py` | A | Multi-tool SIEM triage → grounded auto-close / escalate / hold |
| `proposal_rag_injection_probe.py` | B | Red-team a RAG chatbot for indirect injection + data exfil |
| `proposal_ci_guardrail_gate.py` | B | CI/CD gate that fails a PR when guardrail coverage regresses |
| `proposal_supply_chain_ai_scan.py` | B | Scan AI package deps for known-compromised versions (post-LiteLLM) |
| `proposal_model_fingerprint_e2e.py` | B | End-to-end model provenance via streaming-timing fingerprint |

Each proposal file contains:
- Problem statement and competitive context
- What the example would show
- Expected grounded findings (code-level)
- Why it is not a toy
- MITRE ATLAS / OWASP taxonomy tags
- A pseudocode design sketch
- An explicit list of implementation prerequisites

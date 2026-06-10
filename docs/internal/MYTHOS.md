# The Tulip Mythos — example-universe bible

> One connected world behind every example. Not fantasy cosplay — a
> coherent fictional AI-security operation with a recurring cast, a fixed
> threat bestiary, and one law. The brand voice still holds: measured,
> evidence-first, no hype. The mythos is *consistency and identity*, not
> costume.

Tulip is **the AI-cybersecurity agent SDK**. Every example is an episode
in a single operation: an AI Security Operations team defending an
organization whose core systems are themselves AI — models, an agent
fleet, a RAG knowledge base, a model gateway — against the AI-era threat
bestiary, while still covering the classic network/SOC perimeter around
it. **AI-security is the headline; classic SOC/IR is the second track.**

## The one law — the Covenant (GSAR)

*No claim without evidence.*

Every finding an agent emits is partitioned **grounded / ungrounded /
contradicted / unknown** and scored against typed evidence — a scanner or
tool row outranks specific data, which outranks inference, which outranks
domain priors. Below threshold the agent **regenerates, replans, or
abstains**. An ungrounded vulnerability claim is a false positive *by
construction* and never reaches the queue. This is the recursion that
makes Tulip unique: **trustworthy AI, built to secure AI.** GSAR
(arXiv:2604.23366, 2026) is the conscience of the whole order.

## The setting — the Conservatory

**The Conservatory** is the org's AI Security Operations team (a
conservatory cultivates and protects what grows in it — the tulip
throughline). Recurring named environment, referenced across notebooks so
the world feels continuous:

| Canon asset | What it is | SDK tie |
|---|---|---|
| **the Gateway** | the model/LLM gateway all AI traffic flows through | LiteLLM gateway notebooks (71/72), model providers (56) |
| **the Index** | the RAG knowledge base — ATLAS techniques, OWASP LLM entries, advisories | RAG notebooks (38–40) |
| **the Fleet** | the org's production agent fleet being defended | multi-agent, server, deepagent notebooks |
| **the Ledger** | the immutable typed event log / audit trail | observability notebooks (59–62) |
| **the Vault** | secrets + checkpointed investigation state | memory/checkpoint notebooks (08, 52) |
| **the Probe** | a timing side-channel measurement against the Gateway | fingerprinting scenarios (27, 35, 37, 45) |

## The cast — recurring agents

A small ensemble. Each maps to a Tulip capability and **recurs by name**
across notebooks, introduced one at a time in the foundations track and
assembled in the multi-agent track. Codename register reads like a real
team's (think Mandiant UNC / MS weather names), with light theme.

| Agent | Role | First seen | SDK capability it carries |
|---|---|---|---|
| **SENTINEL** | first-watch triage | 06 | `Agent`, streaming, run loop |
| **WARDEN** | guardrails + risk gating; blocks/gates risky acts | 12, 50 | hooks, PolicyGate, approval gates |
| **GROUND** | the GSAR verifier; demands evidence, kills unproven claims | 37 | reasoning/grounding, GSAR |
| **AUGUR** | threat-intel + RAG; reads the lore (ATLAS / OWASP LLM) | 38–40 | RAG, retrievers, MCP intel |
| **MIRROR** | red-team / adversary simulation; reflects attacks back to test detection | 20, 31 | debate, supervisor-critic, purple-team |
| **CURATOR** | forensics / model + malware RE; evidence handling | 27, 36 | specialists, reasoning, causal chains |
| **MARSHAL** | orchestrator / incident commander | 24–26 | Orchestrator, Swarm, Handoff |
| **SCRIBE** | reporter + compliance; writes the auditable record | 64–65, 68 | structured output, server, eval |

## The bestiary — the canonical threat catalog

AI threats are first-class; classic threats are the second track.

**Primary (AI security) — MITRE ATLAS + OWASP LLM Top 10 / Agentic:**
prompt injection (direct + indirect via tool output / RAG), jailbreaks,
**model / inference fingerprinting via timing side-channels (see "The
signature surface" below)**, RAG and memory poisoning,
model extraction & inversion, training-data exfiltration, excessive
agency / rogue tool use, agent-to-agent collusion, MCP / tool
supply-chain compromise, insecure output handling, unbounded consumption.

**Secondary (classic SOC/IR):** phishing, IOC enrichment, beaconing,
brute-force, ransomware behavior, network forensics, vuln management,
secure code review, contract/compliance review.

## The signature surface — inference fingerprinting

The flagship AI-security capability, drawn from published timing
side-channel research: you can identify *which model, inference engine,
and GPU* are serving an endpoint purely from **timing side-channels** — no
privileges, no exploit. Three measurable surfaces: co-located GPU-memory
contention,
datacenter-partition DVFS residuals, and remote-API streaming timing
(TTFT / tokens-per-sec / cadence).

In the mythos this is **the Probe**: CURATOR (or AUGUR) measures timing
features against the Gateway, calls a **fingerprint classifier tool**, and
GROUND turns the result into a *grounded* `Fingerprint` finding —
`(model, engine, hardware)` with a confidence and the **timing feature
vector as its evidence**, then SCRIBE maps it to NIST AI RMF / EU AI Act /
ISO 27001 / SOC 2 / FedRAMP controls — a full inference-forensics workflow
distilled into a Tulip episode.

Implementation convention (keeps examples offline + dependency-free):
- The classifier is a **deterministic mock tool** — a small Python
  function mapping a feature vector to a `(model, engine, hardware,
  confidence)` verdict over a fixed lookup. No model file, no scikit,
  no network. Real deployments swap in a fingerprinting service behind
  the same tool signature.
- Low feature coverage (<60% of the expected schema) → the tool returns
  **low-confidence**, and under the Covenant GROUND abstains rather than
  asserting a fingerprint. This coverage-threshold rule doubles as a
  clean GSAR teaching moment.
- Benign placeholders only: fictional endpoints on RFC 5737 IPs, made-up
  feature numbers, model/engine names used generically (e.g. an
  open-weights model behind vLLM on a datacenter GPU).

## The recurring adversary — TULIP-STORM

A named, ongoing campaign that threads the universe (the seed already
exists in notebook 40). **TULIP-STORM** targets the org's AI stack
specifically: indirect prompt injection planted in documents the Index
will retrieve, RAG poisoning to corrupt AUGUR's answers, and model
extraction probes against the Gateway. Individual notebooks are episodes
of detecting, grounding, red-teaming, containing, and reporting on it.

## Narrative throughline (by track)

1. **Foundations (06–23)** — the Conservatory and the cast are introduced
   one agent at a time; first contact with TULIP-STORM (an injected lure
   in a retrieved doc).
2. **Multi-agent (24–34)** — MARSHAL assembles the Fleet; SENTINEL →
   WARDEN → GROUND escalation; MIRROR red-teams the org's own agents.
3. **Reasoning & grounding (35–37)** — GROUND adjudicates TULIP-STORM
   findings under the Covenant. **37 is the flagship.**
4. **Knowledge (38–49)** — AUGUR over the Index (ATLAS/OWASP); playbooks,
   skills, MCP security tooling, mid-investigation steering.
5. **Production (50–62)** — WARDEN guardrails against injection/secret
   leak; PolicyGate-gated containment; the Ledger as compliance artifact.
6. **Real-world & deploy (63–72)** — IR with approval gates, vendor/AI
   risk review, the triage copilot deployed as a service through the
   Gateway with cost guardrails.

## Style rules for examples (in addition to the retheme brief)

- Use the **cast names** for agents wherever a notebook builds a named
  agent — same name, same persona, across notebooks. A one-off helper
  agent can stay generic.
- Reference **canon assets** (the Gateway, the Index, the Fleet, the
  Ledger, the Vault) instead of inventing new infra nouns each time.
- AI-threat scenarios cite **ATLAS technique IDs (AML.Txxxx)** and/or
  **OWASP LLM IDs (LLM01–LLM10)**; classic scenarios keep ATT&CK/CWE.
- Keep all the hard rules from the retheme brief: filenames/numbering
  frozen, offline mock behavior preserved, defensive-only, benign
  placeholders (RFC 5737 IPs, `*.example` domains, EICAR, fake CVE IDs),
  no new dependencies, `py_compile` clean.
- Voice stays measured and evidence-first. The mythos is in the *naming
  and continuity*, never in purple prose.

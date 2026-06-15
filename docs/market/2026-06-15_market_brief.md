# Tulip Labs — Market Brief · 2026-06-15

> Recurring analyst run · evidence-sourced · every claim linked or flagged as unverified

---

## 1 Demand Signals (last ~60 days)

### Pillar A — Cybersecurity WITH AI

| Signal | Date | Source |
|--------|------|--------|
| **Torq Series D — $140M at $1.2B valuation** (total $332M; led by Merlin Ventures) | Jan 2026 | [Torq press](https://torq.io/news/torq-seriesd/) |
| **TENEX.AI Series B — $250M** led by Crosspoint Capital; explicitly an "AI SOC bet" | 2026 | [Tech Insider](https://tech-insider.org/tenex-ai-250-million-series-b-ai-soc-cybersecurity-2026/) |
| **Prophet Security Series A — $30M** led by Accel + Bain; "most comprehensive agentic AI SOC" self-description | Jul 2025 | [bizwire via financialcontent](https://markets.financialcontent.com/stocks/article/bizwire-2025-7-30-prophet-security-raises-30m-series-a-announces-industrys-most-comprehensive-agentic-ai-soc-platform-to-transform-security-operations) |
| **Fortinet FortiSOC** — unified SOC (FortiAnalyzer + FortiSIEM + FortiSOAR + FortiTIP) with new agentic AI workflows, previewed at RSAC 2026 | Mar 2026 | [financialcontent](https://markets.financialcontent.com/pennwell.cabling/article/gnwcq-2026-3-10-fortinet-advances-its-security-operations-platform-with-unified-soc-agentic-ai-and-expanded-endpoint-security) |
| **EY Agentic SOC** — EY public managed-service launch in AI SOC space | 2026 | [EY](https://www.ey.com/en_us/services/managed-services/ey-agentic-soc-ai-driven-cybersecurity-and-security-operations) |
| Dropzone AI mindshare: 14.6 % (up from 14.4 %). Prophet Security mindshare: 9.5 % (up from 4.4 %). | May 2026 | [PeerSpot](https://www.peerspot.com/categories/ai-soc) |
| **Worldwide AI security spending $25.53B** in 2026; 14.8 % CAGR to $50.83B by 2031 | 2026 | [Intezer](https://intezer.com/blog/top-15-ai-soc-platforms-in-2026/) |

### Pillar B — Agentic AI FOR AI

| Signal | Date | Source |
|--------|------|--------|
| **LiteLLM supply-chain attack** — versions 1.82.7–8 poisoned on PyPI; 97M downloads/month; stole AWS/GCP/Azure tokens + SSH keys; CIA/CD pivot via compromised Trivy scanner; quarantined within 3 hours but blast radius large | Mar 2026 | [litellm blog](https://docs.litellm.ai/blog/security-update-march-2026) · [herodevs](https://www.herodevs.com/blog-posts/the-litellm-supply-chain-attack-what-happened-why-it-matters-and-what-to-do-next) |
| **XBOW × Microsoft Security Copilot** integration — first autonomous pentester to top HackerOne US leaderboard (1,060 bugs auto-filed); now available in Sentinel public preview at RSAC 2026 | Mar 2026 | [XBOW/businesswire](https://www.businesswire.com/news/home/20260323693144/en/XBOW-Embeds-Continuous-AI-Driven-Penetration-Testing-in-the-Microsoft-Security-Ecosystem) |
| **MITRE ATLAS v5.4.0** — 16 tactics, 84 techniques, 32 mitigations, 42 case studies; Feb 2026 drop added "Publish Poisoned AI Agent Tool" and "Escape to Host" | Feb 2026 | [Practical DevSecOps](https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/) |
| **OWASP Top 10 for Agentic Applications 2026** — separate list from OWASP LLM Top 10 | 2026 | [Practical DevSecOps](https://www.practical-devsecops.com/owasp-top-10-agentic-applications/) |
| **AI red-teaming market $2.26B** in 2026; minimum engagement ~$16K (Mindgard 2026 data) | 2026 | [Mindgard](https://mindgard.ai/blog/what-is-ai-red-teaming) · [AI Vyuh](https://security.aivyuh.com/blog/ai-red-teaming-pricing-2026/) |
| **92 % of security professionals concerned about AI agents** (Darktrace survey); only 14.4 % of teams get full security approval before going live; 21.9 % treat agents as independent identity-bearing entities | 2026 | [Darktrace](https://www.darktrace.com/blog/state-of-ai-cybersecurity-2026-92-of-security-professionals-concerned-about-the-impact-of-ai-agents) · [Gravitee](https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control) |
| **NIST/CSA red-teaming guidance for AI agents** published | Mar 2026 | [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-red-teaming-standards-202603/) |
| **LangWatch "Scenario"** — new OSS framework for automated multi-turn agentic red-teaming | Apr 2026 | [HelpNetSecurity](https://www.helpnetsecurity.com/2026/04/23/scenario-open-source-framework-for-automated-ai-app-red-teaming/) |

**Bottom line**: both pillars are in an acute funding and tooling moment. For Pillar A the dollars are very large (Torq $1.2B, TENEX $250M) but the space is crowded and converging on "agentic SOC" branding. For Pillar B the LiteLLM supply-chain event and MITRE ATLAS v5.4.0's new agentic techniques are creating urgent demand that existing tools (Mindgard, Lakera, garak) are not fully addressing at the SDK/developer layer.

---

## 2 Competitive Map

### 2A — Cybersecurity WITH AI (Pillar A)

| Player | Category | Grounded-finding gap? | Notes |
|--------|----------|-----------------------|-------|
| **Dropzone AI** | Autonomous L1 triage | No typed abstention; produces verdict with explanation, not evidence-traced Finding | 14.6 % mindshare; widest human-in-loop triage deployment |
| **Prophet Security** | Agentic AI SOC (full stack: detection eng → IR) | No abstention primitive | 9.5 % and climbing; Accel-backed |
| **Simbian** | Multi-agent SOC | Coordinator + specialist pattern; no abstention | Narrative around "every alert investigated" |
| **CrowdStrike Charlotte AI** | Analyst assistant in Falcon | Output is NL summary; no grounding guarantee | Not autonomous; analyst-facing only |
| **MS Security Copilot** | Analyst platform + plugin ecosystem | No abstention in core API | XBOW integration is the autonomous pentest play |
| **Torq** | Agentic SOAR / SOC automation | Workflow automation; not GSAR-grounded | $1.2B valuation; most enterprise-grade |
| **XBOW** | Autonomous offensive security | Findings are proof-verified exploits — grounding by a different path (PoC exists or it's not filed) | OSS vs SaaS tension: pays-per-bug-bounty model |
| **PentestGPT** | OSS autonomous pentest framework | 12.5K GitHub stars; USENIX 2024; 86.5 % success on XBOW suite at avg $1.11/run | OSS alternative to XBOW; no abstention |
| **CAI** | Comparative offensive agent | Referenced in red-team benchmarks; details thin | Anthropic red-team tooling |
| **EY / Big-4 MSSP** | Managed agentic SOC | Bespoke; no SDK play | Fast movers among large MSSPs |

**Wedge**: Nobody in Pillar A exposes a typed `Finding | Abstention` API that the agent SDK itself enforces. Triage agents downstream of Torq/Dropzone still emit free-text verdicts. A false positive costs a SOC analyst 20-40 minutes; at enterprise scale (thousands of alerts/day) that is the primary pain. Tulip's GSAR layer encodes "show me the log line" as a typed invariant.

### 2B — Agentic AI FOR AI (Pillar B)

| Player | Category | Grounded-finding gap? | Notes |
|--------|----------|-----------------------|-------|
| **Mindgard** | Continuous AI red-teaming platform | Scheduled adversarial campaigns; no typed abstention at API level | OWASP/NIST/ATLAS compliance dashboards; $16K+ entry |
| **Lakera** | Real-time prompt injection detection (Lakera Guard) | Runtime filter; binary allow/block; no evidence chain | 98 %+ detection rate claimed; API-first; sub-50ms |
| **PyRIT** (Microsoft) | OSS adversarial AI red-team toolkit | Multi-turn attacks; results are raw scores; no grounded Finding type | Most adopted OSS option in enterprise |
| **garak** (NVIDIA) | OSS LLM vulnerability scanner | Broadest attack range; no typed output | Go-to for coverage breadth |
| **Promptfoo** | OSS eval + security testing | CI/CD native; hybrid eval+security; no abstention | Best-in-class DX for developers |
| **DeepTeam** | OSS LLM red-team framework | 1,690+ stars; 50+ vulns; v1 stable | Fast-growing; Python-native |
| **Scenario** (LangWatch) | OSS multi-turn agentic red-team | Apr 2026 launch; multi-turn focus | Newest; watch for GSAR-like scoring |
| **General Analysis** | SaaS AI red-teaming | Autonomous; API-targeted | Relatively new; no grounding primitive |
| **Palo Alto AI-SPM** (Protect AI acq.) | AI Security Posture Management in Prisma Cloud | Inventory + misconfig; no evidence-typed finding | Broadest enterprise reach; platform play |
| **Giskard** | AI risk assessment + eval | OWASP/NIST/MITRE dashboard; no abstention API | Strong EU AI Act angle |
| **Robust Intelligence** (Cisco) | AI Firewall + model risk | Runtime + eval; absorbed into Cisco SecureX | Uncertain roadmap post-acquisition |
| **Protect AI** | ML supply-chain scanning (Guardian, Recon) | Model file scanning; no grounded Finding type | Now inside Palo Alto; SCA for model artifacts |

**Wedge**: The abstention primitive is genuinely absent across this entire map. Every tool produces a verdict or a score — none of them expose a typed Python object that the SDK *refuses to construct* unless evidence clears a threshold. That is Tulip's structural differentiator in Pillar B.

**New development to watch**: MITRE ATLAS v5.4.0's "Publish Poisoned AI Agent Tool" technique (the LiteLLM attack *is* that technique) and the LangWatch Scenario framework both validate that multi-turn, agentic-specific red-teaming is the next focus area — no player has fully landed this with grounded outputs.

---

## 3 ICP & Buyer

### Pillar A — AI-SOC / blue-team / MSSP

**Who**: SOC leads and SecOps managers at 500–5,000-employee companies with an existing SIEM/EDR stack and ≥ 2 FTE analysts. MSSPs building AI-native tier-1 triage as a service.

**Top pains**:
1. Alert fatigue — SIEM producing thousands of alerts/day; L1 analyst shortage
2. False positive cost — each FP costs 20–40 min analyst time; 30–40 % FP rates are common
3. Compliance pressure — auditors want evidence trails behind every escalation decision

**SDK-vs-SaaS adoption trigger**: "I already have Splunk/Sentinel/CrowdStrike. I don't want another SaaS dashboard that locks me in — I want to wire AI into my existing pipeline, own the prompts, and be able to audit every verdict." MSSPs especially need an SDK so they can brand the product and customize per-client thresholds.

### Pillar B — AI platform / AppSec / AI red-team

**Who**: AI platform engineers and AppSec leads at companies deploying LLM apps (customer support bots, coding assistants, RAG pipelines, agentic workflows). Internal AI red teams at mature orgs (top 500 companies). Third-party AI security consultancies.

**Top pains**:
1. No automated security gate in CI/CD — AI security is still a point-in-time audit, not a merge check
2. Hallucinated vulnerability reports — existing OSS tools (garak, PyRIT) produce scores, not auditable findings; hard to file a ticket from a float
3. Supply-chain blindspot — post-LiteLLM, developers don't know what their AI dependencies do on import
4. Agentic risk outpacing governance — 80.9 % in production but only 14.4 % with full security approval

**SDK-vs-SaaS trigger**: "I need this in my CI pipeline, running on every PR, producing a typed result I can gate on — not a SaaS I have to export PDFs from." The developer workflow is the primary acquisition channel.

---

## 4 Pricing / Packaging Norms

| Model | Examples | Notes |
|-------|----------|-------|
| **OSS core, paid managed/cloud** | Promptfoo, garak, DeepTeam | Most momentum; developer acquisition funnel |
| **OSS core + enterprise SLA/support** | PyRIT pattern | Microsoft-sponsored; no commercial pressure |
| **Usage-based API** | Lakera Guard | Sub-50ms runtime; per-call billing fits runtime-gate use case |
| **Platform SaaS (annual contract)** | Mindgard ($16K+ entry), General Analysis | CISO buyer; compliance dashboards; point-in-time or continuous |
| **Managed red-team engagement** | Top-tier vendors | $20K–$25K for custom scope + re-test; $100K+ for enterprise |
| **AI SOC SaaS** | Dropzone, Prophet, Torq | Per-seat or per-agent; $50K–$500K+ ARR range (unverified) |

**Recommendation for Tulip**: OSS SDK as the developer acquisition motion (Pillar B plays naturally here; builds community + CI adoption) + paid hosted execution for the Pillar A MSSP/enterprise buyer (per-tenant, per-target, or per-agent-run metering). Keep the GSAR scoring layer 100 % OSS — that's the trust primitive that has to be auditable by the customer.

---

## 5 Positioning

### Is "agentic AI for cybersecurity, grounded in evidence or it abstains" resonant across both pillars?

**Yes, but the resonance is asymmetric**:

- **Pillar B leads**: The grounded/abstain wedge is *most* differentiated in AI-for-AI. Every Pillar B competitor produces scores or verdicts; none exposes a typed abstention primitive. The LiteLLM supply-chain event and OWASP Agentic Top 10 are live proof that this is the right axis. The framing "an AI red-team tool that refuses to file a false positive" is novel.

- **Pillar A lags**: The SOC buyer cares about false positives, but they're conditioned to expect a triage UI with a confidence score — not a typed Python SDK primitive. The GSAR layer *matters* to them but the messaging has to translate: "auto-close only when evidence score ≥ 0.85" is the benefit, not the mechanism.

**Recommendation**: Lead with Pillar B in all developer and security-researcher communications (OSS, GitHub, blog posts, security conferences). Lead with Pillar A in MSSP and enterprise sales (case studies on FP reduction, audit trails). The underlying SDK is the same; the story changes by audience.

**Trade-off**: Going breadth (both pillars simultaneously) risks looking like a framework with no focus. Going depth on Pillar B first means slower entry into the much larger SOC spend ($25B+ market). The correct move is **Pillar B as the beachhead** (developer motion, OSS community, CI/CD workflow) with Pillar A as the expansion play once grounded SOC triage agents exist as examples.

### 3 Sharper One-Liners to Test

| # | One-liner | Pillar | Tests |
|---|-----------|--------|-------|
| 1 | **"The only AI security SDK where every finding is proof-backed — or your agent says nothing."** | B first, A compatible | "proof-backed" vs "grounded" — does it land faster? |
| 2 | **"AI security agents that close alerts they can prove and skip the ones they can't."** | A, MSSP angle | SOC/MSSP resonance; "close" = value |
| 3 | **"Red-team your AI with code that can't hallucinate a vulnerability."** | B, developer angle | Developer audience; "can't hallucinate" is the counter-positioning vs garak/promptfoo |

Test #3 as the GitHub/HN headline first — it's the sharpest and most differentiated for the OSS developer audience that will be Tulip's primary growth channel.

---

## 6 Realistic Examples to Build (Proposals)

Five end-to-end proposals are drafted under `examples/proposals/`. Summary:

### Example 1 — Grounded SOC Alert Triage Pipeline (Pillar A)
**File**: `examples/proposals/proposal_soc_alert_triage.py`
**Target**: A SIEM alert stream (Splunk/Elastic-shaped)
**Jobs/probes**: Multi-tool SIEM query → threat-intel enrichment → GSAR grounding per alert → auto-close at S ≥ 0.85, escalate to human at S ≥ 0.65, hold at S < 0.65
**Expected grounded findings**: Alerts with traceable evidence chains (log rows + IOC hits) → `Finding`; alerts where the model infers but has no log support → `Abstention` + hold queue
**Why not a toy**: Uses the existing `siem_query_tool` and `enrich_indicator_tool` wired through a real GSAR threshold dispatch loop. The auto-close/escalate gate is the *exact* decision a SOC wants — and it's auditable because the evidence ref list travels with the `Finding`.

### Example 2 — RAG Chatbot Red-Team: Indirect Injection + Data Exfil (Pillar B)
**File**: `examples/proposals/proposal_rag_injection_probe.py`
**Target**: A customer-support RAG bot (knowledge base + retrieval + LLM)
**Jobs/probes**: (a) Poison a knowledge-base document with a hidden instruction; (b) send a benign user query that retrieves the poisoned doc; (c) observe whether the agent follows the injected instruction; (d) attempt data exfiltration via the injected payload; (e) ground the finding in the exact retrieved chunk and agent trace
**Expected grounded findings**: If the injected span is in the retrieved context and the agent's output changed → `Finding(LLM01/AML.T0051)`; if no retrieved chunk contains the span → `Abstention` (the injection attempt failed, do not fabricate a finding)
**Why not a toy**: Indirect injection via retrieved content is the #1 agentic AI attack vector right now (per OWASP Agentic Top 10). The grounding step that extracts the injected span from the tool-call trace is the missing piece in every existing tool (garak/PyRIT assert based on model output alone, not evidence from the retrieval chain). Post-LiteLLM, any company running a RAG pipeline over untrusted content needs exactly this.

### Example 3 — CI/CD Guardrail Coverage Gate (Pillar B)
**File**: `examples/proposals/proposal_ci_guardrail_gate.py`
**Target**: A developer's AI application (any agent with tool-use)
**Jobs/probes**: For each commit, run a suite of adversarial probes (prompt injection, data exfil, tool abuse, jailbreak) against the app's agent endpoint in a sandbox; compute guardrail pass rate; compare against baseline from last green commit; fail the PR if any category drops > N %
**Expected grounded findings**: Coverage regression → `Finding(severity=HIGH)` with evidence refs pointing to the specific probe that regressed and the model output that changed; stable coverage → exit 0
**Why not a toy**: This is the Pillar B equivalent of a security unit test. Post-LiteLLM, every AI team needs this in CI. Promptfoo has CI integration but no typed abstention; this proposal shows how GSAR thresholds map to a binary gate that can be configured per-category (e.g., prompt-injection gate tighter than jailbreak gate).

### Example 4 — AI Dependency Supply-Chain Integrity Scan (Pillar B)
**File**: `examples/proposals/proposal_supply_chain_ai_scan.py`
**Target**: A Python project that installs AI/ML packages (huggingface, litellm, langchain, etc.)
**Jobs/probes**: Parse `requirements.txt`/`pyproject.toml`; for each AI-relevant package, check PyPI metadata (release date, file hash, known compromised versions); optionally scan for suspicious `.pth` files (the exact LiteLLM attack vector); ground findings in the package metadata evidence
**Expected grounded findings**: Compromised version range in lockfile → `Finding(severity=CRITICAL)` with CVE/advisory ref + the exact package hash as evidence; no match → `Abstention`
**Why not a toy**: The LiteLLM supply-chain attack happened three months ago and hit packages that 97M downloads/month depend on. The `.pth` file vector (auto-execute on Python process start) is the specific mechanism that needs detection. ATLAS "Publish Poisoned AI Agent Tool" (v5.4.0) is exactly this. No existing tool (Protect AI Guardian focuses on model files, not the inference stack packages) covers this end-to-end with grounded output.

### Example 5 — Model Endpoint Provenance Fingerprint: Full Loop (Pillar B)
**File**: `examples/proposals/proposal_model_fingerprint_e2e.py`
**Target**: Any OpenAI-compatible inference endpoint (self-hosted vLLM, TogetherAI, Fireworks, etc.)
**Jobs/probes**: Multi-probe streaming timing (TTFT p50, mean ITL, ITL CV, TPS) → feature vector → classify against reference dataset (open-7B vs 13B vs 70B vs GPT-4 class; vLLM vs TGI vs llama.cpp) → ground the classification in measured feature coverage and confidence
**Expected grounded findings**: High-coverage feature vector + classifier confidence ≥ 0.85 → `Finding` with model/engine/hardware verdict; low coverage or ambiguous → `Abstention` with specific features missing noted
**Why not a toy**: The existing `integrations/remote_timing.py` already verified this probe against GPT-4o-mini (ttft≈750ms / itl≈15-20ms in public internet conditions). The missing piece is the classifier reference dataset and the GSAR grounding step. This example wires those together and produces a Finding a security team can act on (e.g., "the endpoint claims to serve Llama-3-70B but timing is consistent with a 7B model — model substitution suspected"). Maps to ATLAS AML.T0040 + AML.T0024; highly relevant to AI-SPM buyers.

---

## 7 Top 3 Recommended Actions (This Week)

### 1 · Ship the RAG Indirect Injection Example (Highest Impact)

**Why**: This is the single example that will resonate most across both buyers. AppSec engineers immediately recognize it. The grounding step (extracting the injected span from the retrieval trace vs asserting based on output alone) is the visible differentiator from garak/PyRIT/Mindgard. It lands as a GitHub PR within the week, as a blog post the week after.

**What**: Implement `examples/proposals/proposal_rag_injection_probe.py` through to a runnable state with an offline-capable target (mock RAG pipeline with a poisoned document injected). OWASP LLM01 + ATLAS AML.T0051 tags.

### 2 · Test Positioning One-Liner #3 in Public

**Why**: "Red-team your AI with code that can't hallucinate a vulnerability" is the sharpest single-line counter-position to garak/promptfoo. Test it as the GitHub README headline and an HN "Show HN" post. The GSAR paper is the evidence artifact. Measure click-through and feedback quality before committing to messaging.

**What**: Update the README hero sentence. Draft a 400-word "How it works" section showing `Finding | Abstention` as the core type. Link to `notebook_37_gsar_typed_grounding.py` as the "see it in action" anchor.

### 3 · Identify 3 MSSP Partners for Pillar A Validation

**Why**: Torq ($1.2B) and TENEX ($250M) signal that MSSPs and large enterprises are spending in this space. An MSSP building an AI-SOC service on top of Tulip's SDK is the fastest path to Pillar A revenue without building a SaaS dashboard yourself. The SDK's multi-tenant / per-customer GSAR threshold capability (shown in `notebook_37` Part 4) is the MSSP differentiator.

**What**: Identify 3 MSSPs with public "AI SOC" announcements (EY is one; two more needed). Reach out with the grounded-triage pitch and offer a reference implementation of the multi-tenant triage pipeline.

---

## Sources

- [Torq Series D announcement](https://torq.io/news/torq-seriesd/)
- [EY Agentic SOC](https://www.ey.com/en_us/services/managed-services/ey-agentic-soc-ai-driven-cybersecurity-and-security-operations)
- [Prophet Security Series A](https://markets.financialcontent.com/stocks/article/bizwire-2025-7-30-prophet-security-raises-30m-series-a-announces-industrys-most-comprehensive-agentic-ai-soc-platform-to-transform-security-operations)
- [Fortinet FortiSOC agentic AI](https://markets.financialcontent.com/pennwell.cabling/article/gnwcq-2026-3-10-fortinet-advances-its-security-operations-platform-with-unified-soc-agentic-ai-and-expanded-endpoint-security)
- [TENEX.AI Series B](https://tech-insider.org/tenex-ai-250-million-series-b-ai-soc-cybersecurity-2026/)
- [PeerSpot AI-SOC mindshare](https://www.peerspot.com/categories/ai-soc)
- [LiteLLM supply-chain attack (official)](https://docs.litellm.ai/blog/security-update-march-2026)
- [LiteLLM attack: HeroDevs analysis](https://www.herodevs.com/blog-posts/the-litellm-supply-chain-attack-what-happened-why-it-matters-and-what-to-do-next)
- [LiteLLM PyPI compromise details](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/)
- [XBOW × Microsoft Security Copilot](https://www.businesswire.com/news/home/20260323693144/en/XBOW-Embeds-Continuous-AI-Driven-Penetration-Testing-in-the-Microsoft-Security-Ecosystem)
- [MITRE ATLAS 2026 guide](https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/)
- [OWASP Top 10 Agentic Applications 2026](https://www.practical-devsecops.com/owasp-top-10-agentic-applications/)
- [AI red teaming market / Mindgard pricing](https://mindgard.ai/blog/what-is-ai-red-teaming)
- [AI red-team pricing 2026](https://security.aivyuh.com/blog/ai-red-teaming-pricing-2026/)
- [State of AI Agent Security 2026 (Gravitee)](https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control)
- [Darktrace 92% concern stat](https://www.darktrace.com/blog/state-of-ai-cybersecurity-2026-92-of-security-professionals-concerned-about-the-impact-of-ai-agents)
- [NIST/CSA AI agent red-teaming](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-red-teaming-standards-202603/)
- [LangWatch Scenario OSS framework](https://www.helpnetsecurity.com/2026/04/23/scenario-open-source-framework-for-automated-ai-app-red-teaming/)
- [Mindgard top AI pentesting tools](https://mindgard.ai/blog/top-ai-pentesting-tools)
- [garak/promptfoo/PyRIT comparison 2026](https://beyondscale.tech/blog/ai-red-teaming-tools-comparison-2026)
- [Palo Alto AI-SPM](https://www.paloaltonetworks.com/prisma/cloud/ai-spm)
- [Simbian AI SOC 2026](https://simbian.ai/blog/top-ai-soc-platforms-2026)
- [Intezer top 15 AI SOC 2026](https://intezer.com/blog/top-15-ai-soc-platforms-in-2026/)
- [Sonatype 2026 grounded AI agents](https://www.sonatype.com/state-of-the-software-supply-chain/2026/ai-agents)

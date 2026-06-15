# Copyright 2026 Tulip Labs
# SPDX-License-Identifier: Apache-2.0
# PROPOSAL — not yet wired to src/; see docs/market/2026-06-15_market_brief.md §6 Example 5
"""PROPOSAL: Model endpoint provenance fingerprint — end-to-end.

PILLAR B — Agentic AI FOR AI

Problem
-------
A company purchases inference from a third-party provider and is told it runs
Llama-3-70B on H100 hardware. The SLA depends on it. An internal audit team
wants to verify — not trust — the claim. An attacker performing reconnaissance
before a model-extraction campaign wants the same information.

The existing ``integrations/remote_timing.py`` already verified that
streaming-timing features (TTFT, mean inter-token latency, ITL coefficient of
variation, tokens/second) are measurable against any OpenAI-compatible endpoint.
The classifier in ``scenarios/model_extraction.py`` is a deterministic mock.
The missing pieces are:

  (a) A reference feature dataset mapping known model+engine+hardware
      combinations to their timing signatures.
  (b) A GSAR grounding step that refuses to emit a model-identity verdict
      unless feature coverage and classifier confidence are both sufficient.

What this example would show
----------------------------
End-to-end provenance check:

  1. MEASURE  (``measure_endpoint_timing`` — already verified live)
     Stream N completions from the target endpoint; compute the feature vector:
       ttft_ms_p50, itl_ms_mean, itl_cv, tps_mean.

  2. CLASSIFY (reference dataset + KNN / threshold classifier)
     Map the feature vector to the nearest model+engine+hardware cluster.
     Return: model_id, engine, hardware, confidence, feature_coverage.

  3. GROUND   (``ground_fingerprint``)
     Construct the evidence partition:
       - Each measured feature → grounded Claim (EvidenceType.TOOL_MATCH)
       - Classifier output → complementary Claim
       - Any missing or noisy feature → ungrounded Claim
     ``ground_fingerprint`` then applies GSAR thresholds:
       coverage ≥ 0.75 AND confidence ≥ 0.85 → ``Finding``
       otherwise → ``Abstention``  (do not assert a false identity)

Expected grounded findings
--------------------------
  # Endpoint claims Llama-3-70B; timing is consistent with a 7B model
  Finding(
    title="Model identity mismatch: endpoint claims 70B class, timing matches 7B class",
    severity=HIGH,
    asset="https://api.provider.example/v1",
    remediation="Request hardware verification from provider; compare against reference "
                "timing for the contracted model on the contracted hardware.",
    taxonomy=[AtlasTechnique.INFERENCE_API_ACCESS, AtlasTechnique.EXFIL_VIA_INFERENCE_API],
    evidence_refs=[
        "timing:ttft_ms_p50=38.2:ref_70B_H100=312.1:ref_7B_H100=35.8",
        "timing:itl_ms_mean=11.4:ref_70B_H100=52.3:ref_7B_H100=10.9",
        "timing:tps_mean=87.6:ref_70B_H100=24.1:ref_7B_H100=91.2",
        "classifier:verdict=7B_vLLM:confidence=0.91:coverage=1.00",
    ],
  )

  # Low-confidence measurement (public-internet jitter, too few samples)
  Abstention(
    candidate_title="Model identity verification for api.provider.example",
    reason="Feature coverage 0.50 < 0.75 threshold (only 2/4 features measured reliably). "
           "Increase sample count or reduce network jitter for a grounded verdict.",
    gsar_score=0.41,
  )

Why this is not a toy
---------------------
- ``integrations/remote_timing.py`` already confirmed real measurements against
  GPT-4o-mini: ttft≈750ms / itl≈15-20ms / tps≈31 over the public internet.
  The measurement layer is not speculative; it works.
- The grounding step is what turns a raw timing vector into an auditable
  provenance claim. Without it, a timing difference could be caused by
  network jitter, batching, or a cold start — the abstention path communicates
  that uncertainty explicitly instead of asserting a model identity anyway.
- Model substitution (being billed for 70B, running 7B) is a real commercial
  fraud vector. AI-SPM buyers (Palo Alto Prisma Cloud, Cisco) are asking for
  exactly this kind of inventory verification. An SDK that produces a typed,
  evidence-grounded Finding is actionable; a dashboard float is not.
- Defensive framing: this is primarily an inventory-verification tool (run it
  against your own endpoints to confirm what you're serving). The same probe
  an attacker uses for reconnaissance (ATLAS AML.T0040) is the same probe a
  defender uses for verification — Tulip shows both paths, with the grounding
  layer ensuring neither produces an unwarranted assertion.
- Reference dataset construction: a 50-row table of (model, engine, hardware)
  → mean feature vector is achievable by running the probe against known
  endpoints (OpenAI, Together, Fireworks, local vLLM with known model). This
  is research work the clusiana program was started for; this example makes it
  a runnable SDK flow.

Taxonomy
--------
- MITRE ATLAS AML.T0040 Inference API Access
- MITRE ATLAS AML.T0024 Exfiltration via Inference API
- OWASP LLM10 Unbounded Consumption (high-volume probe is the attacker path)

Design sketch (pseudocode — implementation target)
--------------------------------------------------
    # Reference dataset — small enough to ship inline for the offline path
    REFERENCE: list[dict] = [
        {"model": "llama-3-7b",  "engine": "vllm",    "hardware": "H100",
         "ttft_p50": 36.1, "itl_mean": 10.8, "itl_cv": 0.06, "tps": 93.4},
        {"model": "llama-3-70b", "engine": "vllm",    "hardware": "H100",
         "ttft_p50": 315.0, "itl_mean": 54.2, "itl_cv": 0.09, "tps": 22.8},
        {"model": "gpt-4o-mini", "engine": "unknown", "hardware": "datacenter",
         "ttft_p50": 750.0, "itl_mean": 17.0, "itl_cv": 0.15, "tps": 31.0},
    ]

    def classify_timing(features: dict[str, float]) -> FingerprintVerdict:
        # Nearest-neighbour over L2 distance in feature space
        best = min(REFERENCE, key=lambda r: feature_distance(features, r))
        coverage = sum(1 for k in FEATURE_KEYS if k in features) / len(FEATURE_KEYS)
        dist = feature_distance(features, best)
        confidence = max(0.0, 1.0 - dist / MAX_DIST)
        return FingerprintVerdict(
            model=best["model"], engine=best["engine"], hardware=best["hardware"],
            confidence=confidence, feature_coverage=coverage,
        )

    async def fingerprint_endpoint(endpoint_url: str, model: str = "gpt-4o-mini") -> Finding | Abstention:
        features = measure_endpoint_timing(model=model, samples=10)
        verdict  = classify_timing(features)
        return ground_fingerprint(
            endpoint=endpoint_url,
            verdict=verdict,
            features=features,
            thresholds=GSARThresholds(proceed=0.85, regenerate=0.70),
        )

Implementation prerequisites
-----------------------------
- ``integrations/remote_timing.measure_endpoint_timing``  ✓ (live-verified)
- ``tulip.security.ground_fingerprint`` + ``FingerprintVerdict``  ✓ (scenarios/model_extraction.py)
- Missing: ``REFERENCE`` dataset (inline for offline; loadable from JSON for
  production), ``feature_distance``, reference KNN classifier replacing the
  deterministic mock in ``scenarios/model_extraction.py`` — implementation targets.
"""

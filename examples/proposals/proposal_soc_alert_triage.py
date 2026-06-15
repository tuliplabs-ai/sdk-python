# Copyright 2026 Tulip Labs
# SPDX-License-Identifier: Apache-2.0
# PROPOSAL — not yet wired to src/; see docs/market/2026-06-15_market_brief.md §6 Example 1
"""PROPOSAL: Grounded SOC alert triage pipeline.

PILLAR A — Cybersecurity WITH AI

Problem
-------
A Splunk/Elastic SIEM fires thousands of alerts per day. A tier-1 analyst
reviews each one. The average false-positive rate is 30–40 %; each FP costs
20–40 minutes. AI triage agents today (Dropzone, Simbian, Prophet) output a
verdict — but no typed evidence chain. An analyst cannot tell which verdict is
grounded in a log row and which is a model inference.

What this example would show
----------------------------
A multi-tool agent that processes a SIEM alert batch and dispatches each alert
through:

  1. ``siem_query_tool`` — pull the raw log events behind the alert.
  2. ``enrich_indicator_tool`` — enrich every IOC in those events (IP, hash, domain).
  3. ``ground_finding`` — attempt to construct a typed ``Finding`` from the
     evidence. The GSAR score determines the dispatch tier:

     S ≥ 0.85  →  AUTO-CLOSE  (evidence is conclusive; benign verdict shipped)
     S ≥ 0.65  →  ESCALATE    (grounded enough to be worth an analyst's time)
     S  < 0.65  →  HOLD        (insufficient evidence; agent abstains; audit record kept)

The result per alert is either a typed ``Finding`` (shipped into the queue with
its evidence refs) or an ``Abstention`` (held, with the candidate text and
GSAR score recorded for the on-call to review). There is no path where a
verdict with no supporting log rows reaches the analyst queue.

Why this is not a toy
---------------------
- Uses the already-verified ``siem_query_tool`` (offline sample) and
  ``enrich_indicator_tool`` (offline EICAR / RFC-5737 sample).
- The auto-close / escalate / hold thresholds are the exact business decision a
  SOC manager parameterises. Tulip exposes them as ``GSARThresholds`` — not a
  magic confidence slider.
- The evidence-ref list that travels with each ``Finding`` is what an auditor
  reads to verify the auto-close decision. This is the compliance property.
- Multi-tenant extension: each customer of an MSSP gets their own
  ``GSARThresholds`` instance. The MSSP can promise contractually that nothing
  is auto-closed below the customer's agreed threshold.

Taxonomy
--------
- OWASP LLM09 Misinformation (the false-positive a hallucinated verdict creates)
- OWASP ASI Identity & Privilege Abuse (the alert class this most often catches)
- MITRE ATLAS AML.T0040 (Inference API Access — relevant when alert is an
  AI-system alert)

Design sketch (pseudocode — implementation target)
--------------------------------------------------
    async def triage_alert(alert: SIEMAlert) -> Finding | Abstention:
        events = await siem_query_tool(query=alert.query, window="1h")
        iocs   = extract_iocs(events)
        reps   = await asyncio.gather(*[enrich_indicator_tool(i) for i in iocs])
        partition = build_partition(events, reps)   # maps log rows → Claims
        return ground_finding(
            title=alert.title,
            description=alert.description,
            severity=map_severity(alert.priority),
            asset=alert.host,
            remediation=...,
            partition=partition,
            thresholds=customer_thresholds,   # configurable per MSSP tenant
        )

    async def run_batch(alerts: list[SIEMAlert]) -> TriageReport:
        results = await asyncio.gather(*[triage_alert(a) for a in alerts])
        auto_closed  = [r for r in results if is_finding(r) and r.gsar_score >= 0.85]
        escalated    = [r for r in results if is_finding(r) and r.gsar_score >= 0.65]
        held         = [r for r in results if not is_finding(r)]
        return TriageReport(auto_closed=auto_closed, escalated=escalated, held=held)

Implementation prerequisites
-----------------------------
- ``tulip.security.ground_finding`` + ``GSARThresholds``  ✓ (notebook_37)
- ``siem_query_tool``  ✓ (examples/integrations/siem_query.py)
- ``enrich_indicator_tool``  ✓ (examples/integrations/threat_intel.py)
- Missing: ``extract_iocs``, ``build_partition``, ``SIEMAlert`` schema,
  ``TriageReport`` type — these are the implementation targets.
"""

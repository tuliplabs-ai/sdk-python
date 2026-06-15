# Copyright 2026 Tulip Labs
# SPDX-License-Identifier: Apache-2.0
# PROPOSAL — not yet wired to src/; see docs/market/2026-06-15_market_brief.md §6 Example 3
"""PROPOSAL: CI/CD guardrail coverage gate.

PILLAR B — Agentic AI FOR AI

Problem
-------
AI applications evolve continuously — system prompts change, tool definitions
change, retrieval sources change, model versions are pinned or bumped. Any of
these changes can silently regress an agent's guardrail coverage: a prompt
tweak that improves helpfulness metrics may also eliminate a safeguard against
prompt injection.

Existing practice: periodic red-team engagement ($16K+ minimum per Mindgard
2026 data) or ad-hoc promptfoo runs that produce a float, not a gate-able
typed result. Neither catches the regression on the day it ships.

The LiteLLM supply-chain attack (March 2026) is an adjacent risk: a CI/CD
dependency change silently introduced malicious behaviour that exfiltrated
secrets. The same pattern applies to AI guardrails: a dependency update or
configuration change that silently removes a safeguard is a security regression
that CI should catch.

What this example would show
----------------------------
A CI runner (usable as a GitHub Actions step or a pre-merge check) that:

  1. Spins up the target agent in an isolated sandbox.
  2. Runs a parametric probe suite across four categories:
       - PROMPT_INJECTION   (direct + indirect; OWASP LLM01)
       - DATA_EXFIL         (tool misuse to exfiltrate context; OWASP LLM02)
       - TOOL_ABUSE         (invoke tools outside intended scope; OWASP LLM07)
       - JAILBREAK          (role-play / DAN-style; OWASP LLM01)
  3. Computes a per-category pass rate.
  4. Compares against the baseline stored at the last green commit.
  5. For each category that regressed beyond the configured tolerance:
       - ``ground_finding`` the regression in the delta evidence (which specific
         probe started failing; what the model output before vs after).
       - Returns a typed ``Finding(severity=HIGH)`` with evidence refs.
  6. Exits non-zero if any ``Finding`` was emitted; exits 0 otherwise.

Expected outcomes
-----------------
  Green PR (no regression):
    All probe categories within tolerance → exit 0 → merge allowed.

  Red PR (guardrail regressed):
    Finding(
      title="Prompt injection pass rate regressed: 94% → 71% on commit abc1234",
      severity=HIGH,
      asset="agent://customer-support-v2",
      taxonomy=[OwaspLLM.PROMPT_INJECTION],
      evidence_refs=[
          "probe:injection_001:baseline_pass=True:current_pass=False:output=<snippet>",
          "probe:injection_017:baseline_pass=True:current_pass=False:output=<snippet>",
      ],
    )
    → exit 1 → PR blocked.

Why this is not a toy
---------------------
- The probe suite is the same as Example 2 (injection probe) + the scenarios/
  directory already provides structural patterns for each category.
- GSAR thresholds encode the policy decision: injection gate at S ≥ 0.90,
  jailbreak gate at S ≥ 0.80, etc. Security teams configure these once;
  developers don't touch them.
- Evidence refs are commit-addressable: a security engineer can look at the CI
  artifact, see exactly which probe regressed and what the model said, and
  reproduce it locally. Not a float in a dashboard PDF.
- The "shift left" narrative is the strongest developer pitch for Pillar B:
  grounded AI security testing is now a PR check, not a quarterly audit.
- Post-LiteLLM: every team that runs AI deps in CI now has a reason to add an
  AI-specific security gate alongside their regular SAST/SCA scans.

Taxonomy
--------
- OWASP LLM01 Prompt Injection
- OWASP LLM07 System Prompt Leakage / Excessive Agency
- MITRE ATLAS AML.T0043 Craft Adversarial Data

Design sketch (pseudocode — implementation target)
--------------------------------------------------
    @dataclass
    class ProbeResult:
        probe_id: str
        category: ProbeCategory
        baseline_passed: bool
        current_passed: bool
        model_output: str

    async def run_ci_gate(
        target: Target,
        baseline_path: Path,      # JSON stored at last green commit
        tolerances: dict[ProbeCategory, float],  # e.g. {INJECTION: 0.05}
    ) -> int:                     # exit code: 0 = pass, 1 = fail

        results   = await run_probe_suite(target)
        baseline  = load_baseline(baseline_path)
        findings  = []

        for category, probes in group_by_category(results).items():
            current_rate  = pass_rate(probes, current=True)
            baseline_rate = pass_rate(probes, baseline=True)
            delta = baseline_rate - current_rate

            if delta > tolerances.get(category, 0.05):
                regressed = [p for p in probes if p.baseline_passed and not p.current_passed]
                partition = Partition(
                    grounded=[
                        Claim(
                            f"Probe {p.probe_id} passed at baseline, fails now",
                            EvidenceType.TOOL_MATCH,
                            evidence_refs=[
                                f"probe:{p.probe_id}:baseline_pass=True"
                                f":current_pass=False:output={p.model_output[:60]}"
                            ],
                        )
                        for p in regressed
                    ]
                )
                f = ground_finding(
                    title=f"{category.value} pass rate regressed: "
                          f"{baseline_rate:.0%} → {current_rate:.0%}",
                    severity=Severity.HIGH,
                    asset=str(target.endpoint),
                    remediation="Revert the prompt/config change that caused the regression.",
                    partition=partition,
                    taxonomy=CATEGORY_TAXONOMY[category],
                )
                if is_finding(f):
                    findings.append(f)

        if findings:
            print_findings(findings)
            return 1
        save_baseline(baseline_path, results)
        return 0

Implementation prerequisites
-----------------------------
- ``tulip.security.ground_finding``  ✓ (notebook_37)
- ``Target.endpoint``  ✓ (core SDK API)
- Missing: ``ProbeCategory``, probe suite loader, ``run_probe_suite``,
  baseline serialization, ``CATEGORY_TAXONOMY`` map — implementation targets.
- GitHub Actions YAML wrapper (5 lines) that runs this and uses the exit code.
"""

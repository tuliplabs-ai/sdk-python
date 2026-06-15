# Copyright 2026 Tulip Labs
# SPDX-License-Identifier: Apache-2.0
# PROPOSAL — not yet wired to src/; see docs/market/2026-06-15_market_brief.md §6 Example 4
"""PROPOSAL: AI dependency supply-chain integrity scan.

PILLAR B — Agentic AI FOR AI

Motivation: the LiteLLM supply-chain attack (March 2026)
---------------------------------------------------------
On 2026-03-24, versions 1.82.7 and 1.82.8 of ``litellm`` were published to
PyPI by threat group TeamPCP. Each package contained a malicious ``.pth``
file (``litellm_init.pth``) that auto-executes on every Python process startup
when litellm is installed. The payload exfiltrated AWS/GCP/Azure tokens, SSH
keys, and Kubernetes credentials. LiteLLM has ~97M downloads/month.

The attack vector is MITRE ATLAS AML.T0048 (v5.4.0 addition) "Publish
Poisoned AI Agent Tool". Existing SCA tools (Snyk, Dependabot, Protect AI
Guardian) focus on known CVEs in model files — none scan for AI-stack
packages with malicious import-time side-effects.

What this example would show
----------------------------
A scan agent that:

  1. Parses ``requirements.txt`` / ``pyproject.toml`` / ``uv.lock`` and
     identifies AI/ML packages (litellm, langchain, transformers, huggingface,
     anthropic, openai, vllm, etc.).

  2. For each package version in the lockfile:
       (a) Queries PyPI metadata (release date, uploader account, file hashes).
       (b) Checks against a known-compromised version table (offline sample
           includes the LiteLLM 1.82.7/1.82.8 event).
       (c) Optionally: unpacks the sdist/wheel and scans for ``.pth`` files,
           ``sitecustomize.py`` overrides, and ``__init__.py`` import-time
           subprocess / socket calls.

  3. Grounds each finding in the PyPI metadata evidence:
       - Known-compromised version → ``Finding(severity=CRITICAL)``
         with evidence_ref = the PyPI release metadata hash + advisory ref.
       - Suspicious package structure (.pth file present) → ``Finding(severity=HIGH)``
         with evidence_ref = the specific file path and its content hash.
       - Clean → ``Abstention`` (explicitly: the agent examined these packages
         and found no evidence of compromise).

Expected grounded findings
--------------------------
  # Lockfile contains litellm==1.82.8 (known-compromised)
  Finding(
    title="Known-compromised AI package: litellm==1.82.8 (LiteLLM supply-chain attack, 2026-03-24)",
    severity=CRITICAL,
    asset="requirements.txt:litellm==1.82.8",
    remediation="Pin to litellm>=1.82.9 (clean release). Rotate all secrets on systems "
                "where the compromised version was installed.",
    taxonomy=[AtlasTechnique.PUBLISH_POISONED_AI_AGENT_TOOL],   # AML.T0048
    evidence_refs=[
        "pypi:litellm:1.82.8:sha256=<hash>:known_compromise=CVE-2026-LITELLM-01",
        "advisory:https://docs.litellm.ai/blog/security-update-march-2026",
    ],
  )

  # Lockfile is clean
  Abstention(
    candidate_title="AI package supply-chain scan",
    reason="All 14 AI packages examined; none match known-compromised versions "
           "and no suspicious import-time side-effects detected.",
    gsar_score=1.0,   # perfect evidence coverage = confident clean verdict
  )

Why this is not a toy
---------------------
- The LiteLLM attack is real and documented. The offline evidence table
  (known-compromised version → advisory hash) mirrors the SCA database
  pattern that security teams already trust for traditional packages.
- The ``.pth`` file scan is a specific, actionable detection: these files
  auto-execute on ``python`` process start; no legitimate AI package needs one.
  The scanner checks for them structurally, not with a signature.
- The ``Abstention`` with ``gsar_score=1.0`` for a clean scan is an
  important output: it tells the security team "we looked and found nothing",
  which is different from "we didn't look". Audit trails need both signals.
- Protect AI Guardian scans model files (pickle, SafeTensors, ONNX). This
  scanner targets the *inference stack* packages — a gap that the LiteLLM
  attack made obvious.
- Plugs directly into the CI gate (Example 3) as a pre-step: if the
  supply-chain scan finds a compromised package, block the PR before even
  running the guardrail coverage checks.

Taxonomy
--------
- MITRE ATLAS AML.T0048 Publish Poisoned AI Agent Tool (v5.4.0)
- OWASP LLM03 Supply Chain Vulnerabilities
- CWE-1104 Use of Unmaintained Third-Party Components

Design sketch (pseudocode — implementation target)
--------------------------------------------------
    KNOWN_COMPROMISED: dict[str, dict] = {
        "litellm==1.82.7": {
            "advisory": "https://docs.litellm.ai/blog/security-update-march-2026",
            "atlas": "AML.T0048",
            "payload": ".pth auto-exec → credential exfil",
        },
        "litellm==1.82.8": {
            "advisory": "https://docs.litellm.ai/blog/security-update-march-2026",
            "atlas": "AML.T0048",
            "payload": ".pth auto-exec → credential exfil",
        },
    }

    def scan_lockfile(lockfile: Path) -> list[Finding | Abstention]:
        packages = parse_ai_packages(lockfile)   # returns [("litellm", "1.82.8"), ...]
        results = []
        for name, version in packages:
            pin = f"{name}=={version}"
            if pin in KNOWN_COMPROMISED:
                rec = KNOWN_COMPROMISED[pin]
                meta = fetch_pypi_metadata(name, version)   # offline: returns sample hash
                partition = Partition(
                    grounded=[
                        Claim(
                            f"{pin} matches known-compromised version",
                            EvidenceType.TOOL_MATCH,
                            evidence_refs=[
                                f"pypi:{name}:{version}:sha256={meta['sha256']}",
                                f"advisory:{rec['advisory']}",
                            ],
                        )
                    ]
                )
                results.append(ground_finding(
                    title=f"Known-compromised AI package: {pin}",
                    severity=Severity.CRITICAL,
                    asset=f"{lockfile}:{pin}",
                    remediation=f"Upgrade {name} past the affected range; rotate secrets.",
                    partition=partition,
                    taxonomy=[AtlasTechnique.PUBLISH_POISONED_AI_AGENT_TOOL],
                ))
            else:
                results.append(Abstention(
                    candidate_title=f"Supply-chain check: {pin}",
                    reason=f"{pin} not in known-compromised table; no .pth anomaly detected.",
                    gsar_score=1.0,
                    decision=Decision.PROCEED,
                ))
        return results

Implementation prerequisites
-----------------------------
- ``tulip.security.ground_finding`` + ``Abstention``  ✓ (notebook_37)
- Missing: ``parse_ai_packages``, ``fetch_pypi_metadata`` (offline sample + live
  PyPI path), ``AtlasTechnique.PUBLISH_POISONED_AI_AGENT_TOOL`` (check current
  Atlas enum coverage), ``KNOWN_COMPROMISED`` table — implementation targets.
- The online PyPI metadata path needs no API key (public JSON endpoint).
"""

# DevSecOps Security Factory (Azure Edition)

A CI/CD pipeline that automatically detects and blocks security issues across the software lifecycle — from source code, through container build, to (soon) cloud infrastructure and runtime.

## Status: In Progress

This is an active learning project. Current phase: Azure IaC (Phase 4).

## What's implemented so far

| Control | Tool | Status |
|---|---|---|
| Secret scanning | Gitleaks | ✅ Enforced on every PR |
| SAST | Semgrep | ✅ Enforced on every PR |
| Dependency scanning + SBOM | Trivy (filesystem) | ✅ Enforced on every PR |
| Container image scanning | Trivy (image) | ✅ Enforced on every PR |
| Unit tests | Pytest | ✅ Enforced on every PR |
| IaC scanning | Checkov | ⏳ Coming next (Phase 4) |
| Cloud deployment | Terraform + AKS | ⏳ Coming next (Phase 4/5) |
| DAST | OWASP ZAP | ⏳ Planned (Phase 5) |
| Runtime detection | Falco | ⏳ Planned (Phase 5) |

All checks are **required** via GitHub branch protection — a failing check genuinely blocks merging to `main`, not just a status badge.

## Application

A minimal Flask API with one authenticated endpoint, used as a deliberately simple target for the security pipeline to protect. `/health` is public; `/secure-data` requires an `X-API-Key` header.

## Container

Built on `python:3.14.6-alpine3.24` rather than the Debian variant — a Trivy scan comparison during development showed Alpine's minimal package set eliminates most OS-level CVEs that Debian (both `trixie` and `bookworm`) carries by default (see `docs/security-report.md`). Runs as a non-root user (`appuser`, UID 1000).

## Running locally

\`\`\`bash
cd app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
\`\`\`

## Running in Docker

\`\`\`bash
cd app
docker build -t devsecops-app .
docker run -p 5000:5000 -e API_KEY=your-key-here devsecops-app
\`\`\`

## Architecture

See `docs/architecture-diagram.md` for the full pipeline flow.

## Security documentation

- [`docs/threat-model.md`](docs/threat-model.md) — STRIDE-based threat model
- [`docs/security-report.md`](docs/security-report.md) — findings and decisions log
- [`docs/remediation-report.md`](docs/remediation-report.md) — vulnerabilities introduced, detected, and fixed (in progress)

## What I'd add with more time

- Azure Key Vault integration for real secrets management (currently env-var based, documented as a known limitation)
- SARIF upload to GitHub's Security tab
- OPA/Kyverno policy-as-code on the Kubernetes layer
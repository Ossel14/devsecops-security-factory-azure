# Threat Model

Using STRIDE. This is a living document — fully populated during the project's remediation phase, updated as each control is implemented.

| Threat category | Example in this project | Control | Status |
|---|---|---|---|
| **S**poofing | Unauthorized access to `/secure-data` without a valid key | API key check | ✅ Implemented |
| **T**ampering | Malicious dependency introduced via `requirements.txt` | Trivy SCA scan | ✅ Implemented |
| **R**epudiation | No audit trail of who deployed what | GitHub Actions run history + commit SHA tagging | ✅ Partial (via CI logs) |
| **I**nformation disclosure | Secret committed to source (API keys, tokens) | Gitleaks | ✅ Implemented |
| **D**enial of service | Resource exhaustion via unrestricted deployment | Azure NSG rules, AKS resource limits | ⏳ Phase 4/5 |
| **E**levation of privilege | Container running as root, escaping to host | Non-root Docker user, Falco runtime detection | ✅ Partial (non-root done, Falco pending) |

## Assets
- Source code and CI/CD pipeline configuration
- The Flask application and its API key
- Azure infrastructure (once deployed): Storage Account, AKS cluster, NSGs

## Assumptions
- This is a demonstration/learning project, not a production system — some controls (e.g. real secrets management via Key Vault) are documented as intended future work rather than fully implemented, and that tradeoff is explicit rather than hidden.
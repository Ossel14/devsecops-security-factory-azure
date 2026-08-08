# Architecture

\`\`\`mermaid
flowchart TD
    A[Developer] --> B[GitHub repo]
    B --> C[Pull request]
    C --> D{GitHub Actions — required checks}
    D --> E[Gitleaks]
    D --> F[Semgrep]
    D --> G[Trivy FS + SBOM]
    D --> H[Trivy image scan]
    D --> I[Pytest]
    E --> J[main - protected]
    F --> J
    G --> J
    H --> J
    I --> J
    J -.Phase 4/5.-> K[Azure IaC, AKS, DAST, Falco]
\`\`\`

## Current state
All five GitHub Actions jobs above are implemented and required via branch protection — a failing check blocks merging to `main`. Azure infrastructure, deployment, DAST, and runtime detection are the next phases.
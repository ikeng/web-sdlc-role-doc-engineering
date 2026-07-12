# SDLC Role Doc Engineering

Role-first SDLC document engineering framework with reusable templates, standards, and a complete example project.

## Structure

```
.
├── README.md
├── .gitignore
├── templates/
│   ├── roles/
│   ├── standards/
│   └── deliverable-templates/
├── examples/
│   └── shopwave/
│       ├── README.md
│       ├── project-info.md
│       ├── roles/
│       ├── deliverables/
│       ├── decisions/
│       ├── sprint-artifacts/
│       ├── docs/
│       └── audit/
└── skills/
    └── sdlc-role-doc-engineering/
        ├── SKILL.md
        ├── assets/
        ├── references/
        └── scripts/
```

## Usage

1. **Role definitions**: `templates/roles/` contains reusable role definitions.
2. **Deliverable templates**: `templates/deliverable-templates/` contains blank templates.
3. **Standards**: `templates/standards/` contains project-wide standards.
4. **Example project**: `examples/shopwave/` shows filled deliverables and enriched role definitions.
5. **Skill**: `skills/sdlc-role-doc-engineering/` encodes the SOP for reuse.

## Quick start

```bash
# Validate ShopWave example artifacts
python3 skills/sdlc-role-doc-engineering/scripts/validate_docs.py .
```

## Role Catalog

| Role | Primary Phase | Key Deliverables |
|------|--------------|------------------|
| Product Owner (PO) | Product | Product Vision, Backlog, User Stories |
| Business Analyst (BA) | Analysis | Requirements Spec, Business Rules |
| UX/UI Designer | Design | Wireframes, UI Spec, Design System |
| Solution Architect | Architecture | Architecture Doc, Tech Stack, API Design |
| Tech Lead | Development | Code Standards, Dev Guidelines |
| Full-stack Developer | Development | Implementation, Code Review |
| QA Engineer | Quality | Test Plan, Test Cases, Quality Metrics |
| DevOps Engineer | Deployment | Deployment Plan, CI/CD Pipeline, Runbook |
| Project Manager | Project | Project Charter, Sprint Plan, Risk Register |
| Security Engineer | Security | Security Requirements, Threat Model |

## Deliverable Categories

- **Product** - Vision, backlog, user stories
- **Analysis** - Requirements, use cases, business rules
- **Design** - Wireframes, UI specs, design systems
- **Architecture** - System design, tech stack, APIs
- **Development** - Code standards, guidelines
- **Quality** - Test plans, test cases, metrics
- **Deployment** - Deployment plans, CI/CD, runbooks
- **Project** - Charters, sprint plans, risk registers
- **Security** - Security requirements, threat models

## Standards

- Documentation Standards - Format, style, versioning
- Naming Conventions - Files, versions, metadata
- Code Review Standards - Review criteria and process
- Quality Gates - Review checkpoints and validation

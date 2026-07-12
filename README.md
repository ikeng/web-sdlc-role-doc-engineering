# SDLC Roles & Deliverables Framework

Web-focused Agile/Scrum SDLC role definitions, output specifications, and reusable templates.

## Quick Start

```bash
# Browse roles
ls roles/

# Browse deliverables by phase
ls deliverables/

# Use a template
cp templates/user-story-template.md deliverables/product/user-stories.md
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

## Usage

1. **Role Definition**: Each role file defines responsibilities, outputs, and file dimensions
2. **Deliverable Creation**: Use templates in `templates/` for consistent output
3. **Quality Assurance**: Follow standards in `standards/` for all artifacts
4. **Review Process**: Use quality gates before phase transitions

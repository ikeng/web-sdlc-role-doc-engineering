# SDLC Role Definitions

## Role Overview

This directory contains detailed definitions for each SDLC role in our Agile/Scrum web development process.

## Role List

| Role | Phase | Description |
|------|-------|-------------|
| [Product Owner](./product-owner.md) | Product | Defines product vision and prioritizes backlog |
| [Business Analyst](./business-analyst.md) | Analysis | Gathers and analyzes business requirements |
| [UX/UI Designer](./ux-designer.md) | Design | Creates user experience and interface designs |
| [Solution Architect](./solution-architect.md) | Architecture | Designs system architecture and tech stack |
| [Tech Lead](./tech-lead.md) | Development | Leads technical implementation and code quality |
| [Full-stack Developer](./fullstack-developer.md) | Development | Implements features across the stack |
| [QA Engineer](./qa-engineer.md) | Quality | Ensures quality through testing |
| [DevOps Engineer](./devops-engineer.md) | Deployment | Manages deployment and infrastructure |
| [Project Manager](./project-manager.md) | Project | Coordinates sprints and manages risks |
| [Security Engineer](./security-engineer.md) | Security | Ensures application security |

## Role Interactions

```
PO → BA → Designer → Architect → Tech Lead → Developer → QA → DevOps
  ↓        ↓           ↓          ↓           ↓        ↓       ↓
  └────────┴───────────┴──────────┴───────────┴────────┴───────┘
                           PM (coordination)
                           Security Engineer (all phases)
```

## Quick Reference

Each role definition includes:
- **Responsibilities** - Core duties and accountabilities
- **Output Files** - Deliverables produced by this role
- **File Dimensions** - Structure and content requirements for each deliverable
- **Quality Gates** - Review criteria and acceptance standards

## Usage

1. **Onboarding**: Read relevant role file to understand responsibilities
2. **Planning**: Reference role outputs when defining sprint goals
3. **Quality**: Use quality gates to validate deliverables
4. **Handoff**: Follow role interaction patterns for smooth transitions

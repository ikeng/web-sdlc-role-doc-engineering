# ShopWave - README

## Project Overview

ShopWave is an e-commerce platform for handcrafted home goods, connecting artisans with conscious consumers.

**Tech Stack**: React + Node.js + PostgreSQL + Stripe + AWS
**Team**: 4 developers
**Timeline**: 6 months (Feb 2026 - Jul 2026)
**Budget**: $135K

## Project Structure

```
shopwave/
├── README.md # This file
├── docs/
│   └── README.md # Documentation index
├── decisions/
│   ├── README.md # ADR index
│   ├── adr-001-react-frontend.md
│   ├── adr-002-nodejs-backend.md
│   ├── adr-003-postgresql-database.md
│   └── adr-004-stripe-payments.md
├── sprint-artifacts/
│   ├── sprint-01/
│   │   ├── sprint-plan.md
│   │   ├── test-execution-summary.md
│   │   └── retro.md
│   ├── sprint-02/
│   │   ├── sprint-plan.md
│   │   ├── test-execution-summary.md
│   │   └── retro.md
│   └── sprint-03/
│       ├── sprint-plan.md
│       ├── test-execution-summary.md
│       └── retro.md
└── deliverables/
    ├── analysis/
    │   ├── requirements-spec.md
    │   ├── business-rules.md
    │   └── use-case-diagram.md
    ├── design/
    │   ├── design-system.md
    │   ├── ui-spec.md
    │   └── wireframes.md
    ├── architecture/
    │   ├── architecture-doc.md
    │   ├── tech-stack.md
    │   └── api-design.md
    ├── development/
    │   ├── code-standards.md
    │   ├── dev-guidelines.md
    │   └── code-review-checklist.md
    ├── quality/
    │   ├── test-plan.md
    │   ├── test-cases.md
    │   └── quality-metrics.md
    ├── deployment/
    │   ├── deployment-plan.md
    │   ├── ci-cd-pipeline.md
    │   └── runbook.md
    ├── project/
    │   ├── project-charter.md
    │   ├── sprint-plan.md
    │   └── risk-register.md
    └── security/
        ├── security-requirements.md
        ├── threat-model.md
        └── security-checklist.md
```

## Key Documents

### Product
- [Requirements Spec](deliverables/analysis/requirements-spec.md)
- [Acceptance Criteria](deliverables/product/acceptance-criteria.md)

### Architecture
- [Architecture Doc](deliverables/architecture/architecture-doc.md)
- [Tech Stack](deliverables/architecture/tech-stack.md)
- [API Design](deliverables/architecture/api-design.md)

### Development
- [Code Standards](deliverables/development/code-standards.md)
- [Dev Guidelines](deliverables/development/dev-guidelines.md)
- [Code Review Checklist](deliverables/development/code-review-checklist.md)

### Quality
- [Test Plan](deliverables/quality/test-plan.md)
- [Test Cases](deliverables/quality/test-cases.md)
- [Quality Metrics](deliverables/quality/quality-metrics.md)

### Deployment
- [Deployment Plan](deliverables/deployment/deployment-plan.md)
- [CI/CD Pipeline](deliverables/deployment/ci-cd-pipeline.md)
- [Runbook](deliverables/deployment/runbook.md)

### Project Management
- [Project Charter](deliverables/project/project-charter.md)
- [Risk Register](deliverables/project/risk-register.md)

### Security
- [Security Requirements](deliverables/security/security-requirements.md)
- [Threat Model](deliverables/security/threat-model.md)
- [Security Checklist](deliverables/security/security-checklist.md)

## Getting Started

### Prerequisites
- Node.js 20+
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose

### Installation

```bash
# Clone the repository
git clone https://github.com/shopwave/shopwave.git
cd shopwave

# Install dependencies
npm install

# Set up environment
cp .env.example .env

# Run database migrations
npm run db:migrate

# Start development servers
npm run dev
```

### Running Tests

```bash
# Run all tests
npm test

# Run specific test types
npm run test:unit
npm run test:integration
npm run test:e2e
```

## Team

| Role | Name | Email |
|------|------|-------|
| Product Owner | Alex Rivera | alex@shopwave.com |
| Tech Lead | Morgan Lee | morgan@shopwave.com |
| Developer | Riley Chen | riley@shopwave.com |
| QA Engineer | Quinn Brooks | quinn@shopwave.com |
| UX Designer | Taylor Kim | taylor@shopwave.com |
| DevOps Engineer | Alex Kim | alex.kim@shopwave.com |
| Security Engineer | Riley Park | riley.park@shopwave.com |
| Project Manager | Sam Patel | sam@shopwave.com |

## License
Private - All rights reserved

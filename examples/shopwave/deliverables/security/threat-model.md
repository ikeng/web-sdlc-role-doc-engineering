# ShopWave - Threat Model

## Metadata
- **Version**: 1.0
- **Author**: Riley Park (Security Engineer)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved

## Methodology

This threat model uses the STRIDE methodology:
- **S**poofing identity
- **T**ampering with data
- **R**epudiation
- **I**nformation disclosure
- **D**enial of service
- **E**levation of privilege

## System Architecture Overview

### Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                                 Users                               │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│  CloudFront CDN                    AWS WAF                            │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Application Load Balancer                                          │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│  ECS Cluster (ShopWave Application)                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
│  │ Frontend    │  │ Backend     │  │ Worker      │                 │
│  │ (React)     │  │ (Node.js)   │  │ (Jobs)      │                 │
│  └─────────────┘  └─────────────┘  └─────────────┘                 │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│  RDS PostgreSQL (Primary + Read Replica)                            │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│  ElastiCache Redis                                                   │
└─────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│  AWS S3 (Product Images, User Assets)                                │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow Diagrams

### DFD 1: User Authentication

```
┌─────┐          ┌─────┐          ┌─────┐          ┌─────────┐
│ User│          │ FE  │          │ LB  │          │ Backend │
└─────┘          └─────┘          └─────┘          └─────────┘
   │                  │                │                  │
   │ 1. Login Request │                │                  │
   │─────────────────>│                │                  │
   │                  │ 2. POST /login │                  │
   │                  │───────────────>│                  │
   │                  │                │ 3. Validate       │
   │                  │                │──────────────────>│
   │                  │                │                  │ 4. DB Query
   │                  │                │                  │─────────>
   │                  │                │                  │         │
   │                  │                │                  │<────────│
   │                  │                │<─────────────────│         │
   │                  │<───────────────│                  │         │
   │ 5. JWT Token     │                │                  │         │
   │<─────────────────│                │                  │         │
   │                  │                │                  │         │
```

### DFD 2: Product Purchase

```
┌─────┐       ┌─────┐       ┌─────────┐       ┌─────────┐
│ User│       │ FE  │       │ Backend │       │ Stripe │
└─────┘       └─────┘       └─────────┘       └─────────┘
   │              │              │                │
   │ 1. Checkout  │              │                │
   │─────────────>│              │                │
   │              │ 2. Request   │                │
   │              │─────────────>│                │
   │              │              │ 3. Create      │
   │              │              │───────────────>│
   │              │              │   Payment Intent│
   │              │              │<───────────────│
   │              │              │                │
   │              │              │ 4. Create      │
   │              │              │   Order        │
   │              │              │───────────────>│
   │              │              │                │ DB Query
   │              │              │                │─────────>
   │              │              │                │         │
   │              │              │                │<────────│
   │              │              │                │
   │              │<─────────────│                │
   │ 5. Redirect   │              │                │
   │<─────────────│              │                │
   │              │              │                │
   │ 6. Confirm   │              │                │
   │─────────────>│              │                │
   │              │─────────────>│                │
```

## Threat Analysis

### STRIDE Analysis

#### Spoofing Identity

| ID | Threat | Target | Mitigation |
|----|--------|--------|------------|
| TH-001 | Attacker guesses user password | User account | Password hashing, rate limiting, account lockout |
| TH-002 | Stolen JWT token used for impersonation | User account | Short token expiry, refresh token rotation |
| TH-003 | CSRF attack on authenticated requests | API endpoints | CSRF tokens, SameSite cookies |

#### Tampering with Data

| ID | Threat | Target | Mitigation |
|----|--------|--------|------------|
| TH-004 | SQL injection via search/filter | Database | Parameterized queries, ORM |
| TH-005 | XSS via product descriptions | Frontend | Input sanitization, CSP headers |
| TH-006 | Price manipulation in checkout | Order | Server-side price verification, immutable order history |

#### Repudiation

| ID | Threat | Target | Mitigation |
|----|--------|--------|------------|
| TH-007 | User denies placing order | Order | Audit logging, order confirmation |
| TH-008 | Admin denies system change | System | Access logs, change tracking |

#### Information Disclosure

| ID | Threat | Target | Mitigation |
|----|--------|--------|------------|
| TH-009 | Sensitive data in error messages | Users | Generic error messages, no PII in logs |
| TH-010 | Database credentials exposed | Infrastructure | Secrets Manager, no hardcoded credentials |
| TH-011 | API keys exposed in client | Third-party APIs | Backend-only API calls, environment variables |

#### Denial of Service

| ID | Threat | Target | Mitigation |
|----|--------|--------|------------|
| TH-012 | API rate limiting bypass | API | Rate limiting, DDoS protection |
| TH-013 | Resource exhaustion | Backend | Input validation, query optimization |
| TH-014 | DDoS attack | Infrastructure | AWS Shield, WAF, rate limiting |

#### Elevation of Privilege

| ID | Threat | Target | Mitigation |
|----|--------|--------|------------|
| TH-015 | Insecure direct object reference (IDOR) | Resources | Authorization checks, resource ownership validation |
| TH-016 | Broken access control on admin endpoints | Admin | Role-based access control |
| TH-017 | JWT algorithm confusion attack | Authentication | Algorithm whitelist, validation |

## Attack Surface Analysis

### Public Attack Surface
- Web application (React)
- API endpoints (Node.js)
- CDN assets

### Partially Protected Surface
- Admin dashboard (requires authentication)

### Restricted Surface
- Database (private subnet)
- Internal services

## Risk Assessment

### High Risk
- Payment processing (PCI DSS requirements)
- User authentication (credential theft)
- Data privacy (GDPR requirements)

### Medium Risk
- API security (rate limiting, injection)
- Third-party integrations (Stripe, SendGrid)

### Low Risk
- Public content (product catalog)
- Static assets (images, CSS, JS)

## Security Controls

### Preventive Controls
- Authentication and authorization
- Input validation and sanitization
- Encryption (at rest and in transit)
- Rate limiting
- WAF rules

### Detective Controls
- Security event logging
- Anomaly detection
- Security scanning (SAST, DAST)

### Corrective Controls
- Automatic vulnerability patching
- Incident response plan
- Backup and recovery

## Compliance Mapping

### PCI DSS
- SEC-AUTH-001: Password Security
- SEC-AUTH-002: Session Management
- SEC-DATA-001: Encryption at Rest
- SEC-DATA-002: Encryption in Transit

### GDPR
- SEC-DATA-004: PII Protection
- SEC-DATA-005: Data Retention
- User consent management

## Approval

- [ ] Riley Park (Security Engineer)
- [ ] Jordan Smith (Solution Architect)
- [ ] Morgan Lee (Tech Lead)

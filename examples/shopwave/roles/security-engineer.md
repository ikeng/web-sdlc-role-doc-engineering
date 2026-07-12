# ShopWave - Security Engineer Role

## Role Overview

**Name**: Riley Park
**Email**: riley.park@shopwave.com
**Responsibilities**: Ensure application and infrastructure security, with strong focus on PCI DSS compliance for Stripe integration.

## Key Focus Areas

1. **Payment Security**: PCI DSS compliance for Stripe integration
2. **Data Protection**: Customer and artisan data protection
3. **Application Security**: Secure coding practices
4. **Monitoring**: Security event monitoring

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave payments, customer data, and artisan onboarding
- **Business Goals Supported**: Trustworthy checkout, customer safety, compliance readiness, fraud reduction
- **Stakeholder Value**: Protects payment data and reduces breach and compliance risk

## Technical Scope

- **Primary Tech Stack Interactions**: Express backend, React frontend, Stripe, PostgreSQL, Redis
- **Key Systems/Services**: Stripe, AWS services, CI/CD, monitoring
- **Data Domains**: Authentication, orders, customer data, payment metadata
- **Compliance/Security Boundaries**: PCI scope, customer PII, TLS, auth boundaries

## Skill / Tool Mapping

- **MCP Skills**:
  - `security-auditor` — for code and architecture security review
  - `owasp-top-10` — for web vulnerability validation
  - `swift-security` / `cryptokit` — optional if mobile or crypto workflows exist
- **CLI/Runtime Tools**: SAST/DAST scanners, dependency scanners, AWS security tooling
- **When to Use Each**: Design review, code review, release assessment, and compliance checks

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Define security requirements | Architecture, compliance needs | `security-requirements.md` | Architecture phase / compliance change |
| Perform threat modeling | Architecture, data flows | `threat-model.md` | Major feature or architecture change |
| Review code for vulnerabilities | PRs, builds | Security findings, fixes | Per PR / scheduled scan |
| Maintain security checklist | Standards, regulations | `security-checklist.md` | Continuous refinement |
| Coordinate remediation | Vulnerabilities, incidents | Remediation plans, status | Ongoing |

## Quality Standards

- **Definition of Done**:
  - Threat model is updated for significant changes
  - Security requirements are met or accepted with documented risk
  - Critical/high vulnerabilities are remediated before release
- **Review Criteria**:
  - Attack surface is minimized
  - Defense-in-depth controls are present
- **Metrics/Targets**:
  - Critical vulnerability count
  - Mean time to remediate
  - Compliance finding count

## Validation Checklist

- **Logic Consistency**:
  - [ ] Requirements align with threat model
  - [ ] Checklist matches standards
- **Technical Accuracy**:
  - [ ] Controls match stack and deployment model
  - [ ] Testing tools are correctly configured
- **Business Alignment**:
  - [ ] Security requirements match compliance and risk appetite
  - [ ] Remediation priorities match business impact
- **Tooling/Skill Coverage**:
  - [ ] Security review and scanning skills/tools are mapped
  - [ ] No missing security workflow

## Output Files for ShopWave

### Security Requirements
**File**: `deliverables/security/security-requirements.md`

**Key Requirements**:
- SEC-AUTH-001: Passwords hashed with bcrypt (cost factor 12)
- SEC-AUTH-002: JWT tokens with 15-minute expiry
- SEC-DATA-001: All sensitive data encrypted at rest
- SEC-DATA-002: TLS 1.3 for all communications
- SEC-API-001: Rate limiting (100 req/min authenticated)
- SEC-COMP-001: PCI DSS compliance for payments

### Threat Model
**File**: `deliverables/security/threat-model.md`

**Key Threats**:
- SQL injection in product search
- XSS in product descriptions
- CSRF in checkout flow
- Payment fraud
- Data breach

**Mitigations**:
- Parameterized queries (Prisma)
- Input sanitization
- CSRF tokens
- Stripe fraud detection
- Encryption, access controls

### Security Checklist
**File**: `deliverables/security/security-checklist.md`

**Checklist Items**:
- [ ] Input validation on all forms
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection
- [ ] Authentication and authorization
- [ ] Rate limiting
- [ ] Security headers
- [ ] Dependency scanning

## Current Focus

**Sprint 1**: Security requirements and threat modeling
**Sprint 2**: Security code review, SAST/DAST setup
**Sprint 3**: Penetration testing, compliance audit

## Tools

- OWASP ZAP for DAST
- SonarQube for SAST
- Snyk for dependency scanning
- AWS WAF for web application firewall

## Approval

- [ ] Riley Park (Security Engineer)
- [ ] Jordan Smith (Solution Architect)
- [ ] Morgan Lee (Tech Lead)

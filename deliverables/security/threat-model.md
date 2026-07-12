# Threat Model

## Metadata
- **Version**: 1.0
- **Author**: Security Engineer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Status**: Draft / In Review / Approved

## System Overview

**System Name**: [Application Name]
**Architecture**: [Microservices / Monolith / etc.]
**Technology Stack**: [Frontend: React, Backend: Node.js, Database: PostgreSQL, etc.]

## System Diagram

```
┌─────────────┐
│   Users     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────┐
│         Load Balancer / CDN             │
└────────────────┬────────────────────────┘
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
┌──────────────┐   ┌──────────────┐
│  Web Server  │   │  Web Server  │
│   (Node 1)   │   │   (Node 2)   │
└──────┬───────┘   └──────┬───────┘
       │                   │
       └─────────┬─────────┘
                 ▼
       ┌─────────────────────┐
       │   API Service       │
       │  (Business Logic)   │
       └─────────┬───────────┘
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Primary  │ │   Cache  │ │   Queue  │
│ Database │ │  (Redis) │ │  (SQS)   │
└──────────┘ └──────────┘ └──────────┘
```

## Trust Boundaries

### Boundary 1: Internet → Load Balancer
- **Description**: Internet users accessing the application
- **Threats**: DDoS, injection attacks, scraping
- **Controls**: WAF, rate limiting, DDoS protection

### Boundary 2: Load Balancer → Web Servers
- **Description**: Internal network traffic
- **Threats**: Man-in-the-middle attacks
- **Controls**: TLS encryption, network segmentation

### Boundary 3: Web Servers → API Service
- **Description**: Internal service communication
- **Threats**: Unauthorized access, data interception
- **Controls**: Network policies, mutual TLS

### Boundary 4: API Service → Database
- **Description**: Application accessing data storage
- **Threats**: SQL injection, unauthorized data access
- **Controls**: Parameterized queries, RBAC, encryption

## Data Flow Analysis

### Flow 1: User Authentication

```
User → LB → Web Server → API Service → Database
```

**Data**: Email, password, JWT tokens
**Sensitivity**: High
**Threats**: Credential theft, session hijacking
**Controls**: TLS, bcrypt hashing, JWT with short expiry, HTTP-only cookies

### Flow 2: User Registration

```
User → LB → Web Server → API Service → Database
                                    → Email Service
```

**Data**: Email, password, name
**Sensitivity**: High
**Threats**: Data breach, email enumeration
**Controls**: TLS, input validation, rate limiting, generic error messages

### Flow 3: Payment Processing

```
User → LB → Web Server → API Service → Payment Gateway
                                    → Database
```

**Data**: Payment details, order information
**Sensitivity**: Critical
**Threats**: Payment fraud, data theft
**Controls**: PCI DSS compliance, tokenization, HTTPS, audit logging

### Flow 4: File Upload

```
User → LB → Web Server → API Service → S3 Storage
                                    → Database
```

**Data**: User-uploaded files
**Sensitivity**: Medium
**Threats**: Malware upload, path traversal
**Controls**: File type validation, malware scanning, random filenames, size limits

## Threat Identification (STRIDE)

### Spoofing Identity

**THREAT-001: Credential Theft**
- **Description**: Attacker steals user credentials
- **Attack Vector**: Phishing, keylogging, data breach
- **Impact**: High - Unauthorized access to user accounts
- **Likelihood**: Medium
- **Risk Score**: 12

**Mitigations**:
- Implement MFA
- Rate limiting on login
- Account lockout after failed attempts
- Security awareness training
- Monitor for suspicious login patterns

---

**THREAT-002: Session Hijacking**
- **Description**: Attacker steals session token
- **Attack Vector**: XSS, network sniffing, malware
- **Impact**: High - Unauthorized access to user session
- **Likelihood**: Low
- **Risk Score**: 10

**Mitigations**:
- HTTP-only cookies
- Secure cookie flag
- Short token expiry
- Token rotation
- TLS everywhere

---

### Tampering with Data

**THREAT-003: SQL Injection**
- **Description**: Attacker manipulates database queries
- **Attack Vector**: Malicious input in forms, URLs
- **Impact**: Critical - Data breach, data manipulation
- **Likelihood**: Low (with proper controls)
- **Risk Score**: 8

**Mitigations**:
- Parameterized queries
- ORM usage (Prisma)
- Input validation
- Regular security scanning
- WAF rules

---

**THREAT-004: XSS (Cross-Site Scripting)**
- **Description**: Attacker injects malicious scripts
- **Attack Vector**: User input rendered without sanitization
- **Impact**: High - Session hijacking, data theft
- **Likelihood**: Medium
- **Risk Score**: 12

**Mitigations**:
- Input sanitization
- Output encoding
- Content Security Policy (CSP)
- Framework XSS protection

---

**THREAT-005: CSRF (Cross-Site Request Forgery)**
- **Description**: Attacker tricks user into making unwanted requests
- **Attack Vector**: Malicious website, email
- **Impact**: Medium - Unauthorized actions
- **Likelihood**: Medium
- **Risk Score**: 9

**Mitigations**:
- CSRF tokens
- SameSite cookies
- Origin/Referer validation

---

### Repudiation

**THREAT-006: Lack of Audit Trail**
- **Description**: Actions cannot be traced to users
- **Attack Vector**: Insider threat, compromised account
- **Impact**: Medium - Cannot investigate incidents
- **Likelihood**: Low
- **Risk Score**: 6

**Mitigations**:
- Comprehensive audit logging
- Log all authentication events
- Log all data modifications
- Immutable log storage
- Regular log review

---

### Information Disclosure

**THREAT-007: Sensitive Data Exposure**
- **Description**: Sensitive data exposed to unauthorized users
- **Attack Vector**: Data breach, misconfiguration
- **Impact**: Critical - Privacy violation, regulatory fines
- **Likelihood**: Low
- **Risk Score**: 10

**Mitigations**:
- Encryption at rest and in transit
- Access controls
- Data classification
- Regular security audits
- PII masking in logs

---

**THREAT-008: Error Message Information Leak**
- **Description**: Error messages expose sensitive information
- **Attack Vector**: Application errors
- **Impact**: Medium - Aids further attacks
- **Likelihood**: Medium
- **Risk Score**: 9

**Mitigations**:
- Generic error messages for users
- Detailed errors logged server-side
- No stack traces in production
- Error handling best practices

---

### Denial of Service

**THREAT-009: DDoS Attack**
- **Description**: Service overwhelmed by traffic
- **Attack Vector**: Botnet, amplification attacks
- **Impact**: High - Service unavailable
- **Likelihood**: Medium
- **Risk Score**: 12

**Mitigations**:
- DDoS protection (Cloudflare/AWS Shield)
- Rate limiting
- Auto-scaling
- CDN for static assets
- Traffic monitoring

---

**THREAT-010: Resource Exhaustion**
- **Description**: Attacker consumes resources
- **Attack Vector**: Large file uploads, complex queries
- **Impact**: Medium - Service degradation
- **Likelihood**: Medium
- **Risk Score**: 9

**Mitigations**:
- Rate limiting
- Request size limits
- Query timeouts
- Resource quotas
- Auto-scaling

---

### Elevation of Privilege

**THREAT-011: Broken Access Control**
- **Description**: Attacker gains unauthorized access
- **Attack Vector**: Insecure direct object references, privilege escalation
- **Impact**: Critical - Unauthorized access to data/functions
- **Likelihood**: Low
- **Risk Score**: 10

**Mitigations**:
- Authorization checks on every endpoint
- Principle of least privilege
- Regular access reviews
- Penetration testing

---

**THREAT-012: Insecure Deserialization**
- **Description**: Attacker manipulates serialized data
- **Attack Vector**: Malicious payload in serialized objects
- **Impact**: High - Remote code execution
- **Likelihood**: Low
- **Risk Score**: 8

**Mitigations**:
- Avoid deserializing untrusted data
- Use JSON instead of binary formats
- Input validation
- Type checking

## Risk Assessment Summary

| Threat | Likelihood | Impact | Risk Score | Priority |
|--------|------------|--------|------------|----------|
| SQL Injection | Low | Critical | 8 | High |
| XSS | Medium | High | 12 | High |
| CSRF | Medium | Medium | 9 | Medium |
| Credential Theft | Medium | High | 12 | High |
| Session Hijacking | Low | High | 10 | High |
| Sensitive Data Exposure | Low | Critical | 10 | High |
| DDoS | Medium | High | 12 | High |
| Broken Access Control | Low | Critical | 10 | High |

## Attack Tree

### Goal: Compromise User Account

```
Compromise User Account
├── Steal Credentials
│   ├── Phishing
│   ├── Keylogging
│   └── Data Breach
├── Session Hijacking
│   ├── XSS
│   ├── Network Sniffing
│   └── Malware
└── Privilege Escalation
    ├── Broken Access Control
    ├── Insecure Direct Object Reference
    └── Logic Flaws
```

## Security Controls

### Preventive Controls
- Input validation
- Authentication & authorization
- Encryption
- Rate limiting
- WAF

### Detective Controls
- Security monitoring
- Audit logging
- Intrusion detection
- Regular security scans

### Corrective Controls
- Incident response plan
- Backup and recovery
- Patch management
- Access revocation

## Recommendations

### High Priority
1. Implement MFA for all users
2. Add comprehensive audit logging
3. Implement WAF rules
4. Regular penetration testing

### Medium Priority
1. Security training for developers
2. Automated security scanning in CI/CD
3. Dependency management process
4. Incident response testing

### Low Priority
1. Bug bounty program
2. Security Champions program
3. Threat modeling for new features

## Approval

- [ ] Security Engineer
- [ ] Solution Architect
- [ ] Tech Lead

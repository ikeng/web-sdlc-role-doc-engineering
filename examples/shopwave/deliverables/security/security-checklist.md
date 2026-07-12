# ShopWave - Security Checklist

## Metadata
- **Version**: 1.0
- **Author**: Riley Park (Security Engineer)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved

## Security Checklist Overview

This checklist ensures security requirements are met throughout the SDLC.

## Development Phase

### Code Security

- [ ] Input validation implemented on all endpoints
- [ ] Output encoding for XSS prevention
- [ ] SQL injection prevention (parameterized queries)
- [ ] CSRF protection on state-changing operations
- [ ] No hardcoded credentials or secrets
- [ ] No console.log with sensitive data in production
- [ ] Error handling doesn't expose stack traces

### Authentication & Authorization

- [ ] Password hashing with bcrypt (cost factor ≥ 12)
- [ ] JWT tokens with appropriate expiry (access: 15min, refresh: 7d)
- [ ] Refresh tokens stored in HTTP-only cookies
- [ ] Account lockout after failed attempts (5 attempts, 15min lockout)
- [ ] RBAC implemented for all protected endpoints
- [ ] Authorization checks on all resources

### Data Protection

- [ ] Sensitive data encrypted at rest (AES-256)
- [ ] TLS 1.3 enforced for all connections
- [ ] Encryption keys stored in AWS KMS/Secrets Manager
- [ ] PII masked in logs
- [ ] Data minimization: collect only necessary data

## Testing Phase

### Security Testing

- [ ] SAST (Static Application Security Testing) configured
- [ ] DAST (Dynamic Application Security Testing) configured
- [ ] Dependency scanning configured (Snyk, Dependabot)
- [ ] Container scanning configured
- [ ] OWASP Top 10 vulnerabilities tested

### Specific Test Coverage

- [ ] Injection attacks tested (SQL, NoSQL, OS command)
- [ ] Broken authentication tested
- [ ] Sensitive data exposure tested
- [ ] XML external entities (XXE) tested
- [ ] Broken access control tested
- [ ] Security misconfiguration tested
- [ ] XSS tested (reflected, stored, DOM-based)
- [ ] Insecure deserialization tested
- [ ] Using components with known vulnerabilities
- [ ] Insufficient logging & monitoring tested

## Deployment Phase

### Infrastructure Security

- [ ] VPC configured with private subnets
- [ ] Security groups restrict access (principle of least privilege)
- [ ] No public database access
- [ ] WAF enabled with OWASP rules
- [ ] DDoS protection enabled (AWS Shield)
- [ ] Regular OS security patches applied
- [ ] Containers run as non-root user

### Secrets Management

- [ ] All secrets in AWS Secrets Manager
- [ ] No secrets in code or configuration files
- [ ] Secrets rotated regularly (90 days)
- [ ] Secrets access audited

### Monitoring & Logging

- [ ] Security event logging enabled
- [ ] Failed login attempts logged
- [ ] Privilege escalation attempts logged
- [ ] Audit logs retained for 1 year
- [ ] Security alerts configured

## Pre-Launch Security Review

### Code Review

- [ ] All PRs reviewed with security checklist
- [ ] No obvious vulnerabilities in code
- [ ] Secrets management reviewed
- [ ] Input validation reviewed
- [ ] Error handling reviewed

### Infrastructure Review

- [ ] Network security review completed
- [ ] Access controls reviewed
- [ ] Backup and recovery tested
- [ ] Incident response plan documented

### Compliance Review

- [ ] PCI DSS compliance verified (if handling payments)
- [ ] GDPR compliance verified
- [ ] Privacy policy published
- [ ] Cookie consent implemented

## Post-Launch Security

### Ongoing Monitoring

- [ ] Security alerts monitored daily
- [ ] Vulnerability scan results reviewed weekly
- [ ] Dependency updates applied weekly
- [ ] Security logs reviewed monthly

### Incident Response

- [ ] Incident response plan documented
- [ ] On-call security contact identified
- [ ] Escalation path defined
- [ ] Communication plan for security incidents

## Security Training

- [ ] Team completed security awareness training
- [ ] Secure coding practices documented
- [ ] Security champion identified
- [ ] Regular security reviews scheduled

## Approval

- [ ] Riley Park (Security Engineer)
- [ ] Jordan Smith (Solution Architect)
- [ ] Morgan Lee (Tech Lead)
- [ ] Sam Patel (Project Manager)

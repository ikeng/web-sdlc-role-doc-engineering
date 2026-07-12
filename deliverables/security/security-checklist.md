# Security Checklist

## Metadata
- **Version**: 1.0
- **Author**: Security Engineer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Last Updated**: YYYY-MM-DD

## Purpose

This checklist ensures security requirements are met throughout the SDLC. Use this checklist during design reviews, code reviews, and pre-deployment checks.

## Design Review Checklist

### Architecture & Design

- [ ] Security requirements are documented
- [ ] Threat model is created and reviewed
- [ ] Authentication and authorization are designed
- [ ] Data classification is complete
- [ ] Encryption strategy is defined
- [ ] Network segmentation is planned
- [ ] Monitoring and logging are designed
- [ ] Incident response plan is defined

### Data Protection

- [ ] Sensitive data is identified and cataloged
- [ ] Encryption at rest is planned (AES-256)
- [ ] Encryption in transit is planned (TLS 1.3)
- [ ] Data retention policies are defined
- [ ] Data backup strategy is defined
- [ ] Data deletion process is defined
- [ ] PII protection measures are planned

### Authentication & Authorization

- [ ] Authentication mechanism is chosen (JWT, OAuth, etc.)
- [ ] Password hashing algorithm selected (bcrypt)
- [ ] Session management strategy defined
- [ ] MFA support considered
- [ ] RBAC model designed
- [ ] Authorization checks planned for all endpoints
- [ ] Account lockout mechanism defined

## Code Review Checklist

### Input Validation

- [ ] All user input is validated
- [ ] Whitelist validation used where possible
- [ ] Input length limits enforced
- [ ] File uploads validated (type, size)
- [ ] Email addresses validated
- [ ] URLs validated to prevent SSRF

### SQL Injection Prevention

- [ ] Parameterized queries used
- [ ] ORM used (Prisma, TypeORM, etc.)
- [ ] No string concatenation in SQL queries
- [ ] Stored procedures validated (if used)

### XSS Prevention

- [ ] User input is sanitized before rendering
- [ ] Output encoding is implemented
- [ ] Content Security Policy (CSP) is configured
- [ ] Framework XSS protection is enabled

### CSRF Protection

- [ ] CSRF tokens implemented for state-changing operations
- [ ] SameSite cookie attribute set
- [ ] Origin/Referer validation implemented

### Authentication & Authorization

- [ ] Passwords are hashed (bcrypt, cost factor 12+)
- [ ] Passwords never logged
- [ ] JWT tokens have short expiry (15 minutes)
- [ ] Refresh tokens are secure (HTTP-only cookies)
- [ ] Authorization checks on all protected endpoints
- [ ] Principle of least privilege followed

### Error Handling

- [ ] Error messages don't expose sensitive information
- [ ] Stack traces not shown in production
- [ ] Errors are logged with context
- [ ] Generic error messages for users

### Cryptography

- [ ] Strong encryption algorithms used (AES-256, RSA-2048+)
- [ ] Secure random number generation
- [ ] Cryptographic keys are securely stored
- [ ] No hardcoded secrets or keys
- [ ] TLS 1.3 enforced

### Session Management

- [ ] Session tokens are random and long
- [ ] Sessions expire appropriately
- [ ] Session invalidation on logout
- [ ] Session fixation prevention

## API Security Checklist

### Authentication

- [ ] All endpoints require authentication (except public ones)
- [ ] JWT tokens are validated
- [ ] Token expiry is enforced
- [ ] Refresh token rotation implemented

### Authorization

- [ ] Authorization checks on all endpoints
- [ ] User can only access their own data
- [ ] Admin endpoints protected
- [ ] Role-based access control enforced

### Rate Limiting

- [ ] Rate limiting implemented
- [ ] Rate limits are appropriate
- [ ] Rate limit headers included in responses
- [ ] Exponential backoff for failed requests

### Input Validation

- [ ] Request body schema validated
- [ ] Query parameters validated
- [ ] Path parameters validated
- [ ] Invalid requests rejected (400)

### Error Handling

- [ ] Consistent error response format
- [ ] No stack traces in responses
- [ ] Appropriate HTTP status codes used
- [ ] Error messages don't leak information

## Database Security Checklist

### Access Control

- [ ] Database credentials are secured
- [ ] Principle of least privilege for DB users
- [ ] No hardcoded database credentials
- [ ] Database access is restricted by IP

### Query Security

- [ ] Parameterized queries used
- [ ] ORM used for database access
- [ ] No dynamic SQL construction
- [ ] Query timeouts configured

### Data Protection

- [ ] Sensitive data encrypted at rest
- [ ] Database backups encrypted
- [ ] PII data identified and protected
- [ ] Data retention policies enforced

### Monitoring

- [ ] Database queries are logged
- [ ] Slow queries are monitored
- [ ] Failed login attempts are logged
- [ ] Database access is audited

## Infrastructure Security Checklist

### Network Security

- [ ] VPC configured with private subnets
- [ ] Security groups restrict access
- [ ] No public database access
- [ ] WAF configured
- [ ] DDoS protection enabled
- [ ] Network segmentation implemented

### Server Hardening

- [ ] OS security patches applied
- [ ] Unnecessary services disabled
- [ ] Containers run as non-root
- [ ] Read-only file systems where possible
- [ ] Security headers configured

### Access Control

- [ ] SSH key-based authentication
- [ ] MFA for admin access
- [ ] Principle of least privilege
- [ ] Regular access reviews
- [ ] Audit trail for privileged actions

### Monitoring & Logging

- [ ] Centralized logging configured
- [ ] Security events monitored
- [ ] Intrusion detection enabled
- [ ] Alerts configured for suspicious activity
- [ ] Log retention policy defined

## Dependency Security Checklist

### Dependency Management

- [ ] Dependencies are scanned for vulnerabilities
- [ ] Automated dependency updates configured
- [ ] Unused dependencies removed
- [ ] Dependency versions are pinned
- [ ] License compliance checked

### Vulnerability Management

- [ ] SAST tools configured (SonarQube, Semgrep)
- [ ] DAST tools configured (OWASP ZAP)
- [ ] Container scanning configured (Trivy)
- [ ] Dependency scanning configured (Snyk, Dependabot)

### Third-Party Services

- [ ] Third-party services are security reviewed
- [ ] API keys are secured
- [ ] Third-party access is limited
- [ ] Monitoring for third-party service failures

## Deployment Security Checklist

### Pre-Deployment

- [ ] Security scan passes
- [ ] Vulnerability scan passes
- [ ] Secrets are in environment variables (not code)
- [ ] No debug mode in production
- [ ] Error messages don't expose sensitive info

### Configuration

- [ ] HTTPS enforced
- [ ] Security headers configured (CSP, HSTS, etc.)
- [ ] CORS properly configured
- [ ] Environment variables secured
- [ ] Secrets managed securely (AWS Secrets Manager)

### Post-Deployment

- [ ] Security monitoring active
- [ ] Alerts configured
- [ ] Incident response plan ready
- [ ] Backup and recovery tested

## Compliance Checklist

### GDPR Compliance

- [ ] Privacy policy published
- [ ] Cookie consent implemented
- [ ] Data processing records maintained
- [ ] Right to access implemented
- [ ] Right to erasure implemented
- [ ] Data portability implemented
- [ ] Breach notification process defined

### SOC 2 Compliance

- [ ] Access controls implemented
- [ ] Audit logging enabled
- [ ] Encryption at rest and in transit
- [ ] Incident response plan documented
- [ ] Regular security audits conducted

### PCI DSS Compliance (if applicable)

- [ ] Cardholder data encrypted
- [ ] Secure network configuration
- [ ] Regular vulnerability scans
- [ ] Access control measures
- [ ] Regular security audits

## Penetration Testing Checklist

### Pre-Testing

- [ ] Penetration testing scope defined
- [ ] Authorization obtained
- [ ] Test environment prepared
- [ ] Rules of engagement documented

### Testing Areas

- [ ] Authentication bypass
- [ ] Authorization bypass
- [ ] SQL injection
- [ ] XSS
- [ ] CSRF
- [ ] SSRF
- [ ] File upload vulnerabilities
- [ ] Business logic flaws
- [ ] Session management flaws
- [ ] API security

### Post-Testing

- [ ] Vulnerabilities documented
- [ ] Remediation plan created
- [ ] Fixes implemented
- [ ] Re-testing conducted
- [ ] Report finalized

## Incident Response Checklist

### Preparation

- [ ] Incident response plan documented
- [ ] Incident response team defined
- [ ] Contact information updated
- [ ] Tools and resources available

### Detection

- [ ] Monitoring systems configured
- [ ] Alerts configured
- [ ] Incident detection procedures defined

### Response

- [ ] Incident classification criteria defined
- [ ] Escalation procedures documented
- [ ] Containment procedures defined
- [ ] Eradication procedures defined
- [ ] Recovery procedures defined

### Post-Incident

- [ ] Lessons learned documented
- [ ] Improvements identified
- [ ] Plan updated based on lessons learned

## Security Training Checklist

### Developer Training

- [ ] Secure coding practices training completed
- [ ] OWASP Top 10 training completed
- [ ] Security tools training completed
- [ ] Incident response training completed

### Team Training

- [ ] Security awareness training completed
- [ ] Phishing awareness training completed
- [ ] Incident response training completed

## Approval

- [ ] Security Engineer
- [ ] Tech Lead
- [ ] Project Manager

# Security Engineer

## Role Overview

The Security Engineer ensures application and infrastructure security throughout the SDLC, from design to deployment and operations.

## Responsibilities

- Define security requirements and standards
- Conduct threat modeling and risk assessment
- Review code for security vulnerabilities
- Implement security testing (SAST, DAST)
- Configure security tools and monitoring
- Manage vulnerability remediation
- Ensure compliance with security standards
- Conduct security audits and assessments
- Train team on security best practices

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `security-requirements.md` | Security | Security requirements and standards |
| `threat-model.md` | Security | Threat modeling and risk assessment |
| `security-checklist.md` | Security | Security checklist and validation |

## File Dimensions

### security-requirements.md

**Purpose**: Define security requirements and standards for the application.

**Required Sections**:
- Document metadata (version, authors, date)
- Security objectives
- Authentication and authorization requirements
- Data protection requirements (encryption, masking)
- Input validation requirements
- Session management requirements
- API security requirements
- Infrastructure security requirements
- Compliance requirements (GDPR, SOC2, etc.)
- Security testing requirements

**Quality Gates**:
- [ ] All security requirements are documented
- [ ] Requirements are testable
- [ ] Compliance requirements are identified
- [ ] Team has reviewed and approved

### threat-model.md

**Purpose**: Identify and assess security threats and risks.

**Required Sections**:
- System overview and architecture
- Trust boundaries
- Data flows
- Threat identification (STRIDE model)
- Risk assessment (likelihood, impact, severity)
- Mitigation strategies
- Residual risk
- Security controls
- Recommendations

**Quality Gates**:
- [ ] All components are analyzed
- [ ] Threats are identified and prioritized
- [ ] Mitigation strategies are defined
- [ ] Risks are accepted or mitigated
- [ ] Team has reviewed

### security-checklist.md

**Purpose**: Validate security implementation throughout the SDLC.

**Required Sections**:
- Design review checklist
- Code review checklist (security-focused)
- Deployment checklist
- Monitoring and logging checklist
- Incident response checklist
- Compliance checklist
- Penetration testing checklist
- Security audit checklist
- Remediation tracking

**Quality Gates**:
- [ ] All checklist items are addressed
- [ ] Security issues are resolved
- [ ] Compliance is verified
- [ ] Documentation is complete

## Interaction Patterns

**Inputs From**:
- Solution Architect (architecture design)
- Business Analyst (compliance requirements)
- QA Engineer (security testing results)

**Outputs To**:
- Solution Architect (security requirements)
- Development Team (secure coding guidelines)
- DevOps Engineer (security configurations)

**Review Cycle**:
- Sprint: Security reviews and code analysis
- Release: Security assessment and audit
- Quarterly: Security strategy review

## Tools & Templates

- SAST tools (SonarQube, Semgrep)
- DAST tools (OWASP ZAP, Burp Suite)
- Dependency scanning (Snyk, Dependabot)
- Threat modeling tools

# DevOps Engineer

## Role Overview

The DevOps Engineer manages deployment infrastructure, CI/CD pipelines, and ensures reliable, scalable operations of web applications.

## Responsibilities

- Design and maintain CI/CD pipelines
- Manage cloud infrastructure and deployment
- Implement monitoring and logging
- Ensure system reliability and uptime
- Automate repetitive tasks
- Manage environment configurations
- Implement security best practices
- Coordinate with development on deployments
- Incident response and troubleshooting

## Output Files

| File | Phase | Description |
|------|-------|-------------|
| `deployment-plan.md` | Deployment | Deployment strategy and execution plan |
| `ci-cd-pipeline.md` | Deployment | CI/CD pipeline configuration and documentation |
| `runbook.md` | Deployment | Operational procedures and troubleshooting |

## File Dimensions

### deployment-plan.md

**Purpose**: Define the deployment strategy and execution steps.

**Required Sections**:
- Deployment strategy (blue-green, canary, rolling)
- Environment setup (dev, staging, prod)
- Deployment prerequisites
- Step-by-step deployment procedure
- Rollback procedure
- Post-deployment verification
- Deployment schedule
- Risk assessment
- Communication plan
- Success criteria

**Quality Gates**:
- [ ] Deployment strategy is defined
- [ ] Rollback plan is tested
- [ ] Environments are configured
- [ ] Team has reviewed and approved
- [ ] Success criteria are measurable

### ci-cd-pipeline.md

**Purpose**: Document the CI/CD pipeline configuration and workflow.

**Required Sections**:
- Pipeline stages (build, test, deploy)
- Trigger conditions (push, PR, schedule)
- Build and test configuration
- Code quality checks (linting, security scan)
- Deployment automation
- Environment variables and secrets
- Pipeline monitoring and alerts
- Pipeline optimization
- Troubleshooting guide

**Quality Gates**:
- [ ] Pipeline is automated
- [ ] All checks pass before deployment
- [ ] Secrets are managed securely
- [ ] Pipeline is monitored
- [ ] Team understands workflow

### runbook.md

**Purpose**: Operational procedures for common tasks and incidents.

**Required Sections**:
- System overview and architecture
- Common operational tasks
- Incident response procedures
- Monitoring and alerting setup
- Troubleshooting guides
- Escalation procedures
- Contact information
- Disaster recovery plan
- Backup and restore procedures

**Quality Gates**:
- [ ] All common tasks are documented
- [ ] Incident response is clear
- [ ] Escalation procedures are defined
- [ ] Team has reviewed and practiced
- [ ] Documentation is up-to-date

## Interaction Patterns

**Inputs From**:
- Solution Architect (architecture requirements)
- Full-stack Developer (deployment artifacts)
- Security Engineer (security requirements)

**Outputs To**:
- Full-stack Developer (deployment status)
- Project Manager (deployment schedule)
- Security Engineer (security compliance)

**Review Cycle**:
- Sprint: Pipeline improvements
- Release: Deployment planning and execution
- Monthly: Infrastructure review

## Tools & Templates

- CI/CD tools (GitHub Actions, GitLab CI, Jenkins)
- Infrastructure as Code (Terraform, CloudFormation)
- Monitoring tools (Prometheus, Grafana, Datadog)
- Containerization (Docker, Kubernetes)

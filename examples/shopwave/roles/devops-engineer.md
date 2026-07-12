# ShopWave - DevOps Engineer Role

## Role Overview

**Name**: Alex Kim
**Email**: alex.kim@shopwave.com
**Responsibilities**: Manage infrastructure, CI/CD pipelines, and deployment processes for ShopWave.

## Key Focus Areas

1. **Infrastructure**: AWS setup and management
2. **CI/CD**: Automated testing and deployment
3. **Monitoring**: Application and infrastructure monitoring
4. **Security**: Infrastructure security and compliance

## Business Context

- **Industry/Domain**: Independent e-commerce storefront for handcrafted home goods
- **Project Example**: ShopWave MVP and growth platform
- **Business Goals Supported**: Reliable checkout flow, fast product browsing, protected customer data, fast recovery
- **Stakeholder Value**: Reduces downtime risk and protects revenue and brand trust

## Technical Scope

- **Primary Tech Stack Interactions**: Node.js backend, React frontend, PostgreSQL, Redis, AWS services
- **Key Systems/Services**: ECS, RDS, ElastiCache, S3, CloudFront, CloudWatch
- **Data Domains**: Deployment artifacts, environment configs, metrics, incidents
- **Compliance/Security Boundaries**: AWS IAM, secret management, TLS, PCI-relevant boundaries

## Skill / Tool Mapping

- **MCP Skills**:
  - `vercel-cli-with-tokens` / `deploy` / `deploy-to-vercel` — for deployment workflows if applicable
  - `frontend-ci-cd` — for frontend pipeline configuration
  - `android-ci-cd` — only if mobile/webview delivery is relevant
- **CLI/Runtime Tools**: AWS CLI, Docker, Terraform/CloudFormation, CI platform CLIs
- **When to Use Each**: Infrastructure provisioning, pipeline changes, deployments, and incident response

## Function List

| Function | Inputs | Outputs | Trigger/Cadence |
|----------|--------|---------|-----------------|
| Provision infrastructure | Architecture, environments | AWS resources, configs | Project setup / scaling events |
| Build CI/CD pipeline | Repo, tests, build steps | `ci-cd-pipeline.md`, pipeline | Project setup / updates |
| Plan deployment | Release artifacts | `deployment-plan.md` | Per release |
| Maintain runbooks | Incidents, procedures | `runbook.md` | Continuous refinement |
| Monitor and respond | Metrics, alerts, logs | Incidents, remediations | Ongoing |

## Quality Standards

- **Definition of Done**:
  - Deployment succeeds in staging and production
  - Monitoring and alerts are active
  - Rollback is tested
- **Review Criteria**:
  - Pipeline reliability
  - Deployment risk controls
  - Observability coverage
- **Metrics/Targets**:
  - Deployment frequency
  - Change failure rate
  - Mean time to recover

## Validation Checklist

- **Logic Consistency**:
  - [ ] Pipeline stages align with build/test/deploy requirements
  - [ ] Rollback and recovery steps are documented
- **Technical Accuracy**:
  - [ ] AWS services match ShopWave stack and traffic expectations
  - [ ] Secrets and IAM permissions are least-privilege
- **Business Alignment**:
  - [ ] Deployment cadence supports launch timeline
  - [ ] Performance/reliability targets are supported by infrastructure
- **Tooling/Skill Coverage**:
  - [ ] Deployment and CI/CD skills/tools are mapped
  - [ ] No missing operational workflow

## Output Files for ShopWave

### Deployment Plan
**File**: `deliverables/deployment/deployment-plan.md`

**Strategy**: Blue-green deployment
**Schedule**: Weekly deployments on Thursdays
**Environments**: Development, Staging, Production

**Deployment Steps**:
1. Build and push Docker image
2. Deploy to staging
3. Run smoke tests
4. Manual approval
5. Deploy to production
6. Monitor for 30 minutes

### CI/CD Pipeline
**File**: `deliverables/deployment/ci-cd-pipeline.md`

**Pipeline Stages**:
1. Lint and format check
2. Unit tests
3. Integration tests
4. Build Docker image
5. Security scan
6. Deploy to staging
7. E2E tests
8. Manual approval
9. Deploy to production

### Runbook
**File**: `deliverables/deployment/runbook.md`

**Common Operations**:
- Deploy to production
- Database backup and restore
- Scale application
- Clear cache
- Review logs
- Rotate secrets

## Infrastructure

### AWS Services
- **ECS**: Container orchestration
- **RDS**: PostgreSQL database
- **ElastiCache**: Redis cache
- **S3**: Product image storage
- **CloudFront**: CDN for static assets
- **CloudWatch**: Monitoring and logging

### Environments
- **Development**: Local/Docker Compose
- **Staging**: AWS (single region)
- **Production**: AWS (multi-AZ)

## Current Focus

**Sprint 1**: Set up AWS infrastructure and CI/CD
**Sprint 2**: Configure monitoring and alerting
**Sprint 3**: Optimize costs and performance

## Approval

- [ ] Alex Kim (DevOps Engineer)
- [ ] Jordan Smith (Solution Architect)
- [ ] Morgan Lee (Tech Lead)

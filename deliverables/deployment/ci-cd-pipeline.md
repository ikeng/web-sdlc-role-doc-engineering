# CI/CD Pipeline

## Metadata
- **Version**: 1.0
- **Author**: DevOps Engineer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **CI/CD Tool**: GitHub Actions

## Pipeline Overview

```
┌─────────┐     ┌──────┐     ┌────────┐     ┌─────────┐     ┌──────────┐     ┌──────────┐
│  Code   │────▶│ Lint │────▶│  Test  │────▶│  Build  │────▶│  Deploy  │────▶│  Notify  │
│  Push   │     │      │     │        │     │         │     │ Staging  │     │          │
└─────────┘     └──────┘     └────────┘     └─────────┘     └──────────┘     └──────────┘
                                                                                   │
                                                                                   ▼
                                                                           ┌──────────┐
                                                                           │ Approve │
                                                                           │ Manual  │
                                                                           └────┬─────┘
                                                                                │
                                                                                ▼
                                                                           ┌──────────┐
                                                                           │ Deploy  │
                                                                           │ Prod    │
                                                                           └──────────┘
```

## Pipeline Stages

### Stage 1: Code Quality

**Trigger**: Push to any branch, Pull request

**Steps**:

#### 1.1 Checkout Code
```yaml
- uses: actions/checkout@v3
```

#### 1.2 Setup Node.js
```yaml
- uses: actions/setup-node@v3
  with:
    node-version: '20'
    cache: 'npm'
```

#### 1.3 Install Dependencies
```yaml
- run: npm ci
```

#### 1.4 Lint
```yaml
- run: npm run lint
```

**Checks**:
- ESLint rules
- Prettier formatting
- TypeScript type checking

**Failure Criteria**: Lint errors, formatting issues, type errors

**Duration**: ~2 minutes

---

### Stage 2: Test

**Trigger**: After lint passes

**Steps**:

#### 2.1 Unit Tests
```yaml
- run: npm run test:unit
  env:
    NODE_ENV: test
```

**Coverage**:
- Frontend components
- Backend services
- Utility functions

**Artifacts**: Test coverage report

#### 2.2 Integration Tests
```yaml
- run: npm run test:integration
  env:
    NODE_ENV: test
    DATABASE_URL: ${{ secrets.TEST_DATABASE_URL }}
```

**Coverage**: API endpoints, database interactions

**Artifacts**: Test results

#### 2.3 Upload Coverage
```yaml
- uses: codecov/codecov-action@v3
  with:
    files: ./coverage/lcov.info
    flags: unittests
```

**Failure Criteria**: Test failures, coverage below threshold (80%)

**Duration**: ~5 minutes

---

### Stage 3: Build

**Trigger**: After tests pass

**Steps**:

#### 3.1 Build Frontend
```yaml
- run: npm run build:frontend
```

**Outputs**:
- Optimized static assets
- Source maps
- Build manifest

#### 3.2 Build Backend
```yaml
- run: npm run build:backend
```

**Outputs**:
- Compiled JavaScript
- Docker image

#### 3.3 Build Docker Image
```yaml
- uses: docker/build-push-action@v4
  with:
    context: .
    push: false
    tags: myapp:${{ github.sha }}
    cache-from: type=registry,ref=myapp:buildcache
    cache-to: type=registry,ref=myapp:buildcache,mode=max
```

**Failure Criteria**: Build errors

**Duration**: ~3 minutes

---

### Stage 4: Security Scan

**Trigger**: After build passes

**Steps**:

#### 4.1 Dependency Scan
```yaml
- uses: snyk/actions/node@master
  with:
    args: --severity-threshold=high
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

#### 4.2 SAST Scan
```yaml
- uses: sonarsource/sonarqube-scan-action@master
  with:
    projectBaseDir: .
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

**Failure Criteria**: High/Critical vulnerabilities

**Duration**: ~2 minutes

---

### Stage 5: Deploy to Staging

**Trigger**: After security scan passes, on push to main

**Steps**:

#### 5.1 Deploy to Staging
```yaml
- uses: azure/k8s-deploy@v4
  with:
    namespace: staging
    manifests: k8s/staging/
    images: |
      myapp:${{ github.sha }}
```

#### 5.2 Run Staging Smoke Tests
```yaml
- run: npm run test:smoke -- --env=staging
```

**Failure Criteria**: Deployment errors, smoke test failures

**Duration**: ~5 minutes

---

### Stage 6: Manual Approval (Production)

**Trigger**: After staging deployment passes, on push to main

**Steps**:

#### 6.1 Manual Approval
```yaml
- uses: trstringer/manual-approval@v1
  with:
    secret: ${{ secrets.GITHUB_TOKEN }}
    approvers: tech-lead,product-owner
```

**Timeout**: 1 hour (auto-reject if not approved)

---

### Stage 7: Deploy to Production

**Trigger**: After manual approval

**Steps**:

#### 7.1 Deploy to Green Environment
```yaml
- uses: azure/k8s-deploy@v4
  with:
    namespace: production
    manifests: k8s/green/
    images: |
      myapp:${{ github.sha }}
```

#### 7.2 Run Production Smoke Tests
```yaml
- run: npm run test:smoke -- --env=production
```

#### 7.3 Switch Traffic
```yaml
- run: kubectl patch service myapp -n production -p '{"spec":{"selector":{"version":"green"}}}'
```

**Failure Criteria**: Deployment errors, smoke test failures

**Rollback**: Automatic if errors detected

**Duration**: ~5 minutes

---

### Stage 8: Notify

**Trigger**: After production deployment

**Steps**:

#### 8.1 Slack Notification
```yaml
- uses: slackapi/slack-github-action@v1
  with:
    channel-id: 'deployments'
    slack-message: |
      :white_check_mark: Deployment successful!
      Version: ${{ github.sha }}
      Environment: Production
      Deployed by: ${{ github.actor }}
    token: ${{ secrets.SLACK_TOKEN }}
```

#### 8.2 Update Status Page
```yaml
- run: |
    curl -X POST ${{ secrets.STATUS_PAGE_API }}
      -H "Authorization: Bearer ${{ secrets.STATUS_PAGE_TOKEN }}"
      -d '{"status":"operational"}'
```

## Pipeline Configuration

### Triggers

```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  workflow_dispatch: # Manual trigger
```

### Environment Variables

**Staging**:
- `DATABASE_URL`: `${{ secrets.STAGING_DATABASE_URL }}`
- `REDIS_URL`: `${{ secrets.STAGING_REDIS_URL }}`
- `JWT_SECRET`: `${{ secrets.JWT_SECRET }}`

**Production**:
- `DATABASE_URL`: `${{ secrets.PROD_DATABASE_URL }}`
- `REDIS_URL`: `${{ secrets.PROD_REDIS_URL }}`
- `JWT_SECRET`: `${{ secrets.JWT_SECRET }}`

### Secrets

| Secret | Description | Required |
|--------|-------------|----------|
| `DATABASE_URL` | Database connection string | Yes |
| `REDIS_URL` | Redis connection string | Yes |
| `JWT_SECRET` | JWT signing secret | Yes |
| `SNYK_TOKEN` | Snyk API token | Yes |
| `SONAR_TOKEN` | SonarQube API token | Yes |
| `SLACK_TOKEN` | Slack bot token | Yes |
| `KUBECONFIG` | Kubernetes config | Yes |

## Caching Strategy

### Dependencies
```yaml
- uses: actions/setup-node@v3
  with:
    node-version: '20'
    cache: 'npm'
```

### Docker Layers
```yaml
- uses: docker/build-push-action@v4
  with:
    cache-from: type=registry,ref=myapp:buildcache
    cache-to: type=registry,ref=myapp:buildcache,mode=max
```

**Benefit**: Reduces build time by 50-70%

## Pipeline Monitoring

### Metrics
- Pipeline duration
- Success/failure rate
- Stage duration
- Flaky test detection

### Alerts
- Pipeline failure notification (Slack)
- Deployment failure notification (PagerDuty)
- Performance degradation alert

## Troubleshooting

### Common Issues

**Issue**: Tests fail intermittently
**Solution**: Fix flaky tests, add retry logic

**Issue**: Build takes too long
**Solution**: Optimize Dockerfile, use caching

**Issue**: Deployment fails
**Solution**: Check logs, verify environment variables

**Issue**: Rollback needed
**Solution**: Execute rollback procedure, investigate root cause

## Approval

- [ ] DevOps Engineer
- [ ] Tech Lead

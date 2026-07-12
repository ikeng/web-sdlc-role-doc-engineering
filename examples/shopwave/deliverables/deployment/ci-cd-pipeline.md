# ShopWave - CI/CD Pipeline

## Metadata
- **Version**: 1.0
- **Author**: Alex Kim (DevOps Engineer)
- **Date**: 2026-01-15
- **Project**: ShopWave
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

**Coverage**: Frontend components, backend services, utility functions

#### 2.2 Integration Tests
```yaml
- run: npm run test:integration
  env:
    NODE_ENV: test
    DATABASE_URL: ${{ secrets.TEST_DATABASE_URL }}
```

**Coverage**: API endpoints, database interactions

#### 2.3 Upload Coverage
```yaml
- uses: codecov/codecov-action@v3
  with:
    files: ./coverage/lcov.info
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

#### 3.2 Build Backend
```yaml
- run: npm run build:backend
```

#### 3.3 Build Docker Image
```yaml
- uses: docker/build-push-action@v4
  with:
    context: .
    push: false
    tags: shopwave:${{ github.sha }}
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
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
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
      shopwave:${{ github.sha }}
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

**Timeout**: 1 hour

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
      shopwave:${{ github.sha }}
```

#### 7.2 Run Production Smoke Tests
```yaml
- run: npm run test:smoke -- --env=production
```

#### 7.3 Switch Traffic
```bash
kubectl patch service shopwave -n production -p '{"spec":{"selector":{"version":"green"}}}'
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
    token: ${{ secrets.SLACK_TOKEN }}
```

## Pipeline Configuration

### Triggers

```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

### Environment Variables

**Staging**:
- `DATABASE_URL`: `${{ secrets.STAGING_DATABASE_URL }}`
- `REDIS_URL`: `${{ secrets.STAGING_REDIS_URL }}`
- `JWT_SECRET`: `${{ secrets.JWT_SECRET }}`
- `STRIPE_SECRET_KEY`: `${{ secrets.STRIPE_SECRET_KEY }}`

**Production**:
- `DATABASE_URL`: `${{ secrets.PROD_DATABASE_URL }}`
- `REDIS_URL`: `${{ secrets.PROD_REDIS_URL }}`
- `JWT_SECRET`: `${{ secrets.JWT_SECRET }}`
- `STRIPE_SECRET_KEY`: `${{ secrets.STRIPE_SECRET_KEY }}`

## Caching Strategy

### Dependencies
```yaml
- uses: actions/setup-node@v3
  with:
    node-version: '20'
    cache: 'npm'
```

## Pipeline Monitoring

### Metrics
- Pipeline duration
- Success/failure rate
- Stage duration

### Alerts
- Pipeline failure notification (Slack)
- Deployment failure notification (PagerDuty)

## Approval

- [ ] Alex Kim (DevOps Engineer)
- [ ] Morgan Lee (Tech Lead)

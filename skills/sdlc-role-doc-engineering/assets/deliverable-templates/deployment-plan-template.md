# Deployment Plan Template

## Instructions
Copy this template for each deployment.
Replace all `[placeholder]` text with actual values.
Remove sections marked as `(Optional)` if not applicable.

## Metadata
- **Version**: 1.0
- **Author**: DevOps Engineer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Release Version**: v[X.X.X]
- **Status**: Draft / In Review / Approved

## Deployment Strategy

### Deployment Approach: [Blue-Green / Rolling / Canary / Other]

**Rationale**: [Why this approach was chosen]

**How It Works**: [Brief description of deployment process]

**Alternatives Considered**:
- [Alternative 1]: [Why not chosen]
- [Alternative 2]: [Why not chosen]

### Deployment Schedule

**Target Date**: YYYY-MM-DD
**Deployment Window**: [e.g., 02:00 - 04:00 UTC]
**Estimated Duration**: [e.g., 30 minutes]
**Rollback Window**: [e.g., 30 minutes]

## Pre-Deployment Checklist

### Infrastructure
- [ ] Production environment is ready
- [ ] Database migrations are tested
- [ ] SSL certificates are valid
- [ ] CDN is configured
- [ ] Monitoring and alerting are set up
- [ ] Log aggregation is configured
- [ ] Backup system is operational

### Code
- [ ] All tests pass (unit, integration, E2E)
- [ ] Code review is approved
- [ ] Security scan passes
- [ ] Performance tests pass
- [ ] No critical bugs open
- [ ] Version tag is created

### Documentation
- [ ] Deployment runbook is ready
- [ ] Rollback plan is documented
- [ ] Stakeholders are notified
- [ ] Support team is briefed

### Communication
- [ ] Deployment calendar invite sent
- [ ] Slack/Teams notification scheduled
- [ ] Status page updated (if applicable)

## Deployment Steps

### Step 1: [Step Name] (T-[X] minutes)
**Owner**: [DevOps Engineer]

1. [Action 1]
2. [Action 2]
3. [Action 3]

**Command**:
```bash
[Command or script]
```

**Duration**: [X minutes]

**Validation**:
- [Validation step 1]
- [Validation step 2]

**Rollback**: [Rollback procedure if this step fails]

---

### Step 2: [Step Name] (T-[X] minutes)
**Owner**: [DevOps Engineer]

1. [Action 1]
2. [Action 2]

**Command**:
```bash
[Command or script]
```

**Duration**: [X minutes]

**Validation**:
- [Validation step]

**Rollback**: [Rollback procedure]

---

### Step 3: [Step Name] (T-[X] minutes)
**Owner**: [QA Engineer]

1. [Action 1]
2. [Action 2]

**Duration**: [X minutes]

**Validation**:
- [Validation step]

---

### Step 4: [Step Name] (T-[X] minutes)
**Owner**: [DevOps Engineer]

1. [Action 1]
2. [Action 2]

**Command**:
```bash
[Command or script]
```

**Duration**: [X minutes]

**Validation**:
- [Validation step]

---

### Step 5: Monitor (T+[X] to T+[Y] minutes)
**Owner**: [DevOps Engineer, QA Engineer]

1. Monitor application metrics
2. Check error logs
3. Monitor user feedback
4. Verify all systems are healthy

**Duration**: [X minutes]

**Monitoring Dashboard**:
- Application metrics (CPU, memory, requests)
- Error rates
- Response times
- Database performance
- Cache hit rate

## Rollback Plan

### When to Rollback
- Error rate > 5%
- Critical functionality broken
- Performance degradation > 50%
- Security vulnerability discovered

### Rollback Procedure

**Step 1: [Rollback Action] (1 minute)**
```bash
[Rollback command]
```

**Step 2: Verify Rollback (2 minutes)**
```bash
[Verification command]
```

**Step 3: Notify Team**
- Post in #deployments channel
- Update status page
- Notify stakeholders

**Step 4: Investigate**
- Review logs
- Identify root cause
- Fix issues before retry

## Post-Deployment

### Immediate (T+[X] to T+[Y] hours)
- [ ] Monitor application metrics
- [ ] Check error logs
- [ ] Respond to user feedback
- [ ] Verify all features working

### Short-term (T+[Y] to T+[Z] hours)
- [ ] Continue monitoring
- [ ] Review performance metrics
- [ ] Check database performance
- [ ] Verify backup systems

### Long-term (T+[Z] to T+[W] days)
- [ ] Decommission old environment
- [ ] Review deployment process
- [ ] Document lessons learned
- [ ] Update runbooks

## Emergency Contacts

| Role | Name | Phone | Email |
|------|------|-------|-------|
| DevOps Lead | [Name] | [Phone] | [Email] |
| Tech Lead | [Name] | [Phone] | [Email] |
| QA Lead | [Name] | [Phone] | [Email] |
| Product Owner | [Name] | [Phone] | [Email] |

## Quality Gates

- [ ] Deployment strategy is defined
- [ ] Rollback plan is tested
- [ ] Environments are configured
- [ ] Team has reviewed and approved
- [ ] Success criteria are measurable

## Approval

- [ ] DevOps Engineer
- [ ] Tech Lead
- [ ] QA Engineer
- [ ] Product Owner

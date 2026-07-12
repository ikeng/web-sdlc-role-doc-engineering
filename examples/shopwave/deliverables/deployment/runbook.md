# ShopWave - Runbook

## Metadata
- **Version**: 1.0
- **Author**: Alex Kim (DevOps Engineer)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Last Updated**: 2026-01-15

## System Overview

### Architecture
- **Frontend**: React app deployed on Vercel
- **Backend**: Node.js API deployed on AWS ECS
- **Database**: PostgreSQL on AWS RDS
- **Cache**: Redis on AWS ElastiCache
- **CDN**: CloudFront

### Environments
- **Production**: https://shopwave.com
- **Staging**: https://staging.shopwave.com
- **Development**: http://localhost:3000

### Key Components
- Load Balancer: AWS ALB
- Web Servers: AWS ECS (2 instances)
- Database: AWS RDS PostgreSQL (primary + 1 read replica)
- Cache: AWS ElastiCache Redis
- Storage: AWS S3 + CloudFront CDN

## Common Operational Tasks

### 1. Deploy to Production

**Frequency**: As needed (typically weekly)

**Steps**:
1. Ensure all tests pass in CI/CD
2. Get approval from Tech Lead
3. Merge PR to main branch
4. Monitor CI/CD pipeline
5. Verify deployment in staging
6. Deploy to production (blue-green deployment)
7. Monitor production metrics for 30 minutes

**Expected Duration**: 30-45 minutes

**Rollback**: If issues detected, switch traffic back to blue environment

**Contacts**: Morgan Lee (Tech Lead), Alex Kim (DevOps)

---

### 2. Database Backup

**Frequency**: Daily (automated)

**Steps**:
1. Verify automated backup is running
2. Check backup completion status
3. Verify backup file exists in S3

**Automated**: AWS RDS automated backups (daily, 7-day retention)

**Manual Backup**:
```bash
pg_dump -h prod-db.shopwave.com -U postgres shopwave > backup_$(date +%Y%m%d).sql
aws s3 cp backup_*.sql s3://shopwave-backups/
```

**Expected Duration**: 5-10 minutes (automated)

---

### 3. Database Restore

**Frequency**: As needed (disaster recovery)

**Steps**:
1. Notify team of restore operation
2. Put application in maintenance mode
3. Create new RDS instance from backup
4. Update application configuration
5. Verify data integrity
6. Bring application back online

**Expected Duration**: 30-60 minutes

**Contacts**: Alex Kim (DevOps), Jordan Smith (Architect)

---

### 4. Scale Application

**Frequency**: As needed (traffic spikes)

**Steps**:
1. Monitor current metrics (CPU, memory, request rate)
2. Determine scaling requirements
3. Update ECS service desired count
4. Monitor scaling progress

**Commands**:
```bash
aws ecs update-service --cluster production --service shopwave --desired-count 4
```

**Expected Duration**: 5 minutes

**Contacts**: Alex Kim (DevOps)

---

### 5. Clear Cache

**Frequency**: As needed (data inconsistency)

**Steps**:
1. Identify cache key or pattern to clear
2. Connect to Redis
3. Delete cache entries

**Commands**:
```bash
redis-cli -h prod-redis.shopwave.com
DEL cart:user:123
```

**Expected Duration**: 1-2 minutes

**Contacts**: Alex Kim (DevOps), Riley Chen (Developer)

---

### 6. Review Logs

**Frequency**: Daily (monitoring), As needed (incidents)

**Steps**:
1. Access CloudWatch Logs
2. Filter by log group and time range
3. Search for errors or specific patterns

**CloudWatch Logs Insights Query**:
```
fields @timestamp, @message, level
| filter level = "ERROR"
| sort @timestamp desc
| limit 100
```

**Expected Duration**: 5-15 minutes

**Contacts**: Alex Kim (DevOps), Riley Chen (Developer)

---

### 7. Rotate Secrets

**Frequency**: Quarterly (security best practice)

**Steps**:
1. Generate new secret
2. Update secret in AWS Secrets Manager
3. Update application configuration
4. Restart application pods
5. Verify application works with new secret
6. Revoke old secret

**Expected Duration**: 15 minutes

**Contacts**: Riley Park (Security Engineer), Alex Kim (DevOps)

---

## Incident Response

### Incident Severity Levels

**P0 - Critical** (System Down)
- Complete system outage
- Data loss
- Security breach
- Response time: Immediate

**P1 - High** (Major Feature Broken)
- Core functionality broken
- Significant user impact
- Response time: < 30 minutes

**P2 - Medium** (Minor Issue)
- Non-critical feature broken
- Limited user impact
- Response time: < 2 hours

**P3 - Low** (Cosmetic)
- UI/UX issues
- Minimal user impact
- Response time: < 24 hours

### Incident Response Procedure

1. **Detect**: Alert triggered, incident identified
2. **Assess**: Gather information, determine severity
3. **Mitigate**: Implement fix or workaround
4. **Resolve**: Identify root cause, implement permanent fix
5. **Review**: Post-incident review, document lessons learned

### Escalation Matrix

| Severity | First Response | Escalation 1 | Escalation 2 |
|----------|---------------|--------------|--------------|
| P0 | On-call Engineer | Tech Lead | Engineering Manager |
| P1 | On-call Engineer | Tech Lead | Engineering Manager |
| P2 | On-call Engineer | Tech Lead | - |
| P3 | On-call Engineer | - | - |

## Troubleshooting Guide

### Issue: High Error Rate

**Symptoms**: Error rate > 5%, 5xx errors in logs

**Diagnosis**:
1. Check CloudWatch metrics for error rate
2. Review error logs for patterns
3. Check application health
4. Verify database connectivity

**Resolution**:
1. If database issue: Check RDS status, connections
2. If application issue: Check app logs, restart pods
3. If external dependency: Check service status

---

### Issue: Slow Performance

**Symptoms**: Response time > 2s, high latency

**Diagnosis**:
1. Check CloudWatch metrics for latency
2. Review slow query logs
3. Check database connections
4. Review application logs

**Resolution**:
1. If database issue: Optimize queries, add indexes
2. If application issue: Profile code, optimize algorithms
3. If cache issue: Check Redis hit rate, scale cache

---

### Issue: Database Connection Exhausted

**Symptoms**: Database connection errors, timeouts

**Diagnosis**:
1. Check current connections
2. Check connection pool settings
3. Review application logs for connection leaks

**Resolution**:
1. Kill idle connections
2. Scale up database instance
3. Fix connection leaks in application

---

## Backup & Recovery

### Backup Strategy
- **Database**: Daily automated backups (7-day retention)
- **Application Code**: Git repository (GitHub)
- **Configuration**: Git repository (Infrastructure as Code)
- **Secrets**: AWS Secrets Manager

### Recovery Procedures

**Database Recovery**:
1. Create new RDS instance from backup
2. Update application configuration
3. Verify data integrity
4. Switch traffic to new instance

**RTO (Recovery Time Objective)**: 1 hour
**RPO (Recovery Point Objective)**: 15 minutes

## Emergency Contacts

| Role | Name | Phone | Email |
|------|------|-------|-------|
| DevOps Lead | Alex Kim | +1-555-0123 | alex.kim@shopwave.com |
| Tech Lead | Morgan Lee | +1-555-0124 | morgan@shopwave.com |
| QA Lead | Quinn Brooks | +1-555-0125 | quinn@shopwave.com |
| Product Owner | Alex Rivera | +1-555-0126 | alex@shopwave.com |
| Security Engineer | Riley Park | +1-555-0127 | riley.park@shopwave.com |

## Approval

- [ ] Alex Kim (DevOps Engineer)
- [ ] Morgan Lee (Tech Lead)
- [ ] Riley Park (Security Engineer)

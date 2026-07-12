# Runbook

## Metadata
- **Version**: 1.0
- **Author**: DevOps Engineer
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Last Updated**: YYYY-MM-DD

## System Overview

### Architecture
- **Frontend**: React app deployed on Vercel
- **Backend**: Node.js API deployed on AWS ECS
- **Database**: PostgreSQL on AWS RDS
- **Cache**: Redis on AWS ElastiCache
- **CDN**: CloudFront

### Environments
- **Production**: https://app.example.com
- **Staging**: https://staging.app.example.com
- **Development**: http://localhost:3000

### Key Components
- Load Balancer: AWS ALB
- Web Servers: AWS ECS (3 instances)
- Database: AWS RDS PostgreSQL (primary + 2 read replicas)
- Cache: AWS ElastiCache Redis (cluster mode)
- Storage: AWS S3 + CloudFront CDN

## Common Operational Tasks

### 1. Deploy to Production

**Frequency**: As needed (typically 2-3 times per week)

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

**Contacts**: Tech Lead, DevOps Engineer

---

### 2. Database Backup

**Frequency**: Daily (automated)

**Steps**:
1. Verify automated backup is running
2. Check backup completion status
3. Verify backup file exists in S3
4. Test restore procedure monthly

**Automated**: AWS RDS automated backups (daily, 7-day retention)

**Manual Backup**:
```bash
pg_dump -h prod-db.example.com -U postgres myapp > backup_$(date +%Y%m%d).sql
aws s3 cp backup_*.sql s3://myapp-backups/
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

**Commands**:
```bash
# Restore from backup
pg_restore -h new-db.example.com -U postgres -d myapp backup_20260115.sql

# Verify data
psql -h new-db.example.com -U postgres -d myapp -c "SELECT COUNT(*) FROM users;"
```

**Expected Duration**: 30-60 minutes

**Contacts**: DevOps Engineer, DBA

---

### 4. Scale Application

**Frequency**: As needed (traffic spikes)

**Steps**:
1. Monitor current metrics (CPU, memory, request rate)
2. Determine scaling requirements
3. Update ECS service desired count
4. Monitor scaling progress
5. Verify performance improvement

**Commands**:
```bash
# Scale up
aws ecs update-service --cluster production --service myapp --desired-count 5

# Scale down
aws ecs update-service --cluster production --service myapp --desired-count 3
```

**Expected Duration**: 5 minutes

**Contacts**: DevOps Engineer

---

### 5. Clear Cache

**Frequency**: As needed (data inconsistency)

**Steps**:
1. Identify cache key or pattern to clear
2. Connect to Redis
3. Delete cache entries
4. Verify cache is cleared

**Commands**:
```bash
# Connect to Redis
redis-cli -h prod-redis.example.com

# Clear specific key
DEL user:123

# Clear pattern
redis-cli --scan --pattern "user:*" | xargs redis-cli DEL

# Clear all (use with caution)
FLUSHDB
```

**Expected Duration**: 1-2 minutes

**Contacts**: DevOps Engineer, Backend Developer

---

### 6. Review Logs

**Frequency**: Daily (monitoring), As needed (incidents)

**Steps**:
1. Access CloudWatch Logs
2. Filter by log group and time range
3. Search for errors or specific patterns
4. Export logs if needed for analysis

**CloudWatch Logs Insights Query**:
```
fields @timestamp, @message, level
| filter level = "ERROR"
| sort @timestamp desc
| limit 100
```

**Expected Duration**: 5-15 minutes

**Contacts**: DevOps Engineer, Developer

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

**Commands**:
```bash
# Generate new JWT secret
openssl rand -base64 32

# Update in AWS Secrets Manager
aws secretsmanager update-secret --secret-id jwt-secret --secret-string "new_secret"

# Restart pods
kubectl rollout restart deployment/myapp -n production
```

**Expected Duration**: 15 minutes

**Contacts**: Security Engineer, DevOps Engineer

---

## Incident Response

### Incident Severity Levels

**P0 - Critical** (System Down)
- Complete system outage
- Data loss
- Security breach
- Response time: Immediate
- Notification: All hands

**P1 - High** (Major Feature Broken)
- Core functionality broken
- Significant user impact
- Response time: < 30 minutes
- Notification: Engineering team

**P2 - Medium** (Minor Issue)
- Non-critical feature broken
- Limited user impact
- Response time: < 2 hours
- Notification: On-call engineer

**P3 - Low** (Cosmetic)
- UI/UX issues
- Minimal user impact
- Response time: < 24 hours
- Notification: Next business day

### Incident Response Procedure

**Step 1: Detect** (0-5 minutes)
- Alert triggered in CloudWatch/PagerDuty
- On-call engineer acknowledges alert
- Initial assessment of severity

**Step 2: Assess** (5-15 minutes)
- Gather information (logs, metrics, user reports)
- Determine impact and scope
- Classify severity level
- Escalate if needed

**Step 3: Mitigate** (15-60 minutes)
- Implement immediate fix or workaround
- Rollback if necessary
- Communicate status to stakeholders
- Document actions taken

**Step 4: Resolve** (1-4 hours)
- Identify root cause
- Implement permanent fix
- Test fix in staging
- Deploy to production

**Step 5: Review** (24-48 hours)
- Post-incident review meeting
- Document incident timeline
- Identify improvements
- Update runbooks

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
5. Check external dependencies

**Resolution**:
1. If database issue: Check RDS status, connections
2. If application issue: Check app logs, restart pods
3. If external dependency: Check service status, implement fallback
4. If traffic spike: Scale up application

**Prevention**: Implement circuit breakers, rate limiting

---

### Issue: Slow Performance

**Symptoms**: Response time > 2s, high latency

**Diagnosis**:
1. Check CloudWatch metrics for latency
2. Review slow query logs
3. Check database connections
4. Review application logs
5. Check CDN performance

**Resolution**:
1. If database issue: Optimize queries, add indexes
2. If application issue: Profile code, optimize algorithms
3. If cache issue: Check Redis hit rate, scale cache
4. If CDN issue: Check cache hit rate, purge cache

**Prevention**: Database query optimization, caching strategy

---

### Issue: Database Connection Exhausted

**Symptoms**: Database connection errors, timeouts

**Diagnosis**:
1. Check current connections: `SELECT count(*) FROM pg_stat_activity;`
2. Check connection pool settings
3. Review application logs for connection leaks
4. Check for long-running queries

**Resolution**:
1. Kill idle connections: `SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state = 'idle';`
2. Scale up database instance
3. Fix connection leaks in application
4. Optimize long-running queries

**Prevention**: Connection pooling, query optimization

---

### Issue: High Memory Usage

**Symptoms**: Pods restarted, OOMKilled errors

**Diagnosis**:
1. Check pod metrics in CloudWatch
2. Review application logs for memory leaks
3. Check for large data processing
4. Review recent deployments

**Resolution**:
1. Increase memory limits
2. Fix memory leaks
3. Implement pagination for large datasets
4. Use streaming for large files

**Prevention**: Memory profiling, load testing

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

**Application Recovery**:
1. Redeploy from previous stable version
2. Verify health checks pass
3. Switch traffic to new deployment

**Full Disaster Recovery**:
1. Restore database from backup
2. Redeploy application
3. Update DNS/load balancer
4. Verify all systems operational

**RTO (Recovery Time Objective)**: 1 hour
**RPO (Recovery Point Objective)**: 15 minutes

## Disaster Recovery

### Disaster Recovery Plan

**Scenario 1: Complete Region Outage**
1. Activate secondary region (us-west-2)
2. Restore database from backup in secondary region
3. Deploy application to secondary region
4. Update DNS to point to secondary region
5. Notify users of temporary service degradation

**Scenario 2: Data Corruption**
1. Stop application writes
2. Restore database from last known good backup
3. Replay transactions from backup to current (if available)
4. Verify data integrity
5. Resume normal operations

**Scenario 3: Security Breach**
1. Isolate affected systems
2. Preserve evidence (logs, snapshots)
3. Notify security team
4. Rotate all secrets
5. Deploy patched version
6. Conduct post-incident analysis

## Maintenance Windows

### Scheduled Maintenance
- **Frequency**: Monthly (first Sunday, 02:00-04:00 UTC)
- **Activities**: Security patches, dependency updates, infrastructure maintenance
- **Notification**: 1 week advance notice to users

### Emergency Maintenance
- **Notification**: As soon as possible
- **Duration**: As needed
- **Rollback**: Always available

## Approval

- [ ] DevOps Engineer
- [ ] Tech Lead
- [ ] Security Engineer

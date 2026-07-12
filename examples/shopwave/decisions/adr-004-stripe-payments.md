# ADR-004: Use Stripe for Payment Processing

## Status
Accepted

## Date
2026-01-12

## Context
We need to choose a payment processor for the ShopWave platform.

## Decision
We will use Stripe for payment processing.

## Rationale
- **Developer experience**: Excellent API and documentation
- **Security**: PCI DSS compliant, handles sensitive data
- **Features**: Supports subscriptions, refunds, disputes
- **International**: Supports multiple currencies and countries
- **Fees**: Competitive pricing (2.9% + $0.30 per transaction)

## Alternatives Considered
- **PayPal**: Wider adoption, but more complex integration
- **Square**: Good for in-person, less suited for online
- **Braintree**: PayPal's service, more complex

## Consequences
- **Positive**: Easy integration, secure, feature-rich
- **Negative**: Additional dependency, fees per transaction

## Approval
- [ ] Alex Rivera (Product Owner)
- [ ] Morgan Lee (Tech Lead)
- [ ] Riley Park (Security Engineer)

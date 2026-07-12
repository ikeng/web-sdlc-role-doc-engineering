# API Design

## Metadata
- **Version**: 1.0
- **Author**: Solution Architect
- **Date**: YYYY-MM-DD
- **Project**: [Project Name]
- **Status**: Draft / In Review / Approved

## API Overview

### API Type
RESTful API with JSON payloads

### Base URL
- **Production**: `https://api.example.com/v1`
- **Staging**: `https://api-staging.example.com/v1`
- **Development**: `http://localhost:3000/api/v1`

### Authentication
All endpoints (except public ones) require authentication via JWT Bearer token:
```
Authorization: Bearer <access_token>
```

### Rate Limiting
- **Authenticated**: 100 requests/minute
- **Unauthenticated**: 20 requests/minute
- **Rate Limit Headers**:
  - `X-RateLimit-Limit`: Request limit
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Time when limit resets (Unix timestamp)

### Versioning
- URL path versioning: `/v1/`, `/v2/`
- Breaking changes require new version
- Non-breaking changes can be deployed to current version

### Error Responses
All errors follow this format:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable error message",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

**HTTP Status Codes**:
- `200 OK`: Successful GET, PUT, PATCH
- `201 Created`: Successful POST
- `204 No Content`: Successful DELETE
- `400 Bad Request`: Invalid request body/parameters
- `401 Unauthorized`: Missing or invalid authentication
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `409 Conflict`: Resource conflict (e.g., duplicate email)
- `422 Unprocessable Entity`: Validation error
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error
- `503 Service Unavailable`: Service temporarily unavailable

## Endpoints

### Authentication

#### POST /auth/register
Register a new user account.

**Request**:
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "name": "John Doe"
}
```

**Validation**:
- `email`: Required, valid email format
- `password`: Required, min 8 chars, must contain uppercase, lowercase, number, special char
- `name`: Required, min 2 chars

**Response 201**:
```json
{
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe",
    "accessToken": "jwt_token",
    "refreshToken": "refresh_token"
  }
}
```

**Error Responses**:
- `409`: Email already registered
- `422`: Validation error

---

#### POST /auth/login
Authenticate user and receive tokens.

**Request**:
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response 200**:
```json
{
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe",
    "accessToken": "jwt_token",
    "refreshToken": "refresh_token"
  }
}
```

**Error Responses**:
- `401`: Invalid credentials
- `422`: Validation error

---

#### POST /auth/refresh
Refresh access token using refresh token.

**Request**:
```json
{
  "refreshToken": "refresh_token"
}
```

**Response 200**:
```json
{
  "data": {
    "accessToken": "new_jwt_token",
    "refreshToken": "new_refresh_token"
  }
}
```

**Error Responses**:
- `401`: Invalid refresh token

---

#### POST /auth/logout
Invalidate refresh token.

**Request**:
```json
{
  "refreshToken": "refresh_token"
}
```

**Response 204**: No content

---

#### POST /auth/forgot-password
Request password reset email.

**Request**:
```json
{
  "email": "user@example.com"
}
```

**Response 204**: No content

**Note**: Always returns 204 to prevent email enumeration

---

#### POST /auth/reset-password
Reset password using token from email.

**Request**:
```json
{
  "token": "reset_token",
  "password": "NewSecurePass123!"
}
```

**Response 204**: No content

---

### Users

#### GET /users/me
Get current user profile.

**Authentication**: Required

**Response 200**:
```json
{
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe",
    "createdAt": "2026-01-01T00:00:00Z",
    "updatedAt": "2026-01-01T00:00:00Z"
  }
}
```

---

#### PATCH /users/me
Update current user profile.

**Authentication**: Required

**Request**:
```json
{
  "name": "John Smith",
  "email": "john.smith@example.com"
}
```

**Validation**:
- `name`: Optional, min 2 chars
- `email`: Optional, valid email format

**Response 200**:
```json
{
  "data": {
    "id": "uuid",
    "email": "john.smith@example.com",
    "name": "John Smith",
    "createdAt": "2026-01-01T00:00:00Z",
    "updatedAt": "2026-01-15T00:00:00Z"
  }
}
```

---

### Products

#### GET /products
List products with pagination and filtering.

**Authentication**: Optional (public endpoint)

**Query Parameters**:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)
- `category`: Filter by category ID
- `search`: Search in product name/description
- `minPrice`: Minimum price filter
- `maxPrice`: Maximum price filter
- `sort`: Sort field (name, price, createdAt)
- `order`: Sort order (asc, desc)

**Response 200**:
```json
{
  "data": [
    {
      "id": "uuid",
      "name": "Product Name",
      "description": "Product description",
      "price": 29.99,
      "imageUrl": "https://cdn.example.com/image.jpg",
      "category": {
        "id": "uuid",
        "name": "Category Name"
      },
      "createdAt": "2026-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

---

#### GET /products/:id
Get product details.

**Authentication**: Optional

**Response 200**:
```json
{
  "data": {
    "id": "uuid",
    "name": "Product Name",
    "description": "Detailed product description",
    "price": 29.99,
    "inventoryCount": 100,
    "imageUrl": "https://cdn.example.com/image.jpg",
    "images": [
      "https://cdn.example.com/image1.jpg",
      "https://cdn.example.com/image2.jpg"
    ],
    "category": {
      "id": "uuid",
      "name": "Category Name"
    },
    "attributes": {
      "color": "Blue",
      "size": "Medium",
      "weight": "1.5kg"
    },
    "createdAt": "2026-01-01T00:00:00Z",
    "updatedAt": "2026-01-15T00:00:00Z"
  }
}
```

**Error Responses**:
- `404`: Product not found

---

#### POST /products
Create a new product (Admin only).

**Authentication**: Required (Admin role)

**Request**:
```json
{
  "name": "New Product",
  "description": "Product description",
  "price": 29.99,
  "inventoryCount": 100,
  "categoryId": "category_uuid",
  "images": ["https://cdn.example.com/image.jpg"],
  "attributes": {
    "color": "Blue",
    "size": "Medium"
  }
}
```

**Response 201**:
```json
{
  "data": {
    "id": "uuid",
    "name": "New Product",
    "description": "Product description",
    "price": 29.99,
    "inventoryCount": 100,
    "categoryId": "category_uuid",
    "images": ["https://cdn.example.com/image.jpg"],
    "attributes": {
      "color": "Blue",
      "size": "Medium"
    },
    "createdAt": "2026-01-15T00:00:00Z"
  }
}
```

---

#### PATCH /products/:id
Update a product (Admin only).

**Authentication**: Required (Admin role)

**Request**:
```json
{
  "name": "Updated Product Name",
  "price": 39.99
}
```

**Response 200**: Updated product object

---

#### DELETE /products/:id
Delete a product (Admin only).

**Authentication**: Required (Admin role)

**Response 204**: No content

---

### Orders

#### GET /orders
List user's orders.

**Authentication**: Required

**Query Parameters**:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20)
- `status`: Filter by status (pending, processing, shipped, delivered)

**Response 200**:
```json
{
  "data": [
    {
      "id": "uuid",
      "status": "processing",
      "totalAmount": 59.98,
      "items": [
        {
          "productId": "uuid",
          "productName": "Product Name",
          "quantity": 2,
          "price": 29.99
        }
      ],
      "createdAt": "2026-01-15T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 5,
    "totalPages": 1
  }
}
```

---

#### POST /orders
Create a new order.

**Authentication**: Required

**Request**:
```json
{
  "items": [
    {
      "productId": "uuid",
      "quantity": 2
    }
  ],
  "shippingAddress": {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip": "10001",
    "country": "US"
  },
  "paymentMethodId": "payment_method_id"
}
```

**Response 201**:
```json
{
  "data": {
    "id": "uuid",
    "userId": "uuid",
    "status": "pending",
    "totalAmount": 59.98,
    "items": [...],
    "shippingAddress": {...},
    "createdAt": "2026-01-15T00:00:00Z"
  }
}
```

**Error Responses**:
- `400`: Insufficient inventory
- `422`: Validation error

---

## Data Models

### User
```typescript
{
  id: string; // UUID
  email: string;
  name: string;
  role: "user" | "admin";
  createdAt: Date;
  updatedAt: Date;
}
```

### Product
```typescript
{
  id: string; // UUID
  name: string;
  description: string;
  price: number;
  inventoryCount: number;
  categoryId: string;
  images: string[];
  attributes: Record<string, string>;
  createdAt: Date;
  updatedAt: Date;
}
```

### Order
```typescript
{
  id: string; // UUID
  userId: string;
  status: "pending" | "processing" | "shipped" | "delivered" | "cancelled" | "refunded";
  totalAmount: number;
  items: OrderItem[];
  shippingAddress: Address;
  createdAt: Date;
  updatedAt: Date;
}

type OrderItem = {
  productId: string;
  productName: string;
  quantity: number;
  price: number;
};

type Address = {
  street: string;
  city: string;
  state: string;
  zip: string;
  country: string;
};
```

## Security Considerations

- All endpoints require authentication except public ones
- Passwords never returned in API responses
- Sensitive fields (password_hash, refresh_tokens) never exposed
- Rate limiting on all endpoints
- Input validation on all requests
- SQL injection prevented via parameterized queries
- XSS prevented via input sanitization

## Performance Considerations

- Pagination on all list endpoints
- Caching headers on static/rarely-changing data
- Database query optimization (indexes, eager loading)
- Response compression (gzip)
- CDN for static assets

## Approval

- [ ] Solution Architect
- [ ] Tech Lead
- [ ] Security Engineer

# ShopWave - API Design

## Metadata
- **Version**: 1.0
- **Author**: Jordan Smith (Solution Architect)
- **Date**: 2026-01-15
- **Project**: ShopWave
- **Status**: Approved

## API Overview

### API Type
RESTful API with JSON payloads

### Base URL
- **Production**: `https://api.shopwave.com/v1`
- **Staging**: `https://api-staging.shopwave.com/v1`
- **Development**: `http://localhost:3000/api/v1`

### Authentication
All endpoints (except public ones) require authentication via JWT Bearer token:
```
Authorization: Bearer <access_token>
```

### Rate Limiting
- **Authenticated**: 100 requests/minute
- **Unauthenticated**: 20 requests/minute

### Versioning
URL path versioning: `/v1/`

### Error Responses
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

## Endpoints

### Authentication

#### POST /auth/register
Register a new user.

**Request**:
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "name": "John Doe"
}
```

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
Authenticate user.

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

---

### Products

#### GET /products
List products with pagination and filtering.

**Authentication**: Optional

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
      "name": "Handcrafted Ceramic Vase",
      "description": "Beautiful ceramic vase...",
      "price": 45.00,
      "imageUrl": "https://cdn.shopwave.com/image.jpg",
      "artisan": {
        "id": "uuid",
        "name": "Jane's Ceramics"
      },
      "category": {
        "id": "uuid",
        "name": "Ceramics"
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
    "name": "Handcrafted Ceramic Vase",
    "description": "Detailed product description",
    "price": 45.00,
    "inventoryCount": 10,
    "imageUrl": "https://cdn.shopwave.com/image.jpg",
    "images": [
      "https://cdn.shopwave.com/image1.jpg",
      "https://cdn.shopwave.com/image2.jpg"
    ],
    "artisan": {
      "id": "uuid",
      "name": "Jane's Ceramics",
      "story": "Jane has been crafting ceramics for 10 years..."
    },
    "category": {
      "id": "uuid",
      "name": "Ceramics"
    },
    "materials": ["Clay", "Non-toxic glaze"],
    "dimensions": "8x8x12 inches",
    "createdAt": "2026-01-01T00:00:00Z"
  }
}
```

**Error Responses**:
- `404`: Product not found

---

#### POST /products
Create a new product (Admin/Artisan only).

**Authentication**: Required

**Request**:
```json
{
  "name": "Handcrafted Ceramic Vase",
  "description": "Beautiful ceramic vase",
  "price": 45.00,
  "inventoryCount": 10,
  "categoryId": "category_uuid",
  "images": ["https://cdn.shopwave.com/image.jpg"],
  "materials": ["Clay", "Non-toxic glaze"],
  "dimensions": "8x8x12 inches"
}
```

**Response 201**: Created product object

---

### Cart

#### GET /cart
Get current user's cart.

**Authentication**: Required

**Response 200**:
```json
{
  "data": {
    "items": [
      {
        "id": "uuid",
        "productId": "uuid",
        "productName": "Handcrafted Ceramic Vase",
        "productImage": "https://cdn.shopwave.com/image.jpg",
        "price": 45.00,
        "quantity": 2,
        "subtotal": 90.00
      }
    ],
    "subtotal": 90.00,
    "tax": 7.20,
    "total": 97.20
  }
}
```

---

#### POST /cart/items
Add item to cart.

**Authentication**: Required

**Request**:
```json
{
  "productId": "uuid",
  "quantity": 1
}
```

**Response 201**: Updated cart object

**Error Responses**:
- `400`: Insufficient inventory
- `404`: Product not found

---

#### PATCH /cart/items/:itemId
Update cart item quantity.

**Authentication**: Required

**Request**:
```json
{
  "quantity": 3
}
```

**Response 200**: Updated cart object

---

#### DELETE /cart/items/:itemId
Remove item from cart.

**Authentication**: Required

**Response 204**: No content

---

### Orders

#### POST /checkout
Create order from cart.

**Authentication**: Required

**Request**:
```json
{
  "shippingAddress": {
    "fullName": "John Doe",
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip": "10001",
    "country": "US"
  },
  "paymentMethodId": "pm_card_visa"
}
```

**Response 201**:
```json
{
  "data": {
    "id": "uuid",
    "status": "pending",
    "totalAmount": 97.20,
    "items": [...],
    "shippingAddress": {...},
    "createdAt": "2026-01-15T00:00:00Z"
  }
}
```

**Error Responses**:
- `400`: Insufficient inventory
- `402`: Payment failed
- `422`: Validation error

---

#### GET /orders
List user's orders.

**Authentication**: Required

**Query Parameters**:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20)

**Response 200**:
```json
{
  "data": [
    {
      "id": "uuid",
      "status": "shipped",
      "totalAmount": 97.20,
      "items": [...],
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

#### GET /orders/:id
Get order details.

**Authentication**: Required

**Response 200**: Order object with items, shipping, tracking

**Error Responses**:
- `404`: Order not found

---

## Data Models

### User
```typescript
{
  id: string;
  email: string;
  name: string;
  role: "customer" | "artisan" | "admin";
  createdAt: Date;
  updatedAt: Date;
}
```

### Product
```typescript
{
  id: string;
  name: string;
  description: string;
  price: number;
  inventoryCount: number;
  artisanId: string;
  categoryId: string;
  images: string[];
  materials: string[];
  dimensions: string;
  createdAt: Date;
  updatedAt: Date;
}
```

### Cart
```typescript
{
  id: string;
  userId: string;
  items: CartItem[];
  subtotal: number;
  tax: number;
  total: number;
}

type CartItem = {
  id: string;
  productId: string;
  quantity: number;
  price: number;
};
```

### Order
```typescript
{
  id: string;
  userId: string;
  status: "pending" | "processing" | "shipped" | "delivered" | "cancelled";
  totalAmount: number;
  items: OrderItem[];
  shippingAddress: Address;
  createdAt: Date;
  updatedAt: Date;
};

type OrderItem = {
  productId: string;
  productName: string;
  quantity: number;
  price: number;
};

type Address = {
  fullName: string;
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
- Rate limiting on all endpoints
- Input validation on all requests
- SQL injection prevented via parameterized queries

## Performance Considerations

- Pagination on all list endpoints
- Caching headers on static/rarely-changing data
- Database query optimization (indexes)
- Response compression (gzip)
- CDN for static assets

## Approval

- [ ] Jordan Smith (Solution Architect)
- [ ] Morgan Lee (Tech Lead)
- [ ] Riley Park (Security Engineer)

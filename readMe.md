# Production REST API Architecture with FastAPI, SQLAlchemy & JWT ⚡

[![Framework: FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![ORM: SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Validation: Pydantic](https://img.shields.io/badge/Validation-Pydantic-E92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Auth: OAuth2 JWT](https://img.shields.io/badge/Auth-OAuth2_JWT_Bearer-000000?logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> A modular, production-ready REST API reference implementation built on FastAPI, demonstrating clean layered architecture (Repository Pattern), SQLAlchemy ORM session lifecycle management, Pydantic validation contracts, and OAuth2 JWT authentication.

---

## 🏛️ Layered Architectural Design

```text
+-----------------------------------------------------------------------------------------+
|                               API LAYER & DEPENDENCY GRAPH                              |
+-----------------------------------------------------------------------------------------+
|                                                                                         |
|   [Client Request] (e.g. POST /blog with Bearer Token)                                  |
|          |                                                                              |
|          v                                                                              |
|   +---------------------------------------------------------------------------------+   |
|   | 1. Authentication & Security Middleware (`blog/oauth2.py`)                       |   |
|   |    - Extracts JWT Bearer token from HTTP Authorization header                   |   |
|   |    - Cryptographically validates signature & expiration (`blog/token.py`)        |   |
|   |    - Resolves authenticated user identity into FastAPI request context          |   |
|   +---------------------------------------------------------------------------------+   |
|          |                                                                              |
|          v                                                                              |
|   +---------------------------------------------------------------------------------+   |
|   | 2. Routing & Request Contract Validation (`blog/routers/`)                      |   |
|   |    - APIRouter matches endpoint and methods                                     |   |
|   |    - Pydantic models (`blog/schemas.py`) enforce type safety & payload shapes   |   |
|   +---------------------------------------------------------------------------------+   |
|          |                                                                              |
|          v                                                                              |
|   +---------------------------------------------------------------------------------+   |
|   | 3. Repository Layer (`blog/repository/`)                                        |   |
|   |    - Encapsulates database queries and persistence business logic               |   |
|   |    - Decouples HTTP transport semantics from data access logic                  |   |
|   +---------------------------------------------------------------------------------+   |
|          |                                                                              |
|          v                                                                              |
|   +---------------------------------------------------------------------------------+   |
|   | 4. Data Access & Session Lifecycle (`blog/database.py`)                         |   |
|   |    - FastAPI `Depends(get_db)` provides scoped SQLAlchemy session               |   |
|   |    - Automatic session cleanup/yield across request lifecycle                   |   |
|   |    - Declarative ORM models (`blog/models.py`) with foreign key relationships   |   |
|   +---------------------------------------------------------------------------------+   |
|                                                                                         |
+-----------------------------------------------------------------------------------------+
```

---

## 🔑 Key Architectural Highlights

1. **Repository Pattern**:
   Database queries and mutation operations are decoupled from HTTP router definitions into discrete repository modules (`repository/blog.py`, `repository/user.py`), ensuring clean unit-testability without spinning up HTTP servers.
2. **Deterministic Session Scoping**:
   Database sessions are provided via Python generators (`get_db`) injected into route dependencies (`Depends(get_db)`), ensuring DB connections are properly committed and released even during unhandled exceptions.
3. **Strict Validation & Serialization (`Pydantic`)**:
   Inbound request bodies and outbound response payloads use separate Pydantic schemas (e.g., `ShowBlog`, `UserResponse`), preventing accidental leakage of sensitive attributes (like hashed passwords) in API outputs.
4. **Secure Password Hashing**:
   Implements `passlib.context.CryptContext` with `bcrypt` salt generation and cryptographic token verification.

---

## 📁 Project Structure

```text
├── blog/
│   ├── repository/           # Data access layer (Business queries)
│   │   ├── blog.py
│   │   └── user.py
│   ├── routers/              # Modular API endpoints
│   │   ├── authentication.py # OAuth2 token issuance (/login)
│   │   ├── blog.py           # Blog CRUD endpoints
│   │   └── user.py           # User management
│   ├── database.py           # Engine configuration & get_db generator
│   ├── hashing.py            # Bcrypt hashing utility
│   ├── models.py             # SQLAlchemy relational database tables
│   ├── oauth2.py             # OAuth2PasswordBearer dependency injection
│   ├── schemas.py            # Pydantic validation & response models
│   ├── token.py              # JWT encoding, decoding & token verification
│   └── main.py               # Application factory & router registration
├── requirements.txt          # Production dependencies
└── README.md                 # System documentation
```

---

## 🚀 Quickstart

### 1. Installation & Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Development Server
```bash
uvicorn blog.main:app --reload --port 8000
```

### 3. Interactive OpenAPI Documentation
Once launched, inspect the automatically generated Swagger UI:
- **Interactive Swagger Docs**: `http://127.0.0.1:8000/docs`
- **ReDoc Specification**: `http://127.0.0.1:8000/redoc`

---

## 🧪 API Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/login` | Authenticate with credentials and receive Bearer JWT | No |
| `POST` | `/user` | Register a new user with bcrypt-hashed password | No |
| `GET` | `/user/{id}` | Fetch user profile and associated posts | Yes |
| `POST` | `/blog` | Create a new blog post | Yes |
| `GET` | `/blog` | List all blog posts with author details | Yes |
| `GET` | `/blog/{id}` | Get specific blog post by ID | Yes |
| `PUT` | `/blog/{id}` | Update existing blog post | Yes |
| `DELETE` | `/blog/{id}` | Delete blog post | Yes |

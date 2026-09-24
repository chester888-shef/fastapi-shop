##E-commerce Backend API

A backend for an online store built with FastAPI, focused on practicing 
clean API design, authentication, and database architecture.

Features

- User registration and authentication via JWT tokens
- Passwords are hashed before storage (never stored in plain text)
- Product catalog with full CRUD operations
- Shopping cart functionality (view, add, update items)
- Interactive API documentation and testing via Swagger UI

echnologies & Architecture

- Language:Python
- Framework: FastAPI
- Database: SQLite
- ORM:SQLAlchemy
- Migrations: Alembic
- Auth: JWT (JSON Web Tokens), with password hashing

## Implementation Details (Under the hood)

- Models are separated by domain (User, Product, Order, etc.) for clean 
  code structure.
- Authentication flow: passwords are hashed on registration; on login, 
  the password is verified against the stored hash before a JWT token 
  is issued.
- Database schema versioning is handled with Alembic migrations, 
  allowing safe, incremental changes to the database structure.
- All endpoints were tested and verified through Swagger UI.


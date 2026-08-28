# Enterprise Resource Planning (ERP) Backend

A scalable and modular Enterprise Resource Planning (ERP) backend built with Django REST Framework. This project provides RESTful APIs for managing core business operations and is designed to be containerized using Docker for easy development and deployment.

## Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL

### In Progress / Planned
- RESTful CRUD APIs for each module (products, inventory, purchases, sales, invoices, etc.)
- JWT-based authentication and role-based authorization
- Business logic for order/inventory workflows (e.g. purchase order → stock update)
- Search, filtering, sorting, and pagination on list endpoints
- Automated tests (auth, permissions, CRUD, business logic)
- Async task handling (Celery + Redis) for emails/notifications
- API documentation


## ** GitHub Release Note (v1.0)**

**Title:**  
`RBAC Prototype v1.0 – Django + DRF`

**Description:**
``

This release delivers the initial implementation of a Role-Based Access Control (RBAC) system using Django and Django REST Framework.

### Features:

* Created two API endpoints:

  * `/api/data/` – GET for all authenticated users
  * `/api/config/` – GET and POST for Administrator only
* Implemented custom DRF permission classes (IsAdmin, IsAnalyst)
* Added role management via Django Groups
* Configured Django Admin UI for managing users and roles
* Verified access rules using Postman and curl

### Testing:

* Admin:

  * Full access to `/api/data/` and `/api/config/`
* Analyst:

  * Read-only access to `/api/data/`
  * Denied access to `/api/config/`

### Notes:

* Uses SQLite by default (can be switched to any Django-supported DB)
* Default DRF authentication applied

```

``
# Role-Based Access Control (RBAC) Prototype – Django & DRF

##  Overview
This project demonstrates how to implement **Role-Based Access Control (RBAC)** in a Django + Django REST Framework environment.  
It defines two user roles (**Administrator** and **Analyst**) with different access permissions for mock API endpoints.

The system uses:
- Django’s built-in authentication
- Groups for role management
- Custom DRF permission classes for access control

---

##  Objectives
- Implement RBAC for two mock API endpoints: `/api/data/` and `/api/config/`.
- **Administrator** → Full access to both endpoints.
- **Analyst** → Read-only access to `/api/data/` and no access to `/api/config/`.
- Manage users and roles via Django Admin UI.
- Test with **Postman** and **curl**.

---

## 🛠 Technologies Used
| Technology              | Purpose                                         |
|-------------------------|-------------------------------------------------|
| **Django**              | Web framework, authentication, admin interface |
| **Django REST Framework** | API endpoint handling, permission classes      |
| **SQLite**              | Default Django database for storing data        |
| **Postman / curl**      | API testing tools                               |
| **Python**              | Programming language                            |

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/princebabou/Django_rbac.git
cd Django_rbac
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Access the admin panel at:
`http://127.0.0.1:8000/admin`

---

## Roles & Permissions

* **Administrator**:

  * GET `/api/data/`
  * GET `/api/config/`
  * POST `/api/config/`
* **Analyst**:

  * GET `/api/data/`
  * No access to `/api/config/`

---

## API Endpoints

| Endpoint  | Method | Role           | Description               |
| --------- | ------ | -------------- | ------------------------- |
| `/api/data/`   | GET    | Admin, Analyst | Retrieve data             |
| `/api/config/` | GET    | Admin only     | View configuration data   |
| `/api/config/` | POST   | Admin only     | Update configuration data |

---

## Testing

**With Postman or curl:**

**Admin user:**

```bash
curl -u admin:password http://127.0.0.1:8000/api/data
curl -u admin:password http://127.0.0.1:8000/api/config
curl -u admin:password -X POST http://127.0.0.1:8000/api/config
```

**Analyst user:**

```bash
curl -u analyst:password http://127.0.0.1:8000/api/data
curl -u analyst:password http://127.0.0.1:8000/api/config
```

---

## Screenshots

* Django Admin – Groups setup
* Admin access to `/api/config/` (200 OK)
* Analyst forbidden on `/api/config/` (403)
* GitHub release page

---

## License

This project is for educational and demonstration purposes.


```

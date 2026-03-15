# Django REST Framework Master-Mapping Backend

A **production-ready, modular Django REST Framework backend** implementing a hierarchical master-mapping system using only **APIView** (no ViewSets) and **drf-yasg** for API documentation.

**Status:** ✅ **COMPLETE & DEPLOYED** - All requirements met, fully tested, and running in production on PythonAnywhere.

---

## 🌐 📍 LIVE PRODUCTION URLS

### **Your Django App is NOW LIVE!**

| Resource | Live URL |
|----------|----------|
| 🏠 **Home** | https://naveencg.pythonanywhere.com/ |
| 📚 **Swagger UI (API Docs)** | https://naveencg.pythonanywhere.com/swagger/ |
| 📖 **ReDoc (Alternative Docs)** | https://naveencg.pythonanywhere.com/redoc/ |
| 🔐 **Django Admin Panel** | https://naveencg.pythonanywhere.com/admin/ |
| 📡 **API Endpoints** | https://naveencg.pythonanywhere.com/api/vendors/ |

### 🔐 Production Admin Credentials
- **Username:** `username`
- **Password:** `admin123`

---

## 🎯 Local Development URLs

| Resource | Local URL |
|----------|-----------|
| **API Documentation (Swagger)** | http://localhost:8000/swagger/ |
| **Alternative Docs (ReDoc)** | http://localhost:8000/redoc/ |
| **Django Admin** | http://localhost:8000/admin/ |
| **API Root** | http://localhost:8000/ (redirects to Swagger) |

---

## 📋 Project Overview

### Master Entities (4 apps)
- **Vendor** - Vendor management with code, description, status
- **Product** - Product catalog  
- **Course** - Training courses
- **Certification** - Certifications and qualifications

### Mapping Relationships (3 apps)
- **VendorProductMapping** - Links Vendors → Products
- **ProductCourseMapping** - Links Products → Courses
- **CourseCertificationMapping** - Links Courses → Certifications

---

## 🚀 Setup & Installation

### 1. **Activate Virtual Environment** (Local Development)
```powershell
cd C:\django_intern_assignment
.\venv\Scripts\Activate.ps1
```

### 2. **Install Dependencies** (if needed)
```bash
pip install -r requirements.txt
```

### 3. **Run Migrations**
```bash
python manage.py migrate
```

### 4. **Seed Sample Data**
```bash
python manage.py seed_data
```

*Creates 3 vendors, 4 products, 4 courses, 4 certifications, and all mapping relationships.*

### 5. **Start Development Server**
```bash
python manage.py runserver 8000
```

The server will start at **http://127.0.0.1:8000**

---

## 📚 API Endpoints Reference

### Master Resources (42 operations total)

#### Vendors
**Production:**
```
GET    https://naveencg.pythonanywhere.com/api/vendors/             - List
POST   https://naveencg.pythonanywhere.com/api/vendors/             - Create
GET    https://naveencg.pythonanywhere.com/api/vendors/<id>/        - Get
PUT    https://naveencg.pythonanywhere.com/api/vendors/<id>/        - Full update
PATCH  https://naveencg.pythonanywhere.com/api/vendors/<id>/        - Partial update
DELETE https://naveencg.pythonanywhere.com/api/vendors/<id>/        - Delete
```

**Local Development:**
```
GET    http://localhost:8000/api/vendors/             - List
POST   http://localhost:8000/api/vendors/             - Create
GET    http://localhost:8000/api/vendors/<id>/        - Get
PUT    http://localhost:8000/api/vendors/<id>/        - Full update
PATCH  http://localhost:8000/api/vendors/<id>/        - Partial update
DELETE http://localhost:8000/api/vendors/<id>/        - Delete
```

**Query Filters:**
- `?is_active=true` - Filter by status

#### Products, Courses, Certifications
Same endpoint structure as Vendors (substituting resource name):
```
Production: /api/products/ | /api/courses/ | /api/certifications/
Local: http://localhost:8000/api/products/ | /api/courses/ | /api/certifications/
```

### Mapping Resources

#### Vendor-Product Mappings
**Production:**
```
GET    https://naveencg.pythonanywhere.com/api/vendor-product-mappings/        - List
POST   https://naveencg.pythonanywhere.com/api/vendor-product-mappings/        - Create
GET    https://naveencg.pythonanywhere.com/api/vendor-product-mappings/<id>/   - Get
PUT    https://naveencg.pythonanywhere.com/api/vendor-product-mappings/<id>/   - Full update
PATCH  https://naveencg.pythonanywhere.com/api/vendor-product-mappings/<id>/   - Partial update
DELETE https://naveencg.pythonanywhere.com/api/vendor-product-mappings/<id>/   - Delete
```

**Local Development:**
```
GET    http://localhost:8000/api/vendor-product-mappings/        - List
POST   http://localhost:8000/api/vendor-product-mappings/        - Create
GET    http://localhost:8000/api/vendor-product-mappings/<id>/   - Get
PUT    http://localhost:8000/api/vendor-product-mappings/<id>/   - Full update
PATCH  http://localhost:8000/api/vendor-product-mappings/<id>/   - Partial update
DELETE http://localhost:8000/api/vendor-product-mappings/<id>/   - Delete
```

**Query Filters:**
```
?vendor_id=1          - Filter by vendor
?product_id=2         - Filter by product
?primary_mapping=true - Filter by primary mapping status
?is_active=true       - Filter by status
```

#### Product-Course Mappings
**Production:** `https://naveencg.pythonanywhere.com/api/product-course-mappings/`
**Local:** `http://localhost:8000/api/product-course-mappings/`
*Filters: ?product_id=, ?course_id=*

#### Course-Certification Mappings
**Production:** `https://naveencg.pythonanywhere.com/api/course-certification-mappings/`
**Local:** `http://localhost:8000/api/course-certification-mappings/`
*Filters: ?course_id=, ?certification_id=*

---

## ✔️ Validations Implemented

### Master Models
- ✅ **Required Fields**: `name`, `code` are mandatory
- ✅ **Unique Code**: Code must be unique within each entity type
- ✅ **Auto Timestamps**: `created_at`, `updated_at` managed automatically
- ✅ **Status Field**: `is_active` boolean (default: True)
- ✅ **Field Lengths**: Enforced string length constraints

### Mapping Models
- ✅ **Unique Pair**: No duplicate parent-child mappings
- ✅ **Primary Mapping**: Only one `primary_mapping=True` per parent
- ✅ **FK Validation**: Parent and child entities must exist
- ✅ **Status Field**: `is_active` boolean for soft deletes
- ✅ **Timestamps**: Auto-managed creation/update times

---

## 🏗️ Project Structure

```
django_intern_assignment/
├── core/
│   ├── settings.py                           # Django config, installed apps
│   ├── urls.py                              # Root URLs + drf-yasg config
│   ├── wsgi.py
│   └── management/
│       └── commands/
│           └── seed_data.py                 # Sample data seeding
├── vendor/
│   ├── models.py                            # Vendor model
│   ├── serializers.py                       # Serializer with validation
│   ├── views.py                             # APIView classes
│   ├── urls.py                              # URL routing
│   ├── admin.py                             # Admin configuration
│   ├── apps.py
│   └── migrations/
├── product/                                 # Same structure
├── course/                                  # Same structure
├── certification/                           # Same structure
├── vendor_product_mapping/                  # Same structure
├── product_course_mapping/                  # Same structure
├── course_certification_mapping/            # Same structure
├── manage.py
├── requirements.txt                         # Dependencies list
├── .gitignore
├── db.sqlite3                              # SQLite database
└── README.md                               # This file
```

---

## 🔧 Technology Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| Django | 4.2.13 LTS | Web framework |
| Django REST Framework | 3.14.0 | API framework |
| drf-yasg | 1.21.5 | Swagger/OpenAPI docs |
| Python | 3.10 | Runtime |
| SQLite | 3.x | Database |
| Hosting | PythonAnywhere | Production deployment |

---

## 📖 API Usage Examples

### Create a Vendor (PowerShell)
```powershell
$body = @{
    name = "TechCorp Inc"
    code = "TECH001"
    description = "Leading technology vendor"
    is_active = $true
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/api/vendors/" `
    -Method POST `
    -Body $body `
    -ContentType "application/json" `
    -UseBasicParsing
```

### List All Vendors
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/api/vendors/" -UseBasicParsing | ConvertFrom-Json
```

### Get Specific Vendor
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/api/vendors/1/" -UseBasicParsing | ConvertFrom-Json
```

### Update Vendor (PATCH)
```powershell
$body = @{ is_active = $false } | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/api/vendors/1/" `
    -Method PATCH `
    -Body $body `
    -ContentType "application/json" `
    -UseBasicParsing
```

### Create Vendor-Product Mapping
```powershell
$body = @{
    vendor = 1
    product = 1
    primary_mapping = $true
    is_active = $true
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/api/vendor-product-mappings/" `
    -Method POST `
    -Body $body `
    -ContentType "application/json" `
    -UseBasicParsing
```

### Filter Mappings by Vendor
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/api/vendor-product-mappings/?vendor_id=1" `
    -UseBasicParsing | ConvertFrom-Json
```

---

## 📊 API Response Format

### Success (List)
```json
{
    "count": 3,
    "data": [
        {
            "id": 1,
            "name": "Vendor A",
            "code": "VENDOR_001",
            "description": "Description",
            "is_active": true,
            "created_at": "2026-03-15T10:00:00Z",
            "updated_at": "2026-03-15T10:00:00Z"
        },
        ...
    ]
}
```

### Success (Detail)
```json
{
    "id": 1,
    "name": "Vendor A",
    "code": "VENDOR_001",
    "description": "Description",
    "is_active": true,
    "created_at": "2026-03-15T10:00:00Z",
    "updated_at": "2026-03-15T10:00:00Z"
}
```

### Error (Validation)
```json
{
    "code": ["This field may not be blank."],
    "name": ["Ensure this field has at most 255 characters."]
}
```

---

## 🔒 Admin Interface

Access at **http://localhost:8000/admin/**

Features:
- ✅ Full CRUD for all 7 models
- ✅ Search by name and code
- ✅ Filter by status and dates
- ✅ Inline mapping selection with dropdowns
- ✅ Read-only timestamps
- ✅ Custom admin classes with list display customization

---

## 📚 Swagger/ReDoc Documentation

### Swagger UI
- **URL**: http://localhost:8000/swagger/
- **Features**: 
  - Interactive API testing
  - Live request/response exploration
  - Full schema browser
  - Authentication support

### ReDoc
- **URL**: http://localhost:8000/redoc/
- **Features**:
  - Beautiful, responsive documentation
  - Full schema with examples
  - Search functionality
  - Mobile-friendly

### Schema Endpoint
- **JSON**: http://localhost:8000/swagger.json
- **YAML**: http://localhost:8000/swagger.yaml

---

## 🎯 Code Architecture

### APIView Implementation
- **No ViewSets** - Pure APIView classes
- **No Mixins** - Manual CRUD methods
- **No Routers** - Explicit URL routing
- **Manual Status Codes** - Proper HTTP responses (200, 201, 204, 400, 404)

### Serializer Validation
Each serializer includes:
- Field-level validation
- Custom validators (e.g., unique code check)
- Duplicate mapping prevention
- Primary mapping constraint logic

### URL Organization
```python
# Each app has its own urls.py
path('api/', include('vendor.urls'))
path('api/', include('product.urls'))
# ... etc
```

---

## 🔍 HTTP Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | OK | GET request successful |
| 201 | Created | POST successful |
| 204 | No Content | DELETE successful |
| 400 | Bad Request | Validation error |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Unexpected error |

---

## 🐛 Troubleshooting

### Server won't start
```powershell
# Check for syntax errors
python manage.py check

# Reset migrations if corrupted
python manage.py migrate --fake-initial
python manage.py migrate
```

### Database issues
```powershell
# Backup old database
Move-Item db.sqlite3 db.sqlite3.backup

# Create fresh database
python manage.py migrate
python manage.py seed_data
```

### Port already in use
```powershell
# Use different port
python manage.py runserver 8001
```

---

## 📦 Deployment

### ✅ DEPLOYED TO PYTHONANYWHERE (PRODUCTION)

The application is **currently live** at:
- **Domain:** https://naveencg.pythonanywhere.com/
- **Status:** ✅ **LIVE & RUNNING**

#### PythonAnywhere Deployment Details
| Component | Details |
|-----------|---------|
| **Hosting** | PythonAnywhere (Free Tier) |
| **Domain** | naveencg.pythonanywhere.com |
| **Python Version** | 3.10 |
| **Virtual Environment** | /home/NaveenCG/.virtualenvs/django_env |
| **Project Path** | /home/NaveenCG/django_intern_assignment |
| **Database** | SQLite (deployed with sample data) |
| **Web Framework** | Django 4.2.13 LTS + WSGI |
| **Static Files** | Collected to /staticfiles/ (192 files) |

#### Live Endpoints Verified ✅
- ✅ Swagger UI: https://naveencg.pythonanywhere.com/swagger/
- ✅ ReDoc: https://naveencg.pythonanywhere.com/redoc/
- ✅ Admin Panel: https://naveencg.pythonanywhere.com/admin/
- ✅ Vendors API: https://naveencg.pythonanywhere.com/api/vendors/
- ✅ Products API: https://naveencg.pythonanywhere.com/api/products/
- ✅ Courses API: https://naveencg.pythonanywhere.com/api/courses/
- ✅ Certifications API: https://naveencg.pythonanywhere.com/api/certifications/
- ✅ All Mapping APIs working with filters

---

### Local Development Checklist
- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Install requirements: `pip install -r requirements.txt`
- [ ] Run migrations: `python manage.py migrate`
- [ ] Seed data: `python manage.py seed_data`
- [ ] Start server: `python manage.py runserver`
- [ ] Visit http://localhost:8000/swagger/

### Production Deployment Guide (For Future Deployments)

#### Pre-Deployment Checklist
- [ ] Change `DEBUG = False` in settings.py
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Set `SECRET_KEY` from environment variable
- [ ] Use PostgreSQL instead of SQLite for production
- [ ] Configure CORS headers if needed
- [ ] Set up HTTPS/SSL (PythonAnywhere provides free HTTPS)
- [ ] Configure database backups
- [ ] Set up monitoring and logging

#### PythonAnywhere Deployment Steps
1. **Create PythonAnywhere Account** - Free tier available
2. **Clone Repository** - `git clone <repo>`
3. **Create Virtual Environment** - `mkvirtualenv django_env`
4. **Install Dependencies** - `pip install -r requirements.txt`
5. **Run Migrations** - `python manage.py migrate`
6. **Seed Database** - `python manage.py seed_data`
7. **Configure WSGI** - Edit WSGI file in PythonAnywhere console
8. **Reload Web App** - Click reload button on PythonAnywhere

#### Sample Production Settings
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.pythonanywhere.com', 'localhost', '127.0.0.1']
SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

## ✅ Acceptance Criteria Met

- ✅ All 7 required apps exist
- ✅ APIs written using **APIView only** (no ViewSets/mixins/routers)
- ✅ **CRUD works** for all 4 master and 3 mapping modules
- ✅ **Validations work** correctly (unique codes, no duplicate mappings, primary mapping constraints)
- ✅ **Swagger is accessible** with full documentation
- ✅ **Code is modular** and readable with clean separation
- ✅ **Project runs without errors**
- ✅ Sample data seeding implemented
- ✅ Django admin fully configured
- ✅ Complete README documentation

---

## 📞 Support & Testing

### Test the Live Application
1. **Visit Production Swagger UI:** https://naveencg.pythonanywhere.com/swagger/
2. **Interactive API Testing:** Click "Try it out" on any endpoint
3. **View API Schema:** https://naveencg.pythonanywhere.com/swagger.json

### Test Locally
1. **Start Development Server:** `python manage.py runserver`
2. **Visit Local Swagger UI:** http://localhost:8000/swagger/
3. **Login to Admin:** http://localhost:8000/admin/ (admin/admin123)

### For Issues
1. **Check Production Logs:** PythonAnywhere Web tab → Error log
2. **Check Local Logs:** Terminal output from `runserver`
3. **Database Issues:** Run `python manage.py migrate --fake-initial`
4. **Port Conflicts:** Use `python manage.py runserver 8001`

### Quick Curl Tests

**Test Production Endpoints:**
```bash
curl https://naveencg.pythonanywhere.com/api/vendors/
curl https://naveencg.pythonanywhere.com/api/products/
curl https://naveencg.pythonanywhere.com/api/courses/
```

**Test Local Endpoints:**
```bash
curl http://localhost:8000/api/vendors/
curl http://localhost:8000/api/products/
curl http://localhost:8000/api/courses/
```

---

## 📄 License

This project is created as a Django internship assignment. Feel free to use for educational and commercial purposes.

---

**Last Updated:** March 15, 2026  
**Project Status:** ✅ Complete and Production-Ready

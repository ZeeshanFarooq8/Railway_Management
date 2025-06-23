# 🚆 Railway Management System

A backend system built with **FastAPI**, **PostgreSQL**, and **Docker** to manage railway operations such as passenger registration, train routes, and authentication.

---

## 📦 Features

- Passenger CRUD APIs
- JWT Authentication
- PostgreSQL database integration
- Dockerized for development and deployment
- FastAPI auto-generated Swagger docs

---

## Project Structure

.
├── app/
│ ├── api/ # Route definitions (passenger, auth, etc.)
│ ├── core/ # Security utils (password hashing, JWT)
│ ├── db/ # Database models and session
│ └── main.py # FastAPI app entrypoint
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🛠 Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose
- Pydantic v2
- Passlib (for password hashing)
- Python-Jose (for JWT)

---

##  Getting Started

### 1. Clone the project

```bash
git clone https://github.com/yourusername/railway-management-system.git
cd railway-management-system
2. Create .env file
Inside the root directory, create a .env file with:

bash
Copy
Edit
DB_URL=postgresql://postgres:password@db:5432/railway
3. Run with Docker
bash
Copy
Edit
docker-compose up --build
Once containers are up, visit:

API Docs: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🧪 API Endpoints
Route	Method	Description
/api/v1/passengers	GET	List all passengers
/api/v1/passengers	POST	Create new passenger
/api/v1/auth/register	POST	Register a new user
/api/v1/auth/login	POST	User login (returns JWT)

🐳 Docker Commands
bash
Copy
Edit
docker-compose up --build     # Start app
docker-compose down           # Stop and remove containers
✅ Authentication
Register using /api/v1/auth/register

Login via /api/v1/auth/login

Use JWT in Authorization: Bearer <token> header for protected endpoints

⚠️ Notes
Pydantic v2 is used — make sure your models use from_attributes=True instead of orm_mode=True.

If you see email-validator is not installed, run:

bash
Copy
Edit
pip install pydantic[email]
📄 License
MIT License

yaml
Copy
Edit

---

Let me know if you'd like to update this once you add train routes or user roles!
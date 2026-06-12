Helpdesk Ticket Management System
Project Overview
The Helpdesk Ticket Management System is a backend application built using FastAPI that allows employees to raise, track, update, and manage support tickets. The system includes authentication, employee management, ticket management, database integration, Docker support, and automated testing.
Features
Authentication
User Registration
User Login
JWT Token Authentication
Password Hashing using Passlib (bcrypt)
Employee Management
Create Employee
Get All Employees
Get Employee by ID
Update Employee
Delete Employee
View Employee Tickets
Ticket Management
Create Ticket
Get All Tickets
Get Ticket by ID
Update Ticket
Delete Ticket
Assign Ticket to Employee
Database
SQLite Database Integration
SQLAlchemy ORM
Automatic Table Creation
Bonus Features Implemented
Docker Support
Dockerfile Created
Docker Image Built Successfully
Docker Container Running Successfully
Build Docker Image
Bash
docker build -t helpdesk-ticket-system .
Run Docker Container
Bash
docker run -d -p 8000:8000 --name helpdesk-container helpdesk-ticket-system
Check Running Containers
Bash
docker ps
API Documentation
FastAPI automatically generates API documentation.
Swagger UI
Plain text
http://127.0.0.1:8000/docs
ReDoc
Plain text
http://127.0.0.1:8000/redoc
Pytest Testing
Implemented basic automated tests.
Test Files
Plain text
app/tests/
├── test_auth.py
├── test_employees.py
├── test_tickets.py
Run Tests
Bash
pytest
Test Result
HELPDESK_TICKET_SYSTEM/
│
├── app/
│   ├── database/
│   │   ├── base.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── employee.py
│   │   └── tickets.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── employee.py
│   │   └── tickets.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── employee.py
│   │   └── ticket.py
│   │
│   ├── services/
│   │   ├── auth_services.py
│   │   ├── employee_service.py
│   │   └── ticket_service.py
│   │
│   ├── utils/
│   │   └── role_checker.py
│   │
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_employees.py
│   │   └── test_tickets.py
│   │
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── helpdesk.db
└── README.md
Plain text
====================
3 passed
====================
Project Structure
Plain text
Installation
Clone Repository
Bash
git clone <repository-url>
Navigate to Project
Bash
cd Helpdesk_ticket_system
Create Virtual Environment
Bash
python -m venv venv
Activate Virtual Environment
Windows:
Bash
venv\Scripts\activate
Install Dependencies
Bash
pip install -r requirements.txt
Run Application
Bash
uvicorn app.main:app --reload
API Endpoints
Authentication
Method
Endpoint
POST
/auth/register
POST
/auth/login
Employees
Method
Endpoint
GET
/employees
POST
/employees
GET
/employees/{employee_id}
PUT
/employees/{employee_id}
DELETE
/employees/{employee_id}
GET
/employees/{employee_id}/tickets
Tickets
Method
Endpoint
POST
/tickets
GET
/tickets
GET
/tickets/{ticket_id}
PUT
/tickets/{ticket_id}
DELETE
/tickets/{ticket_id}
POST
/tickets/{ticket_id}/assign/{employee_id}
Technologies Used
FastAPI
Python 3.13
SQLAlchemy
Pydantic
SQLite
JWT Authentication
Passlib (bcrypt)
Docker
Pytest
Uvicorn
Screenshots
Swagger UI
Add:
Plain text
screenshots/swagger_ui.png
Docker Running Container
Plain text
screenshots/docker_running.png
Pytest Result
Plain text
screenshots/pytest_3_passed.png
Project Structure
Plain text
screenshots/project_structure.png
Author
Bharath G
Backend Developer | FastAPI | Python | SQLAlchemy | Docker
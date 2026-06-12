from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

from app.models.user import User
from app.models.employee import Employee
from app.models.tickets import Ticket

from app.routers import auth
from app.routers import employee
from app.routers import tickets

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)

app.include_router(employee.router)

app.include_router(tickets.router)

@app.get("/")
def home():
    return {
        "message": "Helpdesk Ticket Management System"
    }
from sqlalchemy.orm import Session
from app.models.tickets import Ticket

from app.models.employee import Employee

def create_employee(db: Session, employee):
    
    existing = db.query(Employee).filter(
        Employee.email == employee.email
    ).first()

    if existing:
        return None

    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

def get_employees(db: Session):
    return db.query(Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(
        Employee.id == employee_id
    ).first()
    
def update_employee(
    db: Session,
    employee_id: int,
    employee_data
):

    employee = get_employee(
        db,
        employee_id
    )

    if not employee:
        return None

    employee.name = employee_data.name
    employee.email = employee_data.email
    employee.department = employee_data.department

    db.commit()
    db.refresh(employee)

    return employee    

def delete_employee(
    db: Session,
    employee_id: int
):

    employee = get_employee(
        db,
        employee_id
    )

    if not employee:
        return None

    db.delete(employee)
    db.commit()

    return employee

def get_employee_tickets(
    db: Session,
    employee_id: int
):
    return (
        db.query(Ticket)
        .filter(Ticket.assigned_to == employee_id)
        .all()
    )
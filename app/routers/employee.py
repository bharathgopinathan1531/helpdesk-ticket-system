from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.employee_service import get_employee_tickets
from fastapi import Depends
from app.utils.role_checker import admin_only

from app.database.database import get_db

from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate
)

from app.services.employee_service import (
    create_employee,
    get_employees,
    get_employee,
    update_employee,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/")
def create_new_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    new_employee = create_employee(
        db,
        employee
    )

    if not new_employee:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return new_employee

@router.get("/")
def get_all_employees(
    db: Session = Depends(get_db)
):
    return get_employees(db)

@router.get("/{employee_id}")
def get_single_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = get_employee(
        db,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.put("/{employee_id}")
def update_single_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    updated = update_employee(
        db,
        employee_id,
        employee
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated

@router.delete("/{employee_id}")
def delete_single_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_employee(
        db,
        employee_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }
    
@router.get("/{employee_id}/tickets")
def employee_tickets(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return get_employee_tickets(
        db,
        employee_id
    )    
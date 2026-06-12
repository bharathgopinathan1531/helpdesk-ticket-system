from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.ticket import (
    TicketCreate,
    TicketUpdate,
    TicketResponse
)
from app.services import ticket_service

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/", response_model=TicketResponse)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    return ticket_service.create_ticket(db, ticket)

@router.get("/", response_model=list[TicketResponse])
def get_tickets(
    skip: int = 0,
    limit: int = 10,
    status: str = None,
    priority: str = None,
    db: Session = Depends(get_db)
):
    return ticket_service.get_tickets(
        db,
        skip,
        limit,
        status,
        priority
    )

@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = ticket_service.get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.put("/{ticket_id}", response_model=TicketResponse)
def update_ticket(
    ticket_id: int,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db)
):
    ticket = ticket_service.update_ticket_status(
        db,
        ticket_id,
        ticket_data
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = ticket_service.delete_ticket(
        db,
        ticket_id
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "message": "Ticket deleted successfully"
    }
    
@router.post("/{ticket_id}/assign/{employee_id}")
def assign_ticket_to_employee(
    ticket_id: int,
    employee_id: int,
    db: Session = Depends(get_db)
):
    ticket = ticket_service.assign_ticket(
        db,
        ticket_id,
        employee_id
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "message": "Ticket assigned successfully",
        "ticket": ticket
    }    
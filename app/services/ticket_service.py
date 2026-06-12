from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.tickets import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate


def create_ticket(db: Session, ticket: TicketCreate):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        assigned_to=ticket.assigned_to
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket

def get_tickets(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    status: str = None,
    priority: str = None
):
    query = db.query(Ticket)

    if status:
        query = query.filter(Ticket.status == status)

    if priority:
        query = query.filter(Ticket.priority == priority)

    return query.offset(skip).limit(limit).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

def update_ticket_status(
    db: Session,
    ticket_id: int,
    ticket_data: TicketUpdate
):
    ticket = get_ticket(db, ticket_id)

    if not ticket:
        return None

    allowed = {
        "Open": ["In Progress"],
        "In Progress": ["Resolved"],
        "Resolved": ["Closed"],
        "Closed": []
    }

    if ticket_data.status not in allowed[ticket.status]:
        raise HTTPException(
            status_code=400,
            detail="Invalid status transition"
        )

    ticket.status = ticket_data.status

    db.commit()
    db.refresh(ticket)

    return ticket

def delete_ticket(
    db: Session,
    ticket_id: int
):
    ticket = get_ticket(db, ticket_id)

    if not ticket:
        return None

    db.delete(ticket)
    db.commit()

    return ticket

def assign_ticket(db: Session, ticket_id: int, employee_id: int):
    ticket = get_ticket(db, ticket_id)

    if not ticket:
        return None

    ticket.assigned_to = employee_id

    db.commit()
    db.refresh(ticket)

    return ticket
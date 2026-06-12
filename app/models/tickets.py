from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    priority = Column(String)
    status = Column(String, default="Open")

    assigned_to = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=True
    )
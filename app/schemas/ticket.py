from pydantic import BaseModel
from enum import Enum

class Priority(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    
class Status(str, Enum):
    Open = "Open"
    InProgress = "In Progress"
    Resolved = "Resolved"
    Closed = "Closed"
    
class TicketUpdate(BaseModel):
    status: Status
    
class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: Priority
    status: Status
    assigned_to: int | None = None
        
class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    assigned_to: int | None = None

    class Config:
        from_attributes = True        
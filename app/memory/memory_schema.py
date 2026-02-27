from pydantic import BaseModel
from datetime import datetime


class MemoryCreate(BaseModel):

    organization_id: str
    memory_type: str
    content: str


class MemoryResponse(BaseModel):

    id: str
    organization_id: str
    memory_type: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
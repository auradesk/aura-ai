from sqlalchemy import Column, String, DateTime, Text
from datetime import datetime
import uuid

from app.database import Base


class AuraMemory(Base):
    __tablename__ = "aura_memory"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    organization_id = Column(String, nullable=False)
    memory_type = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
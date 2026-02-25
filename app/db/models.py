from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.db.database import Base


class UsageLog(Base):

    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True, index=True)

    tenant_id = Column(String, index=True)

    domain = Column(String, index=True)

    message = Column(Text)

    response = Column(Text)

    timestamp = Column(DateTime, default=datetime.utcnow)

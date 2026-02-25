from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///./aura.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class SystemMetric(Base):
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(Float)
    memory = Column(Float)
    response_time = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class IntelligenceScore(Base):
    __tablename__ = "intelligence_scores"

    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String)
    score = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
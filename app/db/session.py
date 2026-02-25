# session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Dummy db session for now
db_session = None
# SQLite for simplicity; change URL if using Postgres/MySQL
DATABASE_URL = "sqlite:///./aura_db.sqlite3"

# Create engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Provide a reusable session object
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# For backward compatibility with previous code
db_session = SessionLocal()
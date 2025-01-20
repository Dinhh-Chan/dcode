# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Set up the database engine and session factory
engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session creator for database interaction
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

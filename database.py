from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo = True)
SessionLocal = sessionmaker(bind = engine, autoflush = True, autocommit = False)

def get_db():
    db = SessionLocal()

    try:
        yield db
        
    finally:
        db.close()

class Base(DeclarativeBase):
    pass
    
import uuid

from sqlalchemy import Column, DateTime, String
from db.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    last_login = Column(DateTime, nullable=True)
    reset_password_token = Column(String, nullable=True)
    reset_password_expires = Column(DateTime, nullable=True)
    
    @classmethod
    def all_users(cls, db):
        return db.query(cls).all()
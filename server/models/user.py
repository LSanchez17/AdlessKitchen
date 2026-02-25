import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.asyncio import AsyncSession
from db.db import Base
from pwdlib import PasswordHash

from schemas.user_schema import UserCreate
from models.helpers.transactions import Transactions

SECRET_KEY = 'WUMBO'
ALGORITHM = "HS256"

hasher = PasswordHash.recommended()

class User(Transactions, Base):
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
    
    @classmethod
    def hash_password(cls, password: str) -> str:
        return hasher.hash(password)
    
    @classmethod
    def verify_password(cls, password: str, password_hash: str) -> bool:
        return hasher.verify(password, password_hash)
    
    @classmethod
    async def create(cls, new_user: UserCreate, db: AsyncSession):
        user = cls(
            email=new_user.email,
            password_hash=cls.hash_password(new_user.password)
        )
        db.add(user)
        await cls.save(cls, db)
        await cls.refresh(cls, db, user)
        return user
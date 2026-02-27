import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "URL",
)
ECHO = os.getenv("ECHO", "False") == "True"

engine = create_async_engine(DATABASE_URL, echo=ECHO)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base for SQLAlchemy models
Base = declarative_base()

# FastApi Dependency to get DB session
async def get_db():
    async with async_session() as session:
        yield session

import uuid

from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

from db.db import Base
from models.mixins.timestamps import TimestampMixin


class Recipe(TimestampMixin, Base):
    __tablename__ = "recipes"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    ingredients = Column(JSON, nullable=False)  
    steps = Column(JSON, nullable=False)

    # back reference to allow convenient access from the User model
    user = relationship("User", back_populates="recipes")

import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.db import Base
from models.mixins.transactions import Transactions
from models.mixins.timestamps import TimestampMixin


class Ingredient(Transactions, TimestampMixin, Base):
    """
    Global ingredient catalog (source of truth).
    """

    __tablename__ = "ingredients"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False, index=True)
    kind = Column(String, nullable=True)  # e.g. "ingredient", "spice", "sauce"

    recipe_ingredients = relationship(
        "RecipeIngredient",
        back_populates="ingredient",
        cascade="all, delete-orphan",
    )

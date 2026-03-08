import uuid

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from db.db import Base
from models.mixins.transactions import Transactions
from models.mixins.timestamps import TimestampMixin


class RecipeIngredient(Transactions, TimestampMixin, Base):
    """
    Join table between recipes and ingredients, with quantity and unit.
    """

    __tablename__ = "recipe_ingredients"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    recipe_id = Column(String(36), ForeignKey("recipes.id"), nullable=False, index=True)
    ingredient_id = Column(String(36), ForeignKey("ingredients.id"), nullable=False, index=True)

    quantity = Column(Float, nullable=True)
    unit = Column(String, nullable=True)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_ingredients")

import uuid

from sqlalchemy import Column, Float, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from db.db import Base
from models.mixins.transactions import Transactions
from models.mixins.timestamps import TimestampMixin


class Recipe(Transactions, TimestampMixin, Base):
    __tablename__ = "recipes"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)

    meal_name = Column(String, nullable=False)
    ingredients_text = Column(Text, nullable=True)
    steps = Column(Text, nullable=True)
    spices_text = Column(Text, nullable=True)
    sauce = Column(String, nullable=True)
    total_calories = Column(Float, nullable=True)
    total_fat = Column(Float, nullable=True)
    total_carb = Column(Float, nullable=True)
    total_protein = Column(Float, nullable=True)
    total_fiber = Column(Float, nullable=True)
    calories_per_100_grams = Column(Float, nullable=True)
    average_servings = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)

    user = relationship("User", back_populates="recipes")
    ingredients = relationship(
        "RecipeIngredient",
        back_populates="recipe",
        cascade="all, delete-orphan",
    )

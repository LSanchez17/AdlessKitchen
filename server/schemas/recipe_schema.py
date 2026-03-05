from datetime import datetime
from pydantic import BaseModel
from typing import List


class RecipeBase(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]


class RecipeCreate(RecipeBase):
    pass


class RecipeRead(RecipeBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"orm_mode": True}

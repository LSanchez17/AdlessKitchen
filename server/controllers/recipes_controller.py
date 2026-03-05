from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.db import get_db
from models.recipe import Recipe
from models.user import User
from schemas.recipe_schema import RecipeCreate, RecipeRead
from security.session import get_current_user

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    dependencies=[Depends(get_current_user)],  # all endpoints require an authenticated user
)

# Note: handlers still accept the current user explicitly when they need the id

@router.get("/", response_model=List[RecipeRead])
async def list_recipes(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Recipe).where(Recipe.user_id == user.id))
    return result.scalars().all()


@router.post("/", response_model=RecipeRead)
async def create_recipe(
    payload: RecipeCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    recipe = Recipe(**payload.model_dump(), user_id=user.id)
    db.add(recipe)
    await db.commit()
    await db.refresh(recipe)
    return recipe

"""add recipe ingredient tables

Revision ID: bf7c9a2e1d30
Revises: 7ef330f6f684
Create Date: 2026-03-07 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf7c9a2e1d30'
down_revision: Union[str, Sequence[str], None] = '7ef330f6f684'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'recipes',
        sa.Column('id', sa.String(36), nullable=False),
        sa.Column('user_id', sa.String(36), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('meal_name', sa.String(), nullable=False),
        sa.Column('ingredients_text', sa.Text(), nullable=True),
        sa.Column('spices_text', sa.Text(), nullable=True),
        sa.Column('sauce', sa.String(), nullable=True),
        sa.Column('total_calories', sa.Float(), nullable=True),
        sa.Column('total_fat', sa.Float(), nullable=True),
        sa.Column('total_carb', sa.Float(), nullable=True),
        sa.Column('total_protein', sa.Float(), nullable=True),
        sa.Column('total_fiber', sa.Float(), nullable=True),
        sa.Column('calories_per_100_grams', sa.Float(), nullable=True),
        sa.Column('average_servings', sa.Float(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('discarded_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('ix_recipes_user_id', 'recipes', ['user_id'])

    op.create_table(
        'ingredients',
        sa.Column('id', sa.String(36), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('kind', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('discarded_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )
    op.create_index('ix_ingredients_name', 'ingredients', ['name'])

    op.create_table(
        'recipe_ingredients',
        sa.Column('id', sa.String(36), nullable=False),
        sa.Column('recipe_id', sa.String(36), sa.ForeignKey('recipes.id'), nullable=False),
        sa.Column('ingredient_id', sa.String(36), sa.ForeignKey('ingredients.id'), nullable=False),
        sa.Column('quantity', sa.Float(), nullable=True),
        sa.Column('unit', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('discarded_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('ix_recipe_ingredients_recipe_id', 'recipe_ingredients', ['recipe_id'])
    op.create_index('ix_recipe_ingredients_ingredient_id', 'recipe_ingredients', ['ingredient_id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_recipe_ingredients_ingredient_id', table_name='recipe_ingredients')
    op.drop_index('ix_recipe_ingredients_recipe_id', table_name='recipe_ingredients')
    op.drop_table('recipe_ingredients')

    op.drop_index('ix_ingredients_name', table_name='ingredients')
    op.drop_table('ingredients')

    op.drop_index('ix_recipes_user_id', table_name='recipes')
    op.drop_table('recipes')

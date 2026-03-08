import os

import httpx
from fastapi import APIRouter, Depends

from schemas.recipe_schema import RecipeExtractionRequest, RecipeExtractionResponse
from schemas.response_schema import ServerResponse
from security.token_refresh import get_user_and_refresh

BROWSER_AGENT_URL = os.getenv("BROWSER_AGENT_URL", "http://127.0.0.1:8001")
BROWSER_AGENT_TASK = (
    "Extract all recipe information from this page, "
    "including ingredients, instructions, and nutritional data"
)
RECIPE_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "meal_name": {
            "type": "string",
            "description": "The name of the recipe",
        },
        "description": {
            "type": "string",
            "description": "A short description or introduction to the recipe",
        },
        "average_servings": {
            "type": "number",
            "description": "Number of servings this recipe yields if available",
        },
        "ingredients_text": {
            "type": "array",
            "description": "List of ingredients with quantities and units, e.g. '1 tbsp olive oil'",
            "items": {"type": "string"},
        },
        "steps": {
            "type": "array",
            "description": "Ordered list of cooking instructions, e.g. 'Turn on stove to medium heat'",
            "items": {"type": "string"},
        },
        "nutrition": {
            "type": "object",
            "description": "Nutritional information per serving if available",
            "properties": {
                "calories": {"type": "number"},
                "protein_g": {"type": "number"},
                "carbohydrates_g": {"type": "number"},
                "fat_g": {"type": "number"},
                "fiber_g": {"type": "number"},
            },
        },
    },
    "required": ["meal_name", "ingredients_text", "steps"],
}

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)


@router.post("/imports", response_model=ServerResponse[RecipeExtractionResponse])
async def import_recipe_from_url(
    body: RecipeExtractionRequest,
    _: None = Depends(get_user_and_refresh),
):
    """
    Accept a recipe URL, forward it to the BrowserAgent microservice for
    extraction, and return the pending task details.
    """
    payload = {
        "url": body.url,
        "task": BROWSER_AGENT_TASK,
        "webhook_url": None,
        "response_schema": RECIPE_RESPONSE_SCHEMA
    }

    async with httpx.AsyncClient() as client:
        agent_response = await client.post(
            f"{BROWSER_AGENT_URL}/tasks",
            json=payload,
            timeout=30.0,
        )
        agent_response.raise_for_status()
        agent_data = agent_response.json()

    print("[BrowserAgent response]", agent_data)

    result = RecipeExtractionResponse(
        task_id=agent_data["task_id"],
        status=agent_data.get("status", "pending"),
        result=agent_data.get("result", []),
    )

    return ServerResponse(entity="recipe_import", results=[result])

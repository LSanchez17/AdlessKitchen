from typing import Any, List

from pydantic import BaseModel, field_validator

from schemas.response_schema import model_config


class RecipeExtractionRequest(BaseModel):
    url: str

    model_config = model_config

    @field_validator("url")
    @classmethod
    def url_must_be_https(cls, v: str) -> str:
        if not v.startswith("https://"):
            raise ValueError("URL must start with 'https://'")
        return v


class RecipeExtractionResponse(BaseModel):
    task_id: str
    status: str
    result: List[Any] = []

    model_config = model_config

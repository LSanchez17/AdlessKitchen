from pydantic import BaseModel
from typing import Generic, List, TypeVar
from utils.naming import to_camel

model_config = {"alias_generator": to_camel, "populate_by_name": True}

# Generics <3
T = TypeVar("T")

# Singular response for a single item
class ItemResponse(BaseModel, Generic[T]):
    entity: str
    result: T

    model_config = model_config

# Plural response for lists of items
class ListResponse(BaseModel, Generic[T]):
    entity: str
    results: List[T]

    model_config = model_config

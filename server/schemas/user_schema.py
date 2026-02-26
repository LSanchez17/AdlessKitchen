from pydantic import BaseModel, EmailStr
from schemas.response_schema import model_config

# Base schema for all user-related operations
# first/last are optional in case users haven't provided them yet
class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr

    model_config = model_config

# For creating users
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str | None = None
    last_name: str | None = None

    model_config = model_config

# For logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

    model_config = model_config

# Include the id field for reading users
class UserRead(UserBase):
    id: str

    model_config = {
        **model_config,
        "from_attributes": True,
    }

# For updating users, all fields are optional
class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

    model_config = model_config

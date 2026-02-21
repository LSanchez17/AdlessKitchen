from pydantic import BaseModel, EmailStr

# Base schema for all user-related operations
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

# For creating users, we dont need the other schema fields
class UserCreate(BaseModel):
    password: str
    email: EmailStr

# Include the id field for reading users
class UserRead(UserBase):
    id: str

    class Config:
        orm_mode = True   # allows reading from ORM object; FastAPI should serialize this

# For updating users, all fields are optional
class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
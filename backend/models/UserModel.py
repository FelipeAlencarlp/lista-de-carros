from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    is_admin: bool = False

class UserCreation(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    confirm_password: str = Field(...)


class UserLoginModel(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

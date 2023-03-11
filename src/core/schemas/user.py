from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from core.models.user import UserRoleEnum
from core.schemas import AutoGeneratedFields, BaseSchema


class UserBase(BaseSchema):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[UserRoleEnum] = None


class UserCreate(UserBase):
    email: EmailStr
    hashed_password: Optional[str] = Field(alias='password')


class UserUpdate(UserBase):
    hashed_password: Optional[str] = Field(alias='password')


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase, AutoGeneratedFields):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str


class UserUpdateMe(UserBase):
    hashed_password: Optional[str] = Field(alias='password')
    full_name: Optional[str]
    email: Optional[EmailStr]


class UserOpen(BaseModel):
    hashed_password: str = Field(alias='password')
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]

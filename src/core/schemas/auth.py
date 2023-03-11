import pydantic
from pydantic.fields import Field
from pydantic.networks import EmailStr


class AuthSchema(pydantic.BaseModel):
    class Config:
        orm_mode = True

    email: EmailStr
    password: str


class TokenSchema(pydantic.BaseModel):
    class Config:
        orm_mode = True

    access: str
    refresh: str
    type: str = "Bearer"


class RefreshSchema(pydantic.BaseModel):
    class Config:
        orm_mode = True

    refresh: str

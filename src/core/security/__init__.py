from datetime import datetime, timedelta
from typing import Optional

from fastapi.security import HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt
from passlib.context import CryptContext
from fastapi import Request

from core.conf import settings
from core.errors import AuthBearer


class JsonWebToken(HTTPBearer):
    async def __call__(
            self, request: Request
    ) -> Optional[str]:
        authorization: str = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                raise AuthBearer(
                    {"msg": "You need send JWT token in HTTP Authorization header as 'Bearer {token_here}'"})
            else:
                return None
        if scheme.lower() != "bearer":
            if self.auto_error:
                raise AuthBearer(
                    {"msg": "You need send JWT token in HTTP Authorization header as 'Bearer {token_here}'"})
            else:
                return None
        return credentials


bearer_scheme = JsonWebToken(scheme_name="JWT")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return password_context.hash(password)


def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)


def create_jwt_token(data: dict, expire_minutes: int = None):
    to_encode = data.copy()
    if expire_minutes:
        expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

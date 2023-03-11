from core.conf import settings
from core.models import User
from core.security import create_jwt_token


def create_jwt_for_user(user: User):
    access_token = create_jwt_token(
        data={"sub": str(user.id)}
    )
    refresh_token = create_jwt_token(
        data={"sub": str(user.id)},
        expire_minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
    )
    return access_token, refresh_token

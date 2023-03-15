import uvicorn

from fastapi import FastAPI
from src.routers import apply_routers
from src.utils import get_description


def create_app() -> FastAPI:
    app = FastAPI(
        # root_path=settings.API_V1_STR,
        description=get_description()
    )
    app = apply_routers(app)

    return app


if __name__ == "__main__":
    # Local run

    uvicorn.run('main:create_app', port=8001, reload=True)

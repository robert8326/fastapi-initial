from fastapi import FastAPI
from src.v1 import routers


def apply_routers(app: FastAPI) -> FastAPI:
    for router in routers:
        app.include_router(router)

    return app

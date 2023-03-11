import uvicorn

from fastapi import FastAPI

from core.conf import settings
from utils import get_description

app = FastAPI(
    # root_path=settings.API_V1_STR,
    description=get_description()
)


@app.get("/", tags=['login'])
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    # Local run
    uvicorn.run('main:app', port=8001, debug=True, reload=True)

from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=['login'])
def read_root():
    return {"Hello": "World"}

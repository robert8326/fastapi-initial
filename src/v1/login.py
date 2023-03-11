from main import app


@app.get("/", tags=['login'])
def read_root():
    return {"Hello": "World"}

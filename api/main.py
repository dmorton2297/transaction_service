from fastapi import FastAPI
from api.config import Config

app = FastAPI()
config = Config()

@app.get("/")
def read_root():
    print(config)
    return {"message": "Hello, FastAPI!"}

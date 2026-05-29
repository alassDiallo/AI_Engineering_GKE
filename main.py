from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI(title="API test")


@app.get("/")
def accueil():
    return {"message": "Hello World!"}


@app.post("/informations")
def informations(user: User):
    return {"message": f"Hello {user.name}, you are {user.age} years old!"}

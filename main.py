from fastapi import FastAPI
from pydantic import BaseModel
from db import get_mysql_host


class User(BaseModel):
    name: str
    age: int


app = FastAPI(title="API test")


@app.get("/")
def accueil():
    return {"message": "Hello World!"}


@app.post("/informations")
def informations(user: User):
    """c'est pour afficher les informations de l'utilisateur"""
    return {"message": f"Hello {user.name}, you are {user.age} years old!"}


@app.get("/dbconnection")
def dbconnection():
    db = get_mysql_host()
    return {"message": "Connected to database!", "dbInstance": db}

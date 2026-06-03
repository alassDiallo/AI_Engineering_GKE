from fastapi import FastAPI
from pydantic import BaseModel
from db import CommentDB

comment_db = CommentDB().set_connection()


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
    return {"message": "Connected to database!", "dbInstance": comment_db.dbinstance}


@app.post("/get_comments")
def get_comments():
    """
    get_comments retourne tous les commentaires
    :return: retourne tous les comentaires
    """
    return comment_db.get_comments()


@app.post("/add_comment")
def add_comment(name: str, comment: str):
    """
    add_comment ajoute un commentaire a la base de données
    :param name: le nom de l'utilisateur qui a fait le commentaire
    :param comment: le commentaire de l'utilisateur
    :return: retourne un message de succès ou d'erreur
    """
    from datetime import date

    today = date.today()

    return comment_db.add_comment(name, comment, today.strftime("%Y-%m-%d"))

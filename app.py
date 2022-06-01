from fastapi import FastAPI
from models import user, homework 

from config.db import engine

user.Base.metadata.create_all(bind=engine)
homework.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():
    return{
        "Hello": "World"
    }

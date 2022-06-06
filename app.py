from fastapi import APIRouter, FastAPI

from models import user, homework 
from config.db import engine
from routes.api import users, homeworks

user.Base.metadata.create_all(bind=engine)
homework.Base.metadata.create_all(bind=engine)


app = FastAPI()

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(homeworks.router, prefix="/homeworks", tags=["homeworks"])


app.include_router(api_router, prefix='/api')


@app.get("/")
def root():
    return{
        "Hello": "World"
    }


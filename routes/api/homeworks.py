from typing import List, Generator

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import SessionLocal
from crud import homework, user
import schemas


router = APIRouter()

#Dependency
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/', response_model=List[schemas.homework.HomeWork])
def get_homeworks_by_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return homework.get_home_works(skip=skip, limit=limit, db=Session)

@router.post('/')
def create_home_work(new_home_work: schemas.homework.HomeWorkCreate, db: Session = Depends(get_db)):
    user_db = user.get_user(db=db, user_id=new_home_work.owner_id )
    if user_db is None:
        raise HTTPException(status_code=400, detail="User id not found")
    try:
        db.add(new_home_work)
        db.commit()
        db.refresh
    except Exception as ex:
        raise HTTPException(status_code=400, detail=ex)
    else:
        return new_home_work
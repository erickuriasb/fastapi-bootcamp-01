from re import S
from sqlalchemy.orm import Session

import models, schemas

def get_home_works(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.homework.HomeWork).offset(skip).limit(limit).all()

def create_user_home_work(db: Session, home_work: schemas.homework.HomeWorkCreate):
    db_home_work = models.homework.HomeWork(**home_work.dict())
    db.add(db_home_work)
    db.commit()
    db.refresh(db_home_work)

    return db_home_work
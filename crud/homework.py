from re import S
from sqlalchemy.orm import Session

from . import models, schemas

def get_home_works(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Homework).offset(skip).limit(limit).all()

def create_user_home_work(db: Session, home_work: schemas.HomeWorkCreate, user_id: int):
    db_home_work = models.HomeWork(**home_work.dict(), owner_id=user_id)
    db.add(db_home_work)
    db.commit()
    db.refresh(db_home_work)

    return db_home_work
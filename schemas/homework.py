from typing import Optional
from pydantic import BaseModel

class HomeWorkBase(BaseModel):
    title: str
    description: Optional[str] = "-"

class HomeWorkCreate(HomeWorkBase):
    pass

class HomeWork(HomeWorkBase):
    id: int
    owner_id: int

    class Config:
        orm_mode: True


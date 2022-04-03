from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None

class PostCreate(PostBase):
    pass

class PostResp(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime

    class Config:
        orm_mode = True
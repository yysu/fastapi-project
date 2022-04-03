from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None

class PostCreate(PostBase):
    pass

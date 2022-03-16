from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}
 
@app.get('/posts')
def get_posts():
    return {"data": "This is your post"}

@app.post('/posts')
def create_posts(post: Post):
    print(post)
    return {"data": post.dict()}
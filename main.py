from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, \
        {"title": "title of post 2", "content": "content of post 2", "id": 2}]


def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p
    return None

@app.get("/")
async def root():
    return {"message": "Hello World"}
 
@app.get('/posts')
def get_posts():
    return {"data": my_post}

@app.post('/posts')
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000000)
    my_post.append(post_dict)
    return {"data": post_dict}

@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, \
            detail=f"post with id: {id} was not found")
    return {"data": f"{post}"}
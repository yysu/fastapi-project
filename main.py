from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World yun"}

@app.get('/posts')
def get_posts():
    return {"data": "This is your post"}

@app.post('/createposts')
def create_posts(payload: dict = Body(...)):
    return {"new post": f"title {payload['title']}, content {payload['content']}"}
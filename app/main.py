import time
import psycopg2

from fastapi import FastAPI
from random import randrange
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
from .route import post, user, auth
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='127.0.0.1', port=8080, database='fastapi', user='postgres', password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


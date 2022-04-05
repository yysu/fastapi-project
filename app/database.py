import time
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:8080/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host='127.0.0.1', port=8080, database='fastapi', user='postgres', password='admin', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error: ", error)
#         time.sleep(2)

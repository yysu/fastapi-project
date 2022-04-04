from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "e615c7902d2ff6df8835881afa6052b4734d07d6fe5f6e5e9d3bdc2e821d4ad9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

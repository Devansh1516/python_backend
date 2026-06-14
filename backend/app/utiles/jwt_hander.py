from jose import jwt

SECRET_KEY = "my_super_secret_key"

ALGORITHM = "HS256"


def create_access_token(data: dict):

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verify_token(token: str):

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload
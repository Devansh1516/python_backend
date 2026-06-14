from app.model.user import User

from app.repository.userrep import (
    save_user,
    get_user_by_email
)

from app.utiles.password import (
    hash_password,
    verify_password
)

from app.utiles.jwt_hander import (
    create_access_token
)
from app.utiles.jwt_hander import verify_token
from app.repository.userrep import get_user_by_id

def signup_service(
    username: str,
    email: str,
    password: str
):

    existing_user = get_user_by_email(email)

    if existing_user:

        return {
            "message": "User Already Exists"
        }

    user = User(
        username=username,
        email=email,
        password=hash_password(password),
        role="USER"
    )

    save_user(user)

    return {
        "message": "User Created Successfully"
    }


def login_service(
    email: str,
    password: str
):

    user = get_user_by_email(email)

    if not user:

        return {
            "message": "User Not Found"
        }

    valid_password = verify_password(
        password,
        user.password
    )

    if not valid_password:

        return {
            "message": "Invalid Password"
        }

    token = create_access_token(
        {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
def get_current_user(token: str):

    payload = verify_token(token)

    user_id = payload["id"]

    return get_user_by_id(user_id)
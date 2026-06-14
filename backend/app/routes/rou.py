from fastapi import APIRouter

from app.schema.sec import (
    UserCreate,
    UserLogin
)

from app.service.auth import (
    signup_service,
    login_service
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/")
def home():

    return {
        "message": "Auth Route Working"
    }


@router.post("/register")
def register(user_data: UserCreate):

    return signup_service(
        user_data.username,
        user_data.email,
        user_data.password
    )


@router.post("/login")
def login(user_data: UserLogin):

    return login_service(
        user_data.email,
        user_data.password
    )
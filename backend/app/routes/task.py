from fastapi import APIRouter

from app.schema.sec import TaskCreate

from app.service.task import (
    create_task_service,
    get_tasks_service,
    update_task_service,
    delete_task_service
)

from app.utiles.jwt_hander import verify_token


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_task(
    task_data: TaskCreate,
    token: str
):

    payload = verify_token(token)

    user_id = payload["id"]

    return create_task_service(
        task_data.title,
        task_data.description,
        user_id
    )


@router.get("/")
def get_tasks(token: str):

    payload = verify_token(token)

    user_id = payload["id"]

    return get_tasks_service(user_id)


@router.put("/{task_id}")
def update_task(task_id: int):

    return update_task_service(task_id)


@router.delete("/{task_id}")
def delete_task(task_id: int):

    return delete_task_service(task_id)
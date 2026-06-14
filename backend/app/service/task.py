from app.model.task import Task

from app.repository.taskrepo import (
    save_task,
    get_tasks_by_user,
    update_task,
    delete_task
)


def create_task_service(
    title: str,
    description: str,
    user_id: int
):

    task = Task(
        title=title,
        description=description,
        completed=False,
        user_id=user_id
    )

    return save_task(task)


def get_tasks_service(
    user_id: int
):

    return get_tasks_by_user(user_id)


def update_task_service(
    task_id: int
):

    return update_task(task_id)

def delete_task_service(
    task_id: int
):

    return delete_task(task_id)
from app.database import SessionLocal
from app.model.task import Task


def save_task(task: Task):

    db = SessionLocal()

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def get_tasks_by_user(user_id: int):

    db = SessionLocal()

    tasks = db.query(Task).filter(
        Task.user_id == user_id
    ).all()

    return tasks




def get_tasks_by_user(user_id: int):

    db = SessionLocal()

    return db.query(Task).filter(
        Task.user_id == user_id
    ).all()


def update_task(task_id: int):

    db = SessionLocal()

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        return {
            "message": "Task Not Found"
        }

    task.completed = True

    db.commit()

    db.refresh(task)

    return task


def delete_task(task_id: int):

    db = SessionLocal()

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        return {
            "message": "Task Not Found"
        }

    db.delete(task)

    db.commit()

    return {
        "message": "Task Deleted Successfully"
    }
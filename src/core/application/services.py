from typing import List, Optional
from src.core.domain.entities import Task
from src.core.application.ports.task_repository import TaskRepository

class TodoService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def add_task(self, user_id: str, title: str, description: Optional[str] = None) -> Task:
        if not title:
            raise ValueError("Title cannot be empty")
        task = Task(title=title, description=description, user_id=user_id)
        return self.task_repository.add(task)

    def get_task(self, user_id: str, task_id: int) -> Optional[Task]:
        pass

    def list_tasks(self, user_id: str) -> List[Task]:
        # For now, we are not filtering by user_id, but this is where it would happen
        return self.task_repository.list()

    def update_task(
        self,
        user_id: str,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        is_complete: Optional[bool] = None,
    ) -> Optional[Task]:
        task = self.task_repository.get_by_id(task_id)
        if task and task.user_id == user_id:
            if title is not None:
                if not title:
                    raise ValueError("Title cannot be empty")
                task.title = title
            if description is not None:
                task.description = description
            if is_complete is not None:
                task.is_complete = is_complete
            return self.task_repository.update(task)
        return None

    def delete_task(self, user_id: str, task_id: int) -> bool:
        task = self.task_repository.get_by_id(task_id)
        if task and task.user_id == user_id:
            return self.task_repository.delete(task_id)
        return False

    def mark_task_complete(self, user_id: str, task_id: int) -> Optional[Task]:
        task = self.task_repository.get_by_id(task_id)
        if task and task.user_id == user_id:
            task.is_complete = True
            return self.task_repository.update(task)
        return None

    def mark_task_incomplete(self, user_id: str, task_id: int) -> Optional[Task]:
        task = self.task_repository.get_by_id(task_id)
        if task and task.user_id == user_id:
            task.is_complete = False
            return self.task_repository.update(task)
        return None

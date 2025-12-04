from typing import List, Optional, Dict
from src.core.domain.entities import Task
from src.core.application.ports.task_repository import TaskRepository

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, task: Task) -> Task:
        task.id = self._next_id
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def list(self) -> List[Task]:
        return list(self._tasks.values())

    def update(self, task: Task) -> Optional[Task]:
        if task.id in self._tasks:
            self._tasks[task.id] = task
            return task
        return None

    def delete(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

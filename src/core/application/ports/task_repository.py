from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.domain.entities import Task

class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> Task:
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def list(self) -> List[Task]:
        pass

    @abstractmethod
    def update(self, task: Task) -> Optional[Task]:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass

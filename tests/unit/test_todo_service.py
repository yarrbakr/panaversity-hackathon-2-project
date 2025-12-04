import pytest
from src.core.domain.entities import Task
from src.core.application.ports.task_repository import TaskRepository
from src.core.application.services import TodoService
from src.core.infrastructure.in_memory_repository import InMemoryTaskRepository

@pytest.fixture
def in_memory_repo():
    return InMemoryTaskRepository()

@pytest.fixture
def todo_service(in_memory_repo):
    return TodoService(in_memory_repo)

class TestTodoService:
    def test_add_task(self, todo_service: TodoService):
        task = todo_service.add_task("user1", "Buy groceries", "Milk, eggs")
        assert task.id is not None
        assert task.title == "Buy groceries"
        assert task.description == "Milk, eggs"
        assert not task.is_complete
        assert task.user_id == "user1"

    def test_add_task_empty_title_raises_error(self, todo_service: TodoService):
        with pytest.raises(ValueError, match="Title cannot be empty"):
            todo_service.add_task("user1", "", "Description")

    def test_list_tasks(self, todo_service: TodoService):
        todo_service.add_task("user1", "Task 1")
        todo_service.add_task("user1", "Task 2")
        tasks = todo_service.list_tasks("user1")
        assert len(tasks) == 2
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"

    def test_mark_task_complete(self, todo_service: TodoService):
        task = todo_service.add_task("user1", "Task to complete")
        completed_task = todo_service.mark_task_complete("user1", task.id)
        assert completed_task is not None
        assert completed_task.is_complete
        assert todo_service.get_task("user1", task.id).is_complete

    def test_mark_task_complete_not_found(self, todo_service: TodoService):
        completed_task = todo_service.mark_task_complete("user1", 999)
        assert completed_task is None

    def test_mark_task_incomplete(self, todo_service: TodoService):
        task = todo_service.add_task("user1", "Task to incomplete")
        todo_service.mark_task_complete("user1", task.id) # First complete it
        incomplete_task = todo_service.mark_task_incomplete("user1", task.id)
        assert incomplete_task is not None
        assert not incomplete_task.is_complete
        assert not todo_service.get_task("user1", task.id).is_complete

    def test_mark_task_incomplete_not_found(self, todo_service: TodoService):
        incomplete_task = todo_service.mark_task_incomplete("user1", 999)
        assert incomplete_task is None

    def test_update_task(self, todo_service: TodoService):
        task = todo_service.add_task("user1", "Old title", "Old description")
        updated_task = todo_service.update_task("user1", task.id, "New title", "New description", True)
        assert updated_task is not None
        assert updated_task.title == "New title"
        assert updated_task.description == "New description"
        assert updated_task.is_complete
        
        retrieved_task = todo_service.get_task("user1", task.id)
        assert retrieved_task.title == "New title"
        assert retrieved_task.description == "New description"
        assert retrieved_task.is_complete

    def test_update_task_partial(self, todo_service: TodoService):
        task = todo_service.add_task("user1", "Old title", "Old description")
        updated_task = todo_service.update_task("user1", task.id, title="Only title changed")
        assert updated_task.title == "Only title changed"
        assert updated_task.description == "Old description" # Description should remain unchanged

    def test_update_task_empty_title_raises_error(self, todo_service: TodoService):
        task = todo_service.add_task("user1", "Valid title")
        with pytest.raises(ValueError, match="Title cannot be empty"):
            todo_service.update_task("user1", task.id, title="")

    def test_update_task_not_found(self, todo_service: TodoService):
        updated_task = todo_service.update_task("user1", 999, "New title")
        assert updated_task is None

    def test_delete_task(self, todo_service: TodoService):
        task = todo_service.add_task("user1", "Task to delete")
        success = todo_service.delete_task("user1", task.id)
        assert success
        assert todo_service.get_task("user1", task.id) is None

    def test_delete_task_not_found(self, todo_service: TodoService):
        success = todo_service.delete_task("user1", 999)
        assert not success

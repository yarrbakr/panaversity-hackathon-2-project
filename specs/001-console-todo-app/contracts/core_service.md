# Core Service Contracts: Console To-Do Application

This document defines the interface for the core business logic service, adhering to the Hexagonal Architecture principle. The service operates on `Task` entities and is independent of any presentation or persistence concerns. All methods accept a `user_id` for multi-tenancy support.

## Entity: Task (Input/Output DTO)

```python
from typing import Optional, List
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_complete: Optional[bool] = None

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_complete: bool
    user_id: str
```

## Service Interface: `TodoService`

### `add_task(user_id: str, task_data: TaskCreate) -> Task`

-   **Description**: Adds a new task for the specified user.
-   **Parameters**:
    -   `user_id` (str): The ID of the user creating the task.
    -   `task_data` (TaskCreate): An object containing the title and optional description for the new task.
-   **Returns**: `Task`: The newly created task, including its assigned ID and default status.
-   **Errors**:
    -   `ValueError`: If `task_data.title` is empty.

### `get_task(user_id: str, task_id: int) -> Optional[Task]`

-   **Description**: Retrieves a specific task by its ID for the given user.
-   **Parameters**:
    -   `user_id` (str): The ID of the user requesting the task.
    -   `task_id` (int): The ID of the task to retrieve.
-   **Returns**: `Optional[Task]`: The requested task if found, otherwise `None`.

### `list_tasks(user_id: str) -> List[Task]`

-   **Description**: Retrieves all tasks for the specified user.
-   **Parameters**:
    -   `user_id` (str): The ID of the user whose tasks are to be listed.
-   **Returns**: `List[Task]`: A list of all tasks belonging to the user. Returns an empty list if no tasks are found.

### `update_task(user_id: str, task_id: int, task_data: TaskUpdate) -> Optional[Task]`

-   **Description**: Updates the details (title, description, completion status) of an existing task for the specified user.
-   **Parameters**:
    -   `user_id` (str): The ID of the user owning the task.
    -   `task_id` (int): The ID of the task to update.
    -   `task_data` (TaskUpdate): An object containing the fields to update. Only provided fields will be changed.
-   **Returns**: `Optional[Task]`: The updated task if found, otherwise `None`.
-   **Errors**:
    -   `ValueError`: If `task_data.title` is empty when provided.

### `delete_task(user_id: str, task_id: int) -> bool`

-   **Description**: Deletes a task by its ID for the specified user.
-   **Parameters**:
    -   `user_id` (str): The ID of the user owning the task.
    -   `task_id` (int): The ID of the task to delete.
-   **Returns**: `bool`: `True` if the task was successfully deleted, `False` if the task was not found.

### `mark_task_complete(user_id: str, task_id: int) -> Optional[Task]`

-   **Description**: Marks an existing task as complete for the specified user.
-   **Parameters**:
    -   `user_id` (str): The ID of the user owning the task.
    -   `task_id` (int): The ID of the task to mark complete.
-   **Returns**: `Optional[Task]`: The updated task if found, otherwise `None`.

### `mark_task_incomplete(user_id: str, task_id: int) -> Optional[Task]`

-   **Description**: Marks an existing task as incomplete for the specified user.
-   **Parameters**:
    -   `user_id` (str): The ID of the user owning the task.
    -   `task_id` (int): The ID of the task to mark incomplete.
-   **Returns**: `Optional[Task]`: The updated task if found, otherwise `None`.

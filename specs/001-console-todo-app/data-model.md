# Data Model: Console To-Do Application

## Entity: Task

The `Task` entity represents a single to-do item within the application. It is designed to be a pure Python object, independent of any persistence mechanism, aligning with the Hexagonal Architecture principles.

### Attributes

-   **`id`**:
    -   **Type**: `Integer`
    -   **Description**: A unique identifier for the task. Assigned sequentially, starting from 1. Once an ID is used, it is never reused, even if the task is deleted.
    -   **Constraints**: Primary Key, Auto-incrementing (conceptually for in-memory), Non-nullable.
-   **`title`**:
    -   **Type**: `String`
    -   **Description**: A concise summary or name for the task.
    -   **Constraints**: Non-nullable, minimum length 1 character.
-   **`description`**:
    -   **Type**: `String`
    -   **Description**: A more detailed explanation or notes for the task.
    -   **Constraints**: Nullable (optional).
-   **`is_complete`**:
    -   **Type**: `Boolean`
    -   **Description**: Indicates whether the task has been completed.
    -   **Constraints**: Non-nullable, default value `False`.
-   **`user_id`**:
    -   **Type**: `String`
    -   **Description**: Identifier for the user who owns the task. This supports multi-tenancy from Day 1. For Phase I (CLI), this will be a mocked or default value.
    -   **Constraints**: Non-nullable.

### Relationships

-   None (for Phase I, tasks are independent entities within a user's context).

### Example (Conceptual SQLModel representation)

```python
from typing import Optional
from sqlmodel import Field, SQLModel

class Task(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    is_complete: bool = False
    user_id: str = "default_user" # Mocked for Phase I
```

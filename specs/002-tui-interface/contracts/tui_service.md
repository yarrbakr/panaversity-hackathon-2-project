# TUI Service Contracts: Console To-Do Application

This document describes how the Terminal User Interface (TUI) will interact with the existing core business logic service (`TodoService`).

## Core Service Dependency

The TUI will depend on the `TodoService` interface defined in the `001-console-todo-app` feature's `core_service.md`. The TUI will be responsible for instantiating the `TodoService` with the `InMemoryTaskRepository` and calling its methods in response to user interactions.

## TUI-Service Interaction Mapping

| User Action in TUI | `TodoService` Method Called |
|---|---|
| View task list | `list_tasks(user_id)` |
| Submit "Add Task" form | `add_task(user_id, task_data)` |
| Toggle task completion | `mark_task_complete(user_id, task_id)` or `mark_task_incomplete(user_id, task_id)` |
| Submit "Edit Task" form | `update_task(user_id, task_id, task_data)` |
| Confirm task deletion | `delete_task(user_id, task_id)` |

The `user_id` will be a mocked or default value for Phase I, as defined in the constitution.

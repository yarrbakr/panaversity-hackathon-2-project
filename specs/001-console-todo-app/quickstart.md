# Quickstart: Console To-Do Application

This document provides a quick guide to setting up and using the Console To-Do Application.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Set up Python environment with `uv`:**
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install -e .
    ```

## Usage

The application is a command-line interface (CLI) tool. Once installed, you can interact with it using the following commands:

### Add a Task

To add a new task, use the `add` command:

```bash
python -m src.interfaces.cli add --title "Buy groceries" --description "Milk, eggs, bread"
```

### List All Tasks

To view all tasks, use the `list` command:

```bash
python -m src.interfaces.cli list
```

### Mark a Task as Complete

To mark a task as complete, use the `done` command with the task's ID:

```bash
python -m src.interfaces.cli done --id 1
```

### Mark a Task as Incomplete

To mark a task as incomplete, use the `undone` command with the task's ID:

```bash
python -m src.interfaces.cli undone --id 1
```

### Update a Task

To update a task's title or description, use the `update` command with the task's ID and the fields you want to change:

```bash
python -m src.interfaces.cli update --id 1 --title "Buy organic groceries"
```

### Delete a Task

To delete a task, use the `delete` command with the task's ID:

```bash

python -m src.interfaces.cli delete --id 1
```

# Console To-Do Application

This is a simple, in-memory to-do application with both a Command-Line Interface (CLI) and a Terminal User Interface (TUI).

## Features

-   Add, list, update, delete, and mark tasks as complete.
-   Hexagonal architecture for a clean separation of concerns.
-   Both a CLI and a TUI for interacting with the application.
-   In-memory data storage (tasks are not persisted).

## Getting Started

### Prerequisites

-   Python 3.10+
-   [uv](https://github.com/astral-sh/uv) (a fast Python package installer and resolver)

### 1. Clone the Repository

```bash
git clone https://github.com/yarrbakr/panaversity-hackathon-2-project
cd panaversity-hackathon-2-project
```

### 2. Set Up the Environment

This project uses `uv` to manage the Python environment and dependencies.

**Install `uv`:**

```bash
# For macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# For Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Create and activate the virtual environment:**

```bash
uv venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
uv pip install -e .[test]
```

### 4. Run the Application

You can run the application in two ways:

**a) Terminal User Interface (TUI)**

This provides an interactive, full-screen experience.

```bash
python -m src.interfaces.tui
```

**b) Command-Line Interface (CLI)**

This is a standard command-line interface.

-   **Add a task:**
    ```bash
    python -m src.interfaces.cli add --title "My new task" --description "A description"
    ```
-   **List tasks:**
    ```bash
    python -m src.interfaces.cli list
    ```
-   **Mark a task as complete:**
    ```bash
    python -m src.interfaces.cli done --id 1
    ```
-   And so on for `undone`, `update`, and `delete`.

### 5. Run the Tests

To run the unit and integration tests, use `pytest`:

```bash
pytest
```

### 6. Automated Verification

To run a script that simulates a full user workflow, use `verify.sh`:

```bash
bash verify.sh
```

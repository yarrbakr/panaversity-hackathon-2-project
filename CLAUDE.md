# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Console To-Do Application** built with Python that implements both a Command-Line Interface (CLI) and a Terminal User Interface (TUI). The application follows hexagonal architecture principles with clean separation of concerns.

## Architecture

The project follows **Hexagonal Architecture (Ports and Adapters)** with the following layers:

1. **Domain Layer** (`src/core/domain/`):
   - Contains the `Task` entity using SQLModel
   - Defines the core business objects

2. **Application Layer** (`src/core/application/`):
   - Contains `TodoService` with all business logic
   - Defines `TaskRepository` port interface
   - Contains application services and ports

3. **Infrastructure Layer** (`src/core/infrastructure/`):
   - Implements `InMemoryTaskRepository`
   - Provides concrete implementations of ports

4. **Interfaces Layer** (`src/interfaces/`):
   - **CLI**: Command-line interface with argparse-based commands
   - **TUI**: Textual-based terminal user interface with screens and widgets

## Development Commands

### Environment Setup
```bash
# Install uv (Python package installer)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies (including test dependencies)
uv pip install -e .[test]
```

### Running the Application
```bash
# Terminal User Interface (TUI) - Interactive full-screen experience
python -m src.interfaces.tui

# Command-Line Interface (CLI)
python -m src.interfaces.cli [command] [options]
```

### CLI Commands
```bash
# Add a task
python -m src.interfaces.cli add --title "My new task" --description "A description"

# List tasks
python -m src.interfaces.cli list

# Mark a task as complete
python -m src.interfaces.cli done --id 1

# Mark a task as incomplete
python -m src.interfaces.cli undone --id 1

# Update a task
python -m src.interfaces.cli update --id 1 --title "New title" --description "New description"

# Delete a task
python -m src.interfaces.cli delete --id 1
```

### Testing
```bash
# Run all tests
pytest

# Run a single test file
pytest tests/unit/test_filename.py

# Run tests with coverage
pytest --cov=src

# Run the automated verification script that simulates a full user workflow
bash verify.sh
```

## Key Components

1. **Task Entity** (`src/core/domain/entities.py`):
   - Simple model with id, title, description, completion status, and user_id

2. **TodoService** (`src/core/application/services.py`):
   - Main business logic service with methods for all operations
   - Handles user authentication (though currently using a default user)

3. **InMemoryTaskRepository** (`src/core/infrastructure/in_memory_repository.py`):
   - In-memory storage implementation using a dictionary
   - Implements the TaskRepository port interface

4. **CLI Interface** (`src/interfaces/cli/`):
   - Command-line interface using argparse
   - Supports add, list, done, undone, update, and delete commands

5. **TUI Interface** (`src/interfaces/tui/`):
   - Full-screen terminal user interface using Textual
   - Features task list, header, footer, and modal screens
   - Keyboard shortcuts for all operations
   - Includes confirmation dialogs

## Important Notes

- The application uses in-memory data storage (tasks are not persisted)
- The project uses `uv` for package management instead of pip
- Both CLI and TUI interfaces share the same underlying business logic
- The TUI uses the Textual framework for the terminal user interface
- The CLI uses the Rich library for formatting and tables
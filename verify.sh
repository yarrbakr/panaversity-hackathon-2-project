#!/bin/bash

# This script verifies the functionality of the Console To-Do Application
# by simulating a full user workflow.

# Ensure the script exits if any command fails
set -e

echo "--- Starting Console To-Do App Verification ---"

# --- Setup ---
echo "Initializing environment..."
# Activate the uv virtual environment
source .venv/bin/activate

# Run a single Python script to execute all commands
python - <<END_PYTHON
import sys
from src.core.application.services import TodoService
from src.core.infrastructure.in_memory_repository import InMemoryTaskRepository
from src.interfaces.cli.handlers import add_task, list_tasks, done_task, undone_task, update_task_handler, delete_task_handler
from rich.console import Console

console = Console()
repository = InMemoryTaskRepository()
service = TodoService(repository)

console.print("--- Testing Add and List ---", style="bold blue")
# Add a task
console.print("Adding task 1: Buy groceries", style="blue")
add_task(service, "Buy groceries", "Milk, eggs, bread")

# Add another task
console.print("Adding task 2: Call mom", style="blue")
add_task(service, "Call mom")

# List tasks
console.print("Listing all tasks:", style="blue")
list_tasks(service)

console.print("--- Testing Mark Complete and Incomplete ---", style="bold blue")
# Mark task 1 as complete
console.print("Marking task 1 as complete:", style="blue")
done_task(service, 1)

# List tasks to verify
console.print("Listing tasks after marking task 1 complete:", style="blue")
list_tasks(service)

# Mark task 1 as incomplete
console.print("Marking task 1 as incomplete:", style="blue")
undone_task(service, 1)

# List tasks to verify
console.print("Listing tasks after marking task 1 incomplete:", style="blue")
list_tasks(service)

console.print("--- Testing Update ---", style="bold blue")
# Update task 2
console.print("Updating task 2: Call mom -> Call Mom (urgent)", style="blue")
update_task_handler(service, 2, "Call Mom (urgent)", "Discuss weekend plans")

# List tasks to verify
console.print("Listing tasks after updating task 2:", style="blue")
list_tasks(service)

console.print("--- Testing Delete ---", style="bold blue")
# Delete task 1
console.print("Deleting task 1:", style="blue")
delete_task_handler(service, 1)

# List tasks to verify
console.print("Listing tasks after deleting task 1:", style="blue")
list_tasks(service)

console.print("--- Testing Edge Cases ---", style="bold blue")
console.print("Attempting to delete non-existent task (ID 999):", style="blue")
delete_task_handler(service, 999)

console.print("Attempting to add task with empty title:", style="blue")
add_task(service, "")

console.print("--- Verification Complete ---", style="bold green")
console.print("All simulated commands executed. Please review output for correctness.", style="bold green")
END_PYTHON

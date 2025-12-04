#!/bin/bash

# This script verifies the functionality of the Console To-Do Application
# by simulating a full user workflow.

# Ensure the script exits if any command fails
set -e

echo "--- Starting Console To-Do App Verification ---"

# --- Setup ---
echo "Initializing environment..."
# Assuming uv venv and uv pip install -e . have been run
# For this script, we'll just ensure python -m src.interfaces.cli works
python -c "import sys; sys.path.insert(0, '.'); import src.interfaces.cli.__main__"

echo "--- Testing Add and List ---"
# Add a task
echo "Adding task 1: Buy groceries"
python -m src.interfaces.cli add --title "Buy groceries" --description "Milk, eggs, bread"

# Add another task
echo "Adding task 2: Call mom"
python -m src.interfaces.cli add --title "Call mom"

# List tasks
echo "Listing all tasks:"
python -m src.interfaces.cli list

echo "--- Testing Mark Complete and Incomplete ---"
# Mark task 1 as complete
echo "Marking task 1 as complete:"
python -m src.interfaces.cli done --id 1

# List tasks to verify
echo "Listing tasks after marking task 1 complete:"
python -m src.interfaces.cli list

# Mark task 1 as incomplete
echo "Marking task 1 as incomplete:"
python -m src.interfaces.cli undone --id 1

# List tasks to verify
echo "Listing tasks after marking task 1 incomplete:"
python -m src.interfaces.cli list

echo "--- Testing Update ---"
# Update task 2
echo "Updating task 2: Call mom -> Call Mom (urgent)"
python -m src.interfaces.cli update --id 2 --title "Call Mom (urgent)" --description "Discuss weekend plans"

# List tasks to verify
echo "Listing tasks after updating task 2:"
python -m src.interfaces.cli list

echo "--- Testing Delete ---"
# Delete task 1
echo "Deleting task 1:"
python -m src.interfaces.cli delete --id 1

# List tasks to verify
echo "Listing tasks after deleting task 1:"
python -m src.interfaces.cli list

echo "--- Testing Edge Cases ---"
echo "Attempting to delete non-existent task (ID 999):"
python -m src.interfaces.cli delete --id 999 || true # Expecting error, so don't exit

echo "Attempting to add task with empty title:"
python -m src.interfaces.cli add --title "" || true # Expecting error, so don't exit

echo "--- Verification Complete ---"
echo "All simulated commands executed. Please review output for correctness."

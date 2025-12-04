import pytest
import subprocess
import sys

# Helper function to run CLI commands
def run_cli_command(command_args):
    result = subprocess.run(
        [sys.executable, "-m", "src.interfaces.cli"] + command_args,
        capture_output=True,
        text=True,
        check=False # Don't raise exception for non-zero exit codes
    )
    return result

def test_add_and_list_task():
    # Add a task
    add_result = run_cli_command(["add", "--title", "Test Task", "--description", "This is a test description"])
    assert "Success: Task 'Test Task' added with ID 1." in add_result.stdout
    assert add_result.returncode == 0

    # List tasks
    list_result = run_cli_command(["list"])
    assert "Test Task" in list_result.stdout
    assert "This is a test description" in list_result.stdout
    assert "[bold red]✗[/bold red]" in list_result.stdout # Should be incomplete
    assert list_result.returncode == 0

def test_mark_task_complete_and_incomplete():
    # Add a task
    run_cli_command(["add", "--title", "Task to complete"])

    # Mark as complete
    done_result = run_cli_command(["done", "--id", "1"])
    assert "Success: Task 1 marked as complete." in done_result.stdout
    assert done_result.returncode == 0

    # List and check status
    list_result = run_cli_command(["list"])
    assert "[bold green]✓[/bold green]" in list_result.stdout # Should be complete
    assert list_result.returncode == 0

    # Mark as incomplete
    undone_result = run_cli_command(["undone", "--id", "1"])
    assert "Success: Task 1 marked as incomplete." in undone_result.stdout
    assert undone_result.returncode == 0

    # List and check status
    list_result = run_cli_command(["list"])
    assert "[bold red]✗[/bold red]" in list_result.stdout # Should be incomplete
    assert list_result.returncode == 0

def test_update_task():
    # Add a task
    run_cli_command(["add", "--title", "Original Title", "--description", "Original Description"])

    # Update task
    update_result = run_cli_command(["update", "--id", "1", "--title", "Updated Title", "--description", "Updated Description"])
    assert "Success: Task 1 updated." in update_result.stdout
    assert update_result.returncode == 0

    # List and check updated details
    list_result = run_cli_command(["list"])
    assert "Updated Title" in list_result.stdout
    assert "Updated Description" in list_result.stdout
    assert list_result.returncode == 0

def test_delete_task():
    # Add a task
    run_cli_command(["add", "--title", "Task to delete"])

    # Delete task
    delete_result = run_cli_command(["delete", "--id", "1"])
    assert "Success: Task 1 deleted." in delete_result.stdout
    assert delete_result.returncode == 0

    # List and ensure task is gone
    list_result = run_cli_command(["list"])
    assert "No tasks to show." in list_result.stdout
    assert "Task to delete" not in list_result.stdout
    assert list_result.returncode == 0

def test_non_existent_task_error_messages():
    # Try to operate on a non-existent task
    result = run_cli_command(["done", "--id", "999"])
    assert "Error: Task with ID 999 not found." in result.stdout
    assert result.returncode != 0

    result = run_cli_command(["update", "--id", "999", "--title", "Non Existent"])
    assert "Error: Task with ID 999 not found." in result.stdout
    assert result.returncode != 0

    result = run_cli_command(["delete", "--id", "999"])
    assert "Error: Task with ID 999 not found." in result.stdout
    assert result.returncode != 0

def test_add_task_empty_title_error():
    result = run_cli_command(["add", "--title", ""])
    assert "Error: Title cannot be empty" in result.stdout
    assert result.returncode != 0

def test_invalid_id_format_error():
    result = run_cli_command(["done", "--id", "abc"])
    assert "argument --id: invalid int value: 'abc'" in result.stderr # argparse error message
    assert result.returncode != 0

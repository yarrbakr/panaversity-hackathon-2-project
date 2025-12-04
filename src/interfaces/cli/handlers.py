from typing import Optional
from src.core.application.services import TodoService
from rich.console import Console
from rich.table import Table

console = Console()

def add_task(service: TodoService, title: str, description: Optional[str] = None):
    try:
        task = service.add_task("default_user", title, description)
        console.print(f"Success: Task '{task.title}' added with ID {task.id}.", style="bold green")
    except ValueError as e:
        console.print(f"Error: {e}", style="bold red")

def list_tasks(service: TodoService):
    tasks = service.list_tasks("default_user")
    if not tasks:
        console.print("No tasks to show.", style="bold yellow")
        return

    table = Table(title="To-Do List")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Title", style="bold")
    table.add_column("Description")
    table.add_column("Status", justify="right")

    for task in tasks:
        status = "[bold green]✓[/bold green]" if task.is_complete else "[bold red]✗[/bold red]"
        table.add_row(
            str(task.id),
            task.title,
            task.description or "",
            status,
        )
    
    console.print(table)

def done_task(service: TodoService, task_id: int):
    try:
        task = service.mark_task_complete("default_user", task_id)
        if task:
            console.print(f"Success: Task {task.id} marked as complete.", style="bold green")
        else:
            console.print(f"Error: Task with ID {task_id} not found.", style="bold red")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def undone_task(service: TodoService, task_id: int):
    try:
        task = service.mark_task_incomplete("default_user", task_id)
        if task:
            console.print(f"Success: Task {task.id} marked as incomplete.", style="bold green")
        else:
            console.print(f"Error: Task with ID {task_id} not found.", style="bold red")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def update_task_handler(service: TodoService, task_id: int, title: Optional[str] = None, description: Optional[str] = None):
    try:
        task = service.update_task("default_user", task_id, title, description)
        if task:
            console.print(f"Success: Task {task.id} updated.", style="bold green")
        else:
            console.print(f"Error: Task with ID {task_id} not found.", style="bold red")
    except ValueError as e:
        console.print(f"Error: {e}", style="bold red")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def delete_task_handler(service: TodoService, task_id: int):
    try:
        success = service.delete_task("default_user", task_id)
        if success:
            console.print(f"Success: Task {task_id} deleted.", style="bold green")
        else:
            console.print(f"Error: Task with ID {task_id} not found.", style="bold red")
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

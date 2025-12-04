from textual.app import App, ComposeResult
from textual.binding import Binding
from src.interfaces.tui.widgets.header import AppHeader
from src.interfaces.tui.widgets.footer import AppFooter
from src.interfaces.tui.widgets.task_list import TaskList
from src.interfaces.tui.screens.add_task import AddTaskScreen
from src.interfaces.tui.screens.confirm_delete import ConfirmDeleteScreen
from src.core.application.services import TodoService
from src.core.infrastructure.in_memory_repository import InMemoryTaskRepository

from src.interfaces.tui.screens.confirm_delete import ConfirmDeleteScreen

from src.interfaces.tui.screens.edit_task import EditTaskScreen
from src.interfaces.tui.screens.delete_by_id import DeleteByIdScreen

class TodoApp(App):
    """A Textual To-Do application."""

    TITLE = "To-Do TUI"
    CSS_PATH = "app.css"
    BINDINGS = [
        Binding("a", "add_task", "Add Task"),
        Binding("e", "edit_task", "Edit Task"),
        Binding("d", "delete_task", "Delete Task"),
        Binding("ctrl+i", "delete_by_id", "Delete by ID"),
        Binding("space", "toggle_task_status", "Toggle Status"),
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self):
        super().__init__()
        self.service = TodoService(InMemoryTaskRepository())

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield AppHeader()
        yield TaskList()
        yield AppFooter()

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.update_task_list()

    def update_task_list(self):
        """Update the task list with the latest tasks."""
        task_list = self.query_one(TaskList)
        task_list.clear()
        tasks = self.service.list_tasks("default_user")
        for task in tasks:
            status = "✓" if task.is_complete else "✗"
            task_list.add_row(str(task.id), task.title, task.description or "", status)

    def action_toggle_task_status(self) -> None:
        """An action to toggle the completion status of a task."""
        task_list = self.query_one(TaskList)
        if task_list.cursor_row >= 0:
            task_id = int(task_list.get_row_at(task_list.cursor_row)[0])
            task = self.service.get_task("default_user", task_id)
            if task:
                if task.is_complete:
                    self.service.mark_task_incomplete("default_user", task_id)
                else:
                    self.service.mark_task_complete("default_user", task_id)
                self.update_task_list()

    def action_add_task(self) -> None:
        """An action to add a new task."""
        def add_task_callback(data):
            if data:
                title, description = data
                self.service.add_task("default_user", title, description)
                self.update_task_list()
        
        self.push_screen(AddTaskScreen(), add_task_callback)

    def action_delete_task(self) -> None:
        """An action to delete a task."""
        task_list = self.query_one(TaskList)
        if task_list.cursor_row >= 0:
            task_id = int(task_list.get_row_at(task_list.cursor_row)[0])
            task = self.service.get_task("default_user", task_id)
            if task:
                def delete_task_callback(confirmed: bool):
                    if confirmed:
                        self.service.delete_task("default_user", task_id)
                        self.update_task_list()
                
                self.push_screen(ConfirmDeleteScreen(task.title), delete_task_callback)

    def action_edit_task(self) -> None:
        """An action to edit a task."""
        task_list = self.query_one(TaskList)
        if task_list.cursor_row >= 0:
            task_id = int(task_list.get_row_at(task_list.cursor_row)[0])
            task = self.service.get_task("default_user", task_id)
            if task:
                def edit_task_callback(data):
                    if data:
                        title, description = data
                        self.service.update_task("default_user", task_id, title, description)
                        self.update_task_list()
                
                self.push_screen(EditTaskScreen(task.title, task.description or ""), edit_task_callback)

    def action_delete_by_id(self) -> None:
        """An action to delete a task by its ID."""
        def delete_by_id_callback(task_id: int):
            if task_id is not None:
                task = self.service.get_task("default_user", task_id)
                if task:
                    def delete_task_callback(confirmed: bool):
                        if confirmed:
                            self.service.delete_task("default_user", task_id)
                            self.update_task_list()
                    
                    self.push_screen(ConfirmDeleteScreen(task.title), delete_task_callback)
        
        self.push_screen(DeleteByIdScreen(), delete_by_id_callback)

if __name__ == "__main__":
    app = TodoApp()
    app.run()

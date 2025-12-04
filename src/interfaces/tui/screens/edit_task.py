from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Input, Button

class EditTaskScreen(ModalScreen):
    """A modal screen for editing a task."""

    def __init__(self, task_title: str, task_description: str) -> None:
        super().__init__()
        self.task_title = task_title
        self.task_description = task_description

    def compose(self) -> ComposeResult:
        yield Input(value=self.task_title, id="title")
        yield Input(value=self.task_description, id="description")
        yield Button("Update Task", variant="primary", id="update")
        yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "update":
            title = self.query_one("#title", Input).value
            description = self.query_one("#description", Input).value
            if title:
                self.dismiss((title, description))
            else:
                self.dismiss()
        else:
            self.dismiss()

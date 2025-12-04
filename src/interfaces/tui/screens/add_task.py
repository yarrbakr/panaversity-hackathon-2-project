from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Input, Button

class AddTaskScreen(ModalScreen):
    """A modal screen for adding a new task."""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Title", id="title")
        yield Input(placeholder="Description", id="description")
        yield Button("Add Task", variant="primary", id="add")
        yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add":
            title = self.query_one("#title", Input).value
            description = self.query_one("#description", Input).value
            if title:
                self.dismiss((title, description))
            else:
                self.dismiss()
        else:
            self.dismiss()

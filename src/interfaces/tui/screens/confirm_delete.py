from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Label

class ConfirmDeleteScreen(ModalScreen):
    """A modal screen for confirming task deletion."""

    def __init__(self, task_title: str) -> None:
        super().__init__()
        self.task_title = task_title

    def compose(self) -> ComposeResult:
        yield Label(f"Are you sure you want to delete '{self.task_title}'?")
        yield Button("Delete", variant="error", id="delete")
        yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "delete":
            self.dismiss(True)
        else:
            self.dismiss(False)

from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Input, Button, Label

class DeleteByIdScreen(ModalScreen):
    """A modal screen for deleting a task by its ID."""

    def compose(self) -> ComposeResult:
        yield Label("Enter the ID of the task to delete:")
        yield Input(placeholder="Task ID", id="task_id")
        yield Button("Delete", variant="error", id="delete")
        yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "delete":
            task_id_input = self.query_one("#task_id", Input).value
            if task_id_input.isdigit():
                self.dismiss(int(task_id_input))
            else:
                self.dismiss()
        else:
            self.dismiss()

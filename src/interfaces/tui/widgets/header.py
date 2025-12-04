from textual.widgets import Header

class AppHeader(Header):
    """A header with the application title."""

    def __init__(self) -> None:
        super().__init__()
        self.tall = False

    def on_mount(self) -> None:
        self.update("To-Do TUI")

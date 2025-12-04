from textual.widgets import DataTable

class TaskList(DataTable):
    """A DataTable for displaying tasks."""

    def on_mount(self) -> None:
        self.add_columns("ID", "Title", "Description", "Status")

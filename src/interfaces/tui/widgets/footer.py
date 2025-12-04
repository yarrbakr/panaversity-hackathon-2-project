from textual.widgets import Footer

class AppFooter(Footer):
    """A footer with key bindings."""

    def on_mount(self) -> None:
        self.update("a: Add | e: Edit | d: Delete | space: Toggle | q: Quit")

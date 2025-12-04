from src.interfaces.tui.app import TodoApp

def main():
    """Run the TUI application."""
    app = TodoApp()
    app.run()

if __name__ == "__main__":
    main()

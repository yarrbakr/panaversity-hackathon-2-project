# Quickstart: Terminal User Interface (TUI)

This document provides a quick guide to setting up and running the Terminal User Interface (TUI) for the To-Do Application.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Set up Python environment with `uv`:**
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install -e .
    ```
3.  **Install TUI dependencies:**
    ```bash
    uv pip install textual
    ```

## Running the TUI

To start the TUI application, run the following command:

```bash
python -m src.interfaces.tui
```

This will launch the full-screen interactive terminal interface.

## Key Bindings

-   **`a`**: Add a new task.
-   **`e`**: Edit the selected task.
-   **`d`**: Delete the selected task.
-   **`space`**: Toggle the completion status of the selected task.
-   **`q`**: Quit the application.
-   **Up/Down Arrows**: Navigate the task list.

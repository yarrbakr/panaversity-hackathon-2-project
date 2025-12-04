# Feature Specification: Terminal User Interface (TUI)

**Feature Branch**: `002-tui-interface`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Implement a Terminal User Interface (TUI) for the to-do application using Textual."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - View and Add Tasks (Priority: P1)

As a user, I want to see all my tasks in a list when I start the application and be able to add new tasks through a form, so I can manage my to-do list interactively.

**Why this priority**: This provides the core functionality of viewing and adding tasks in a user-friendly, interactive way.

**Independent Test**: A user can start the TUI, see a list of tasks (or an empty state), press a key to open an "Add Task" form, fill it out, submit it, and see the new task appear in the list.

**Acceptance Scenarios**:

1.  **Given** the TUI application is started, **When** the main screen is displayed, **Then** a list of all current tasks is shown.
2.  **Given** the main screen is displayed, **When** I press the 'a' key, **Then** a form appears to enter a new task's title and description.
3.  **Given** the "Add Task" form is open, **When** I fill in the title and description and submit the form, **Then** the form closes and the new task is visible in the task list.

---

### User Story 2 - Change Task Status and Delete (Priority: P2)

As a user, I want to quickly mark tasks as complete or incomplete and delete tasks I no longer need, using single key presses.

**Why this priority**: This makes managing the task list fast and efficient.

**Independent Test**: A user can select a task in the list, press a key to toggle its completion status, and see the UI update. They can also press another key to delete the selected task, which then disappears from the list.

**Acceptance Scenarios**:

1.  **Given** a task is selected in the list, **When** I press the 'space' key, **Then** the task's completion status is toggled, and the UI reflects the change.
2.  **Given** a task is selected in the list, **When** I press the 'd' key, **Then** a confirmation prompt appears, and upon confirming, the task is removed from the list.

---

### User Story 3 - Edit a Task (Priority: P3)

As a user, I want to edit the title and description of an existing task.

**Why this priority**: Allows for correcting mistakes or updating task details as things change.

**Independent Test**: A user can select a task, press a key to open an "Edit Task" form pre-filled with the task's data, modify the data, submit the form, and see the updated task in the list.

**Acceptance Scenarios**:

1.  **Given** a task is selected in the list, **When** I press the 'e' key, **Then** a form appears, pre-filled with the selected task's title and description.
2.  **Given** the "Edit Task" form is open, **When** I change the title and submit, **Then** the form closes and the task list shows the updated title.

### Edge Cases

-   The task list should display a clear message when it is empty.
-   The UI should handle long task titles and descriptions gracefully (e.g., by truncating or wrapping text).
-   The application should provide a clear way to quit (e.g., pressing 'q' or Ctrl+C).

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The TUI MUST display all tasks in a scrollable list upon startup.
-   **FR-002**: The TUI MUST provide a key binding (e.g., 'a') to open a modal form for adding a new task.
-   **FR-003**: The TUI MUST provide a key binding (e.g., 'space') to toggle the completion status of the currently selected task.
-   **FR-004**: The TUI MUST provide a key binding (e.g., 'd') to delete the currently selected task, with a confirmation step.
-   **FR-005**: The TUI MUST provide a key binding (e.g., 'e') to open a modal form for editing the currently selected task.
-   **FR-006**: The TUI MUST provide a key binding (e.g., 'q') to quit the application.
-   **FR-007**: The task list MUST automatically refresh after a task is added, updated, or deleted.

### Key Entities *(include if feature involves data)*

-   This feature uses the existing **Task** entity and does not introduce new ones.

## Constitution Alignment *(mandatory)*

-   **Spec-First Law**: This document fulfills the requirement for a specification.
-   **Hexagonal Architecture**: This spec introduces a new TUI interface in `src/interfaces/tui`, which will be completely separate from the core domain logic and will use the existing `TodoService`.
-   **State Isolation**: The TUI will be stateless and will interact with the core logic, which manages the application state.
-   **I/O Ban**: All core logic remains free of I/O operations. The TUI handles all user input and display output.
-   **User-Centricity**: The TUI will interact with the `TodoService`, which already supports the `user_id` parameter.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: A user can perform all core to-do operations (add, view, update, delete, complete) exclusively through the TUI without needing to restart the application.
-   **SC-002**: The TUI provides immediate visual feedback for all user actions (e.g., highlighting selection, showing forms, updating status).
-   **SC-003**: The state of the tasks displayed in the TUI is always consistent with the state managed by the core service.
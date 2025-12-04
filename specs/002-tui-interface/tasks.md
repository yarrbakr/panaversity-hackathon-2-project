# Tasks: Terminal User Interface (TUI)

**Input**: Design documents from `/specs/002-tui-interface/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Core Logic**: `src/core/`
- **Interfaces**: `src/interfaces/tui/`
- **Tests**: `tests/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for the TUI feature.

- [ ] T001 [P] Add `textual` and `pytest-textual-snapshot` to `pyproject.toml` under the `[project.dependencies]` and `[project.optional-dependencies.test]` sections, respectively.
- [ ] T002 [P] Create the directory structure for the TUI interface: `src/interfaces/tui/widgets`, `src/interfaces/tui/screens`, and `tests/integration/tui`.

---

## Phase 2: Foundational (TUI Structure)

**Purpose**: Core TUI infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T003 Create the main TUI app file `src/interfaces/tui/app.py` with a basic `App` class that will contain the TUI.
- [ ] T004 [P] Create a `Header` widget in `src/interfaces/tui/widgets/header.py` to display the application title.
- [ ] T005 [P] Create a `Footer` widget in `src/interfaces/tui/widgets/footer.py` to display key bindings and other contextual information.
- [ ] T006 Create a basic `DataTable` widget in `src/interfaces/tui/widgets/task_list.py` for displaying tasks.
- [ ] T007 [P] Create a CSS file `src/interfaces/tui/app.css` for basic styling of the TUI components.
- [ ] T008 Compose the main app layout in `src/interfaces/tui/app.py` using the Header, Task List, and Footer widgets.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - View and Add Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to see their tasks and add new ones through an interactive form.
**Independent Test**: A user can start the TUI, see a list of tasks, and add a new task that appears in the list.

### Implementation for User Story 1

- [ ] T009 [US1] Implement the logic in `src/interfaces/tui/app.py` to fetch tasks from the `TodoService` and populate the `DataTable` on mount.
- [ ] T010 [US1] Create a modal `Screen` for adding a new task in `src/interfaces/tui/screens/add_task.py`. This screen should contain a form with input fields for title and description.
- [ ] T011 [US1] Implement the 'a' key binding in `src/interfaces/tui/app.py` to push the `AddTaskScreen` as a modal dialog.
- [ ] T012 [US1] Implement the form submission logic in `AddTaskScreen` to call the `add_task` method of the `TodoService` and then refresh the main task list.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Change Task Status and Delete (Priority: P2)

**Goal**: Allow users to quickly manage tasks by changing their status or deleting them.
**Independent Test**: A user can select a task, press a key to toggle its status, and see the change. They can also delete a task after confirming.

### Implementation for User Story 2

- [ ] T013 [US2] Implement the 'space' key binding in `src/interfaces/tui/app.py` to toggle the completion status of the currently selected task in the `DataTable`.
- [ ] T014 [US2] Create a confirmation dialog `Screen` in `src/interfaces/tui/screens/confirm_delete.py` to ask the user for confirmation before deleting a task.
- [ ] T015 [US2] Implement the 'd' key binding in `src/interfaces/tui/app.py` to push the `ConfirmDeleteScreen`.
- [ ] T016 [US2] Implement the deletion logic in `ConfirmDeleteScreen` to call the `delete_task` method of the `TodoService` upon confirmation and refresh the task list.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Edit a Task (Priority: P3)

**Goal**: Allow users to edit the details of an existing task.
**Independent Test**: A user can select a task, open an edit form, change the details, and see the updated task in the list.

### Implementation for User Story 3

- [ ] T017 [US3] Create a modal `Screen` for editing a task in `src/interfaces/tui/screens/edit_task.py`, with a form pre-filled with the task's data.
- [ ] T018 [US3] Implement the 'e' key binding in `src/interfaces/tui/app.py` to push the `EditTaskScreen` with the data of the currently selected task.
- [ ] T019 [US3] Implement the form submission logic in `EditTaskScreen` to call the `update_task` method of the `TodoService` and refresh the task list.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [ ] T020 [P] Add snapshot tests for the main app screen and modal screens in `tests/integration/tui/`.
- [ ] T021 [P] Refine the TUI layout and styling in `src/interfaces/tui/app.css` for a better user experience.
- [ ] T022 Create a `__main__.py` file in `src/interfaces/tui/` to allow running the TUI app as a module (`python -m src.interfaces.tui`).

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion. BLOCKS all user stories.
- **User Stories (Phase 3-5)**: Depend on Foundational phase completion.
- **Polish (Phase 6)**: Depends on all user stories being complete.

### User Story Dependencies

- All user stories are independent and can be implemented in any order after the Foundational phase is complete, but following the P1-P3 priority is recommended.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently. The TUI should be able to display and add tasks.

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready.
2.  Add User Story 1 → Test independently → MVP is ready.
3.  Add User Story 2 → Test independently.
4.  Add User Story 3 → Test independently.
5.  Each story adds value without breaking previous stories.

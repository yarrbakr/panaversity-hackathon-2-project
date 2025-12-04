# Tasks: Console To-Do Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Core Logic**: `src/core/`
- **Interfaces**: `src/interfaces/cli/`
- **Tests**: `tests/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize Python project with `uv` by running `uv venv` and creating a `src` directory.
- [x] T002 [P] Create `pyproject.toml` and add dependencies: `sqlmodel`, `rich`, `pytest`.
- [x] T003 [P] Create project directory structure: `src/core/application/ports`, `src/core/domain`, `src/core/infrastructure`, `src/interfaces/cli`, `tests/unit`, `tests/integration`.

---

## Phase 2: Foundational (Core Domain)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Define the `Task` entity using SQLModel in `src/core/domain/entities.py`.
- [x] T005 Define the abstract `TaskRepository` interface (port) in `src/core/application/ports/task_repository.py`.
- [x] T006 Implement the `InMemoryTaskRepository` adapter in `src/core/infrastructure/in_memory_repository.py`.
- [x] T007 Define the `TodoService` class in `src/core/application/services.py` with empty methods based on the `core_service.md` contract.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks and view their complete list of tasks.
**Independent Test**: A user can start the app, add a task, and see it in the list.

### Implementation for User Story 1

- [x] T008 [US1] Implement the `add_task` use case in `src/core/application/services.py`.
- [x] T009 [US1] Implement the `list_tasks` use case in `src/core/application/services.py`.
- [x] T010 [US1] Implement the `add` command handler in `src/interfaces/cli/handlers.py`.
- [x] T011 [US1] Implement the `list` command handler in `src/interfaces/cli/handlers.py`.
- [x] T012 [US1] Implement the main CLI entry point with `argparse` in `src/interfaces/cli/__main__.py` to handle the `add` and `list` commands.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Change Task Status (Priority: P2)

**Goal**: Allow users to mark tasks as complete or incomplete.
**Independent Test**: A user can mark a task as done and see its status change, and then mark it as not done.

### Implementation for User Story 2

- [x] T013 [US2] Implement the `mark_task_complete` use case in `src/core/application/services.py`.
- [x] T014 [US2] Implement the `mark_task_incomplete` use case in `src/core/application/services.py`.
- [x] T015 [US2] Implement the `done` command handler in `src/interfaces/cli/handlers.py`.
- [x] T016 [US2] Implement the `undone` command handler in `src/interfaces/cli/handlers.py`.
- [x] T017 [US2] Update `src/interfaces/cli/__main__.py` to handle the `done` and `undone` commands.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Edit and Delete Tasks (Priority: P3)

**Goal**: Allow users to edit the details of a task or remove it completely.
**Independent Test**: A user can update a task's title/description and delete a task.

### Implementation for User Story 3

- [x] T018 [US3] Implement the `update_task` use case in `src/core/application/services.py`.
- [x] T019 [US3] Implement the `delete_task` use case in `src/core/application/services.py`.
- [x] T020 [US3] Implement the `update` command handler in `src/interfaces/cli/handlers.py`.
- [x] T021 [US3] Implement the `delete` command handler in `src/interfaces/cli/handlers.py`.
- [x] T022 [US3] Update `src/interfaces/cli/__main__.py` to handle the `update` and `delete` commands.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [x] T023 [P] Refactor CLI output to use the `rich` library for formatted tables and colors in `src/interfaces/cli/handlers.py`.
- [x] T024 [P] Add comprehensive unit tests for all service methods in `tests/unit/`.
- [x] T025 [P] Add integration tests for the CLI commands in `tests/integration/`.
- [x] T026 Create a verification script `verify.sh` to run a full user workflow, simulating the commands from `quickstart.md`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion. BLOCKS all user stories.
- **User Stories (Phase 3-5)**: Depend on Foundational phase completion. Can be implemented sequentially (P1 → P2 → P3) or in parallel if staffed.
- **Polish (Phase 6)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2).
- **User Story 2 (P2)**: Can start after Foundational (Phase 2).
- **User Story 3 (P3)**: Can start after Foundational (Phase 2).

### Within Each User Story

- Core service logic should be implemented before the interface handler.
- The main CLI entry point is updated last within each story phase.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently. The app should be able to add and list tasks.

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready.
2.  Add User Story 1 → Test independently → MVP is ready.
3.  Add User Story 2 → Test independently.
4.  Add User Story 3 → Test independently.
5.  Each story adds value without breaking previous stories.

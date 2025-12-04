# Implementation Plan: Terminal User Interface (TUI)

**Branch**: `002-tui-interface` | **Date**: 2025-12-05 | **Spec**: ./spec.md
**Input**: Feature specification from `/specs/002-tui-interface/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation of a Terminal User Interface (TUI) for the to-do application using the Textual library. The TUI will provide an interactive, full-screen experience for managing tasks, including viewing, adding, editing, deleting, and changing the status of tasks. The TUI will be a new interface that leverages the existing core business logic (`TodoService`), ensuring adherence to the Hexagonal Architecture.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13+ (Managed by `uv`)
**Primary Dependencies**: Textual (for the TUI), SQLModel (for data modeling)
**Storage**: In-memory dictionary (reusing existing infrastructure)
**Testing**: pytest, pytest-textual-snapshot (for TUI snapshot testing)
**Target Platform**: Linux console
**Project Type**: Monorepo (core, interfaces, frontend)
**Performance Goals**: Responsive TUI interaction (sub-second response times for all user actions)
**Constraints**: I/O Ban in `src/core`, TUI must use existing `TodoService`
**Scale/Scope**: Single user, in-memory task list

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Spec-First Law**: ✅ A detailed specification (`spec.md`) drives this feature.
- **Hexagonal Architecture**: ✅ The plan introduces a new TUI interface in `src/interfaces/tui`, which will be completely separate from the core domain logic and will use the existing `TodoService`.
- **State Isolation**: ✅ The TUI will be stateless and will interact with the core logic, which manages the application state.
- **I/O Ban**: ✅ All core logic remains free of I/O operations. The TUI handles all user input and display output.
- **User-Centricity**: ✅ The TUI will interact with the `TodoService`, which already supports the `user_id` parameter.

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
```text
/
├── specs/
│   ├── features/
│   ├── api/
│   ├── database/
│   └── ui/
├── src/
│   ├── core/      # Business Logic - Pure Python, No I/O
│   └── interfaces/ # cli/, api/, mcp/
├── frontend/      # Next.js - Phase II+
└── tests/
    ├── contract/
    ├── integration/
    └── unit/
```

**Structure Decision**: The project structure is fixed by the constitution. All features must adhere to this layout.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

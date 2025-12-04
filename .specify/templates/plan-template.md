# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13+ (Managed by `uv`)
**Primary Dependencies**: SQLModel
**Storage**: [if applicable, e.g., PostgreSQL, files or N/A]
**Testing**: [e.g., pytest or NEEDS CLARIFICATION]
**Target Platform**: [e.g., Linux server, WASM or NEEDS CLARIFICATION]
**Project Type**: Monorepo (core, interfaces, frontend)
**Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]
**Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]
**Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Spec-First Law**: Does a specification in `/specs` drive this feature?
- **Hexagonal Architecture**: Is the core domain (`/src/core`) fully isolated from interfaces (`/src/interfaces`)?
- **State Isolation**: Is application state managed externally and injected into the core?
- **I/O Ban**: Does the code in `/src/core` contain ZERO `print`, `input`, or direct HTTP calls?
- **User-Centricity**: Do all core methods accept a `user_id` parameter?

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

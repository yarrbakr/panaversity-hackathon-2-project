<!--
Sync Impact Report

- Version change: None -> 1.0.0
- List of modified principles: N/A (Initial creation)
- Added sections:
  - Core Principles
  - Key Standards
  - Constraints & Success Criteria
  - Governance
  
- Removed sections: N/A
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# PANAVERSITY-HACKATHON (Evolutionary Architecture: CLI -> Web -> AI Agent -> Cloud Native) Constitution

## Core Principles

### I. The "Spec-First" Law
No code is written manually. All implementation originates from Markdown specifications in the `/specs` folder. The Source of Truth is the Spec, not the Code.

### II. Hexagonal Architecture (Ports & Adapters)
The "Core Domain" (Todo Logic) must remain isolated from the "Presentation Layer" (CLI/Web/Chat).
- Phase I (CLI) is treated as an "Interface" to the domain.
- Phase II (Web) is treated as an "Interface" to the domain.
- Phase III (MCP/AI) is treated as an "Interface" to the domain.

### III. State Isolation
The application logic must be stateless. State persistence (Memory/DB/Kafka) is an external dependency injected into the core.

### IV. Event-Driven Mindset
Operations should be designed as events (e.g., "Task Created") rather than just database writes, preparing the system for Phase V (Kafka/Dapr).

## Key Standards

- **Monorepo Structure**: Strictly adhere to the Spec-Kit Plus directory layout:
    - `/.spec-kit/` (Configuration)
    - `/specs/` (features/, api/, database/, ui/)
    - `/src/core/` (Business Logic - Pure Python, No I/O)
    - `/src/interfaces/` (cli/, api/, mcp/)
    - `/frontend/` (Next.js - Phase II+)
- **Technology Stack**:
    - Language: Python 3.13+ (Managed by `uv`)
    - ORM: SQLModel (Used in Core for Pydantic models, even for in-memory Phase I)
    - Auth: Better Auth / JWT concepts (User ID must be a parameter in Core methods from Day 1, even if mocked in CLI).
- **Documentation**:
    - Root `CLAUDE.md` for global context.
    - Sub-directory `CLAUDE.md` files for specific layer context (Frontend vs Backend).

## Constraints & Success Criteria

- **I/O Ban**: The `/src/core` directory is strictly forbidden from using `print()`, `input()`, or direct HTTP calls. It must return raw data objects (DTOs/Dictionaries).
- **Tooling**: All Docker/Kubernetes operations (Phase IV) must be performed via AI Assistants (Gordon/kubectl-ai), defined via Specs.
- **User-Centricity**: Every Core method must accept a `user_id` argument to support Multi-Tenancy (Phase II) and RAG Context (Phase III) immediately.
- **Success**: This constitution serves as the immutable law for the project lifecycle. It defines the workflow (Spec -> AI -> Code -> Verify) and prevents technical debt by enforcing separation of concerns (Data/View/Control).

## Governance

This Constitution is the supreme governing document for this project. It dictates the principles, standards, and constraints that all contributors MUST follow. All development artifacts, including specifications, code, and documentation, must comply with this constitution.

The defined workflow is: Spec Update -> AI Code Prompt -> Implementation -> Verification.

**Version**: 1.0.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-05
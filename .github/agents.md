# agents.md

## Purpose
Guidelines for AI/code agents working in this monorepo.

## Monorepo Overview
- **Client**: Vite + React + TypeScript + shadcn/ui + Redux Toolkit + RTK Query
- **Server**: FastAPI + Uvicorn (Python)

## Repository Layout (expected)
```text
/
├─ apps/
│  ├─ client/          # Frontend app
│  └─ server/          # FastAPI backend
├─ .github/
│  └─ agents.md
└─ README.md
```

## Agent Operating Rules
1. Keep changes minimal and scoped to the requested task.
2. Prefer existing patterns over introducing new architecture.
3. Do not rename/move files unless required.
4. Update docs when behavior, setup, or API contracts change.
5. Keep commits logically atomic.

## Client Standards (Vite React TS)
- Use strict TypeScript; avoid `any`.
- Prefer functional components and hooks.
- Use **Redux Toolkit** slices for state logic.
- Use **RTK Query** for server data fetching/caching.
- Use shadcn/ui components and existing design tokens.
- Keep UI components presentational; business logic in hooks/services.
- Name files in snake_case format: `my_component.tsx`

## Server Standards (FastAPI)
- Use Pydantic models for request/response schemas.
- Keep route handlers thin; move logic to service modules.
- Use dependency injection for shared resources.
- Validate input and return explicit HTTP errors.
- Keep async patterns consistent (`async def` where applicable).

## API Contract Practices
- Maintain clear DTO/schema boundaries between client and server.
- When API changes, update:
    - FastAPI schema/models
    - Client RTK Query endpoints/types
    - Relevant docs/examples

## Local Development Commands (typical)
### Client
```bash
cd apps/client
yarn install
yarn run dev
yarn run build
yarn run test
```

### Server
```bash
cd apps/server
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest
```

## Quality Checklist Before Merge
- Client builds and lints successfully.
- Server starts and tests pass.
- Types are consistent across boundaries.
- No dead code, debug logs, or commented blocks left behind.
- Documentation updated for any new setup/env vars/routes.

## Environment Variables
- Never commit secrets.
- Keep `.env.example` updated when adding variables.
- Use separate env files for client and server as needed.

## PR Expectations
- Clear summary of what changed and why.
- List impacted apps (`client`, `server`, `shared`).
- Include manual test steps.
- Include screenshots/GIFs for UI changes.

## Non-Goals
- No broad refactors without explicit request.
- No dependency migrations unless task requires it.
- No speculative optimizations.
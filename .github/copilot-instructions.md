## Repository snapshot

- Project: efootball-feeder (feature-first workspace)
- Key files:
  - `spec.yaml` — RapidAPI configuration and example endpoint(s).
  - `env` — environment variables (contains `RAPIDAPI_KEY` placeholder).
  - `memory/context.md` — current working feature metadata (feature id, status).
  - `plans/001-rapidapi-efootball-fetch/plan-001.md` and `specs/001-rapidapi-efootball-fetch/*` — feature plan and specs with SPECPULSE_METADATA headers.
  - `efootball-feeder/.specpulse/` — tool-specific docs and artifacts.

## Purpose for an AI coding agent

Provide immediate, project-specific guidance so an AI contributor can:
- Understand the planned feature (RapidAPI e-football fetch).
- Locate where to implement code for the feature and how the integration should behave.
- Follow repository conventions (feature directory structure and SPECPULSE metadata).

## Big picture (what to know first)

- This repository is organized around features. The active feature is `001-rapidapi-efootball-fetch` (see `memory/context.md`).
- `spec.yaml` describes the external API surface used by the project. Example:

  - `apis[0].base_url` = `https://api-football-v1.p.rapidapi.com/v3`
  - Headers must include `X-RapidAPI-Key: ${RAPIDAPI_KEY}` and `X-RapidAPI-Host: api-football-v1.p.rapidapi.com` (see `spec.yaml`).

- Implementation should fetch fixtures using the described endpoints and respect the query parameters present in `spec.yaml` (e.g., `league`, `season`). The project currently contains plans/specs but not a concrete implementation folder — create source under a new language-specific subfolder (e.g., `services/` or `src/feature-001/`).

## Project-specific conventions and patterns

- Feature directories use numeric prefixes and the feature slug: `001-rapidapi-efootball-fetch`.
- Plan/spec files include a SPECPULSE metadata block at the top. Preserve and update that block when editing specs or plan documents (it contains keys like `FEATURE_DIR`, `FEATURE_ID`, `STATUS`).
- Secrets/API keys are stored in the `env` file for local development. Use environment variables (do not commit secrets to git). Example: `RAPIDAPI_KEY` in `env` is referenced by `spec.yaml` headers as `${RAPIDAPI_KEY}`.

## Integration points & external dependencies

- RapidAPI (api-football-v1) is the primary external dependency. Authentication and host headers must match the `spec.yaml` template.
- No package manifest or language-specific runner found — the repository is a feature scaffold. When you add implementation code, also add a minimal manifest (`package.json`, `pyproject.toml`, etc.) and a small README in the feature folder explaining how to run it.

## How to approach edits (concrete examples)

- If you need to implement the fetcher, follow these steps:
  1. Create a new implementation folder under `services/feature-001` or `src/feature-001`.
  2. Add an entry point that reads `RAPIDAPI_KEY` from environment variables and calls `${base_url}/fixtures` with the query params from `spec.yaml`.
  3. Add a tiny README under that folder describing how to run locally and where to add tests.

- When updating specs or plans, update the SPECPULSE_METADATA block at the top of the markdown file. Example fields: `FEATURE_DIR`, `FEATURE_ID`, `PLAN_ID`, `STATUS`.

## Developer workflows (what's discoverable)

- No build/test commands are present yet. Before adding them, include a short `README.md` with the exact commands required to run the new code (examples: `python -m venv .venv; .\.venv\Scripts\Activate; pip install -r requirements.txt` for Python, or `npm install && npm run start` for Node).
- Local env: copy `env` to `.env` (or export to your shell) and set `RAPIDAPI_KEY`. The header template in `spec.yaml` expects `${RAPIDAPI_KEY}`.

## What to reference in code and docs

- Use `spec.yaml` as the single source of truth for API endpoints and required headers.
- Use `memory/context.md` to confirm the active feature and status before making wide changes.
- Keep plan/spec changes aligned with the SPECPULSE_METADATA block.

## Quick checklist for AI edits

- [ ] Locate the active feature in `memory/context.md`.
- [ ] Follow `spec.yaml` for API details (base_url, headers, sample query params).
- [ ] Keep secrets out of commits; read `RAPIDAPI_KEY` from environment.
- [ ] Add a small README and a language-appropriate manifest when you add implementation code.

If anything above is unclear or you'd like me to include starter code (Python/Node) or add CI/test scaffolding, tell me which language you prefer and I'll add an implementation example and minimal test harness.

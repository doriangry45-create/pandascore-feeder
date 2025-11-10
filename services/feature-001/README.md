# E-Football Fixtures Fetcher (Feature 001)

Minimal RapidAPI e-football fixture fetcher for `efootball-feeder` project.

## Quick Start

### 1. Setup environment (PowerShell)
```powershell
# Copy env to .env if not already done
copy env .env

# Create and activate virtual env
python -m venv .venv
.\.venv\Scripts\Activate

# Install dependencies
pip install -r services\feature-001\requirements.txt
```

### 2. Run fetcher
```powershell
# Fetch Premier League 2023 fixtures (default)
python services\feature-001\main.py

# Custom league/season
python services\feature-001\main.py --league 39 --season 2024 --output my_fixtures.json
```

### 3. Run tests
```powershell
pytest services\feature-001\tests\
```

## Files

- `main.py` — EFootballFetcher class + CLI entry point
- `requirements.txt` — Dependencies (requests, pytest)
- `tests/test_main.py` — Unit tests (mock-based, no network calls)
- `README.md` — This file

## API Details

**Base URL**: `https://api-football-v1.p.rapidapi.com/v3`  
**Endpoint**: `/fixtures`  
**Headers**: `X-RapidAPI-Key` and `X-RapidAPI-Host` (loaded from env)  
**Default Query**: `league=39` (Premier League), `season=2023`

See `spec.yaml` in repo root for full API specification.

## Environment

Ensure `RAPIDAPI_KEY` is set:
```powershell
$env:RAPIDAPI_KEY = "your_key_here"
# Or load from .env
```

## Status

- [x] Fetcher implementation
- [x] Error handling (network, env validation)
- [x] CLI with --league, --season, --output options
- [x] Unit tests with mocking
- [ ] Integration tests (requires live API)
- [ ] CI/CD pipeline (TODO)

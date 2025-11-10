# E-Football Fixtures Fetcher (Feature 001)

Minimal RapidAPI e-football fixture fetcher for `efootball-feeder` project with Flask web UI.

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

### 2. Option A: Run Flask Web UI (Recommended)
```powershell
# Start Flask server
python services\feature-001\app.py

# Open browser and go to:
# http://localhost:5000
```

Dashboard features:
- 🏆 Select league (Premier League, La Liga, Serie A, Bundesliga, Ligue 1, World Cup)
- 📅 Select season (2015-2025)
- ⚽ Browse fixtures with live scores
- 📊 View match status (Not Started, Live, Finished)
- 💾 Export fixtures to JSON

### 3. Option B: Run CLI Fetcher
```powershell
# Fetch Premier League 2023 fixtures (default)
python services\feature-001\main.py

# Custom league/season
python services\feature-001\main.py --league 39 --season 2024 --output my_fixtures.json
```

### 4. Run Tests
```powershell
pytest services\feature-001\tests\
```

## Files

- `app.py` — Flask web server + REST API
- `main.py` — EFootballFetcher class + CLI entry point
- `templates/index.html` — Beautiful responsive dashboard
- `requirements.txt` — Dependencies (requests, flask, pytest)
- `tests/test_main.py` — Unit tests (mock-based, no network calls)
- `README.md` — This file

## API Details

**Base URL**: `https://api-football-v1.p.rapidapi.com/v3`  
**Endpoint**: `/fixtures`  
**Headers**: `X-RapidAPI-Key` and `X-RapidAPI-Host` (loaded from env)  
**Default Query**: `league=39` (Premier League), `season=2023`

See `spec.yaml` in repo root for full API specification.

## REST API Endpoints (Flask)

```
POST /api/fixtures
  Body: { "league": 39, "season": 2023 }
  Response: { "status": "success", "count": N, "fixtures": [...] }

GET /api/leagues
  Response: [{ "id": 39, "name": "Premier League (England)" }, ...]

GET /api/health
  Response: { "status": "healthy", "api_key_set": true }
```

## Environment

Ensure `RAPIDAPI_KEY` is set:
```powershell
$env:RAPIDAPI_KEY = "your_key_here"
# Or load from .env
```

## Status

- [x] Fetcher implementation (main.py)
- [x] Flask web server (app.py)
- [x] Beautiful responsive UI (templates/index.html)
- [x] REST API endpoints
- [x] Error handling & validation
- [x] Unit tests with mocking
- [ ] Integration tests (requires live API)
- [ ] Docker support (TODO)
- [ ] CI/CD pipeline (TODO)

## Troubleshooting

**Error: RAPIDAPI_KEY not set**
```powershell
$env:RAPIDAPI_KEY = "your_key_here"
```

**Port 5000 already in use**
```powershell
# Change port in app.py line:
# app.run(..., port=5001)
```

**Tests fail**
```powershell
# Make sure pytest and pytest-mock are installed
pip install -r requirements.txt --upgrade
```

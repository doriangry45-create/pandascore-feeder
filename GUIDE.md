# 🚀 Complete Step-by-Step Guide: From Zero to Production

**efootball-feeder — New Account Setup & Development Guide**

Yeni bir hesapla sıfırdan başlayan siz için tam rehber.

---

## 📋 İçindekiler

1. [GitHub Account Setup](#1-github-account-setup)
2. [Repository Fork & Clone](#2-repository-fork--clone)
3. [Local Development Environment](#3-local-development-environment)
4. [Running the Project Locally](#4-running-the-project-locally)
5. [Understanding the Codebase](#5-understanding-the-codebase)
6. [Making Your First Contribution](#6-making-your-first-contribution)
7. [Creating a Pull Request](#7-creating-a-pull-request)
8. [Code Review & Merge](#8-code-review--merge)
9. [Next Development Tasks](#9-next-development-tasks)
10. [Deployment (Production)](#10-deployment-production)

---

## 1. GitHub Account Setup

### 1.1 Create GitHub Account
- [ ] Go to https://github.com
- [ ] Click "Sign up"
- [ ] Enter email, password, username
- [ ] Verify email address
- [ ] Complete profile (optional but recommended)

### 1.2 Configure Git (Local Machine)
```powershell
# Set global git config (one time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify
git config --global --list
```

### 1.3 Generate SSH Key (Optional but Recommended)
```powershell
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# When prompted, press Enter to use default location
# Add password (optional but secure)

# Output: Your public key is saved in ~/.ssh/id_ed25519.pub
```

Add SSH key to GitHub:
- [ ] Go to https://github.com/settings/keys
- [ ] Click "New SSH key"
- [ ] Paste content of `~/.ssh/id_ed25519.pub`
- [ ] Save

---

## 2. Repository Fork & Clone

### 2.1 Fork the Repository
- [ ] Go to https://github.com/doriangry45-create/pandascore-feeder
- [ ] Click "Fork" button (top right)
- [ ] GitHub creates a copy under your account: `https://github.com/YOUR_USERNAME/pandascore-feeder`

### 2.2 Clone Your Fork
```powershell
# SSH (recommended if you set up SSH key)
git clone git@github.com:YOUR_USERNAME/pandascore-feeder.git
cd pandascore-feeder

# HTTPS (if no SSH key)
git clone https://github.com/YOUR_USERNAME/pandascore-feeder.git
cd pandascore-feeder
```

### 2.3 Add Upstream Remote (to sync with original)
```powershell
# Add link to original repo
git remote add upstream https://github.com/doriangry45-create/pandascore-feeder.git

# Verify remotes
git remote -v
# Output:
# origin    git@github.com:YOUR_USERNAME/pandascore-feeder.git (fetch)
# origin    git@github.com:YOUR_USERNAME/pandascore-feeder.git (push)
# upstream  https://github.com/doriangry45-create/pandascore-feeder.git (fetch)
# upstream  https://github.com/doriangry45-create/pandascore-feeder.git (push)
```

### 2.4 Checkout Feature Branch
```powershell
# Fetch latest from upstream
git fetch upstream

# Switch to feature branch
git checkout -b 001-rapidapi-efootball-fetch upstream/001-rapidapi-efootball-fetch

# Verify current branch
git branch -a
```

---

## 3. Local Development Environment

### 3.1 Install Python (if not already)
**Check if Python is installed:**
```powershell
python --version
# Expected output: Python 3.13.x or higher
```

**If not installed:**
- [ ] Download from https://www.python.org/downloads/
- [ ] Run installer
- [ ] ✅ **Check**: "Add Python to PATH" during installation
- [ ] Verify: `python --version`

### 3.2 Install Git (if not already)
```powershell
git --version
# Expected: git version 2.x.x
```

If not installed:
- [ ] Download from https://git-scm.com/download/win
- [ ] Run installer
- [ ] Use defaults

### 3.3 Create Virtual Environment
```powershell
# Navigate to project root
cd C:\path\to\pandascore-feeder

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate

# Verify activation (prompt should show (.venv))
```

### 3.4 Install Dependencies
```powershell
# Make sure you're in project root and .venv is activated

# Install Flask, requests, pytest, etc.
pip install -r services\feature-001\requirements.txt

# Verify
pip list
# Should show: flask, requests, pytest, pytest-mock
```

### 3.5 Set API Key (RAPIDAPI_KEY)
```powershell
# Copy .env if exists (contains API key)
copy env .env

# OR set environment variable directly
$env:RAPIDAPI_KEY = "2936622ae4msh4569de3e35fcbf4p1af2c7jsn5440174f71aa"

# Verify
$env:RAPIDAPI_KEY
```

⚠️ **IMPORTANT**: Never commit `.env` or API key to Git. `.gitignore` should exclude it.

---

## 4. Running the Project Locally

### 4.1 Run Flask Web UI (Most Common)
```powershell
# Make sure .venv is activated
.\.venv\Scripts\Activate

# Run Flask server
python services\feature-001\app.py

# Output:
# 🚀 Flask app running on http://localhost:5000
# 📊 Dashboard: http://localhost:5000
```

Open browser: **http://localhost:5000**

**What you'll see:**
- ⚽ E-Football Fixtures dashboard
- League selector (Premier League, La Liga, etc.)
- Season picker (2015-2025)
- "Fetch Fixtures" button
- Results table with live scores

### 4.2 Run CLI Fetcher
```powershell
# Fetch Premier League 2023 fixtures
python services\feature-001\main.py --league 39 --season 2023

# Custom output file
python services\feature-001\main.py --league 39 --season 2023 --output my_fixtures.json

# Output:
# ✓ Saved 400 fixtures to fixtures.json
```

### 4.3 Run Tests
```powershell
# Run all tests
pytest services\feature-001\tests\ -v

# Run specific test
pytest services\feature-001\tests\test_main.py::TestEFootballFetcher::test_init_with_env -v

# Run with coverage
pytest services\feature-001\tests\ -v --cov=services/feature-001

# Expected output: ===== 6 passed in 0.68s =====
```

---

## 5. Understanding the Codebase

### 5.1 Project Structure
```
pandascore-feeder/
├── .github/
│   ├── copilot-instructions.md     ← AI agents guide
│   └── workflows/                  ← CI/CD (TODO)
├── services/feature-001/
│   ├── main.py                     ← CLI fetcher (READ THIS FIRST)
│   ├── app.py                      ← Flask web server
│   ├── requirements.txt            ← Dependencies
│   ├── README.md                   ← Technical docs
│   ├── templates/
│   │   └── index.html              ← Web dashboard
│   └── tests/
│       └── test_main.py            ← Unit tests
├── spec.yaml                       ← RapidAPI config (IMPORTANT!)
├── env                             ← API credentials
├── ONBOARDING.md                   ← Quick start
├── TODO.md                         ← 30-item roadmap
├── HANDOFF.md                      ← Project status
└── GUIDE.md                        ← This file!
```

### 5.2 Key Files to Read

**Start with these (in order):**

1. **`ONBOARDING.md`** (10 min)
   - Quick start overview
   - Project structure
   - Key concepts

2. **`services/feature-001/README.md`** (10 min)
   - How to run Flask, CLI, tests
   - API details
   - Troubleshooting

3. **`spec.yaml`** (5 min)
   - RapidAPI endpoint configuration
   - Headers, base URL, query parameters
   - **This is the source of truth for API integration**

4. **`services/feature-001/main.py`** (15 min read)
   - EFootballFetcher class
   - How API calls work
   - Error handling patterns

5. **`services/feature-001/app.py`** (10 min)
   - Flask endpoints
   - How REST API works

6. **`TODO.md`** (skim 5 min)
   - Full roadmap
   - What's next

### 5.3 Understanding RapidAPI Integration

**spec.yaml defines:**
```yaml
base_url: https://api-football-v1.p.rapidapi.com/v3
endpoint: /fixtures
headers:
  X-RapidAPI-Key: ${RAPIDAPI_KEY}    # Read from environment
  X-RapidAPI-Host: api-football-v1.p.rapidapi.com
query:
  league: 39                          # Premier League
  season: 2023
```

**In Python (main.py):**
```python
# EFootballFetcher loads RAPIDAPI_KEY from env
fetcher = EFootballFetcher()

# Makes HTTP GET to:
# https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2023
# With headers: X-RapidAPI-Key, X-RapidAPI-Host
response = fetcher.fetch_fixtures(league=39, season=2023)

# Returns JSON with fixtures array
```

### 5.4 Code Flow Diagram

```
User Input (Web UI)
    ↓
Browser POST to /api/fixtures
    ↓
Flask (app.py) receives request
    ↓
Calls EFootballFetcher (main.py)
    ↓
HTTP GET to RapidAPI
    ↓
API returns JSON fixtures
    ↓
Flask returns JSON to browser
    ↓
JavaScript renders table
```

---

## 6. Making Your First Contribution

### 6.1 Create Feature Branch
```powershell
# Make sure you're on main branch
git checkout main

# Sync with upstream
git pull upstream main

# Create new branch for your work
git checkout -b 001-add-logging

# Verify you're on new branch
git branch -a
# * 001-add-logging
#   main
#   upstream/001-rapidapi-efootball-fetch
```

### 6.2 Make Code Changes

**Example: Add logging to main.py**

Open `services/feature-001/main.py` and add:
```python
import logging

# Add after imports
logger = logging.getLogger(__name__)

# In __init__ method
logger.info(f"EFootballFetcher initialized with league={league}")

# In fetch_fixtures method
logger.debug(f"Fetching fixtures for league={league}, season={season}")
```

### 6.3 Test Your Changes
```powershell
# Run tests to make sure nothing broke
pytest services\feature-001\tests\ -v

# Manual test (optional)
python services\feature-001\main.py --league 39 --season 2023
```

### 6.4 Commit Your Changes
```powershell
# Check what changed
git status

# Stage all changes
git add -A

# Or stage specific files
git add services\feature-001\main.py

# Commit with meaningful message
git commit -m "feat(001): Add logging to EFootballFetcher

- Add logger initialization
- Log fixture fetch operations
- Track API response times"

# Verify commit
git log --oneline -3
```

**Commit Message Format:**
```
type(scope): subject

body (optional)

footers (optional)
```

**Types:**
- `feat` — New feature
- `fix` — Bug fix
- `docs` — Documentation
- `refactor` — Code reorganization
- `test` — Test additions
- `perf` — Performance improvement

### 6.5 Push to Your Fork
```powershell
# Push to your fork (origin)
git push -u origin 001-add-logging

# Output should show:
# * [new branch]      001-add-logging -> 001-add-logging
# Branch 'xxx' set up to track remote branch 'xxx'
```

---

## 7. Creating a Pull Request

### 7.1 Open Pull Request on GitHub

- [ ] Go to https://github.com/YOUR_USERNAME/pandascore-feeder
- [ ] You should see a banner: "Compare & pull request"
- [ ] Click it
- [ ] Or manually:
  - [ ] Click "Pull requests" tab
  - [ ] Click "New pull request"
  - [ ] Set: `base: doriangry45-create/pandascore-feeder:main`
  - [ ] Set: `compare: YOUR_USERNAME/pandascore-feeder:001-add-logging`

### 7.2 Fill PR Details

**Title (clear and descriptive):**
```
feat(001): Add logging to EFootballFetcher

or

fix(001): Handle null goals in fixture response
```

**Description (explain what and why):**
```markdown
## Description
Adds comprehensive logging to EFootballFetcher class to track API operations and improve debugging.

## What Changed
- Added logger initialization in main.py
- Log fixture fetch operations with league/season
- Track API response times
- Log errors with full context

## Testing
- All 6 unit tests pass ✓
- Manual test with CLI: `python main.py --league 39`
- No breaking changes

## Related Issues
Closes #123 (if fixing an issue)

## Checklist
- [x] Code follows project style
- [x] Tests pass locally
- [x] No secrets in commits
- [x] README updated (if needed)
```

### 7.3 Request Review

- [ ] Click "Reviewers" (right sidebar)
- [ ] Add team members or maintainers
- [ ] Add labels (enhancement, bug, etc.)
- [ ] Link related issues

### 7.4 Respond to Feedback

During review, maintainer may ask for changes:

```powershell
# Make requested changes
# Edit files...

# Commit changes (new commit, don't amend)
git add -A
git commit -m "review(001): Address logging performance concerns

- Use lazy logging %s instead of f-strings
- Only log in debug mode by default"

# Push again (same branch)
git push origin 001-add-logging
```

PR automatically updates with new commits.

---

## 8. Code Review & Merge

### 8.1 Review Checklist (for reviewers)

**Code Quality:**
- [ ] Code follows Python conventions (PEP 8)
- [ ] No unused imports
- [ ] Clear variable names
- [ ] Proper error handling

**Testing:**
- [ ] New tests added
- [ ] All tests pass
- [ ] Test coverage doesn't decrease

**Security:**
- [ ] No secrets in code
- [ ] Input validation
- [ ] No SQL injection (if DB)
- [ ] RAPIDAPI_KEY not exposed

**Documentation:**
- [ ] Comments for complex code
- [ ] README updated if needed
- [ ] Docstrings on functions
- [ ] CHANGELOG updated

### 8.2 Approval & Merge

Once approved:
- [ ] Review comments addressed
- [ ] At least 1 approval
- [ ] All CI checks pass (if enabled)

Maintainer clicks "Merge pull request":
- Merge strategy: "Squash and merge" or "Create a merge commit"
- Branch deleted after merge

### 8.3 Verify Merge

```powershell
# Switch to main
git checkout main

# Pull latest from upstream
git pull upstream main

# Verify your changes are there
git log --oneline -5
```

---

## 9. Next Development Tasks

### 9.1 Pick Next Task from TODO

Open `TODO.md` and pick from:

**High Priority (do next):**
- [14] Docker containerization
- [15] GitHub Actions CI/CD
- [19] Security hardening
- [24] Production deployment

**Medium Priority:**
- [16] Swagger API docs
- [18] Error logging
- [25] Documentation

**Lower Priority:**
- [17] Caching
- [20] Integration tests
- [21] Database (optional)

### 9.2 Development Workflow

For each task:
```powershell
# 1. Create branch
git checkout -b 002-add-docker

# 2. Make changes
# Create Dockerfile, docker-compose.yml, .dockerignore

# 3. Test locally
# docker build -t efootball-feeder:latest .
# docker run -p 5000:5000 -e RAPIDAPI_KEY=... efootball-feeder:latest

# 4. Commit
git add -A
git commit -m "feat(001): Add Docker containerization

- Create Dockerfile with Python 3.13 base
- Copy requirements and install
- Expose port 5000
- Include .dockerignore"

# 5. Push
git push -u origin 002-add-docker

# 6. Create PR
# Go to GitHub and create PR

# 7. Wait for review & merge
```

### 9.3 Important Development Patterns

**Always:**
- [ ] Create feature branch (never work on main)
- [ ] Write tests before/with code
- [ ] Run tests locally before pushing
- [ ] Write clear commit messages
- [ ] Keep commits focused (one feature per commit)

**Never:**
- [ ] Commit secrets (API keys, passwords)
- [ ] Force push (git push -f)
- [ ] Work directly on main branch
- [ ] Merge without review
- [ ] Break existing tests

---

## 10. Deployment (Production)

### 10.1 Deployment Flow

```
Code on main branch
    ↓
CI/CD Pipeline runs (GitHub Actions)
    ↓
Build Docker image
    ↓
Push to Docker registry (Docker Hub, ECR, etc.)
    ↓
Deploy to cloud (Heroku, AWS, GCP, etc.)
    ↓
Set environment variables (RAPIDAPI_KEY)
    ↓
Start Flask server
    ↓
Open http://your-app.com
```

### 10.2 Deployment Steps (Heroku Example)

**Prerequisites:**
- [ ] Heroku account (https://www.heroku.com)
- [ ] Heroku CLI installed: https://devcenter.heroku.com/articles/heroku-cli

**Deploy:**
```powershell
# 1. Login to Heroku
heroku login

# 2. Create Heroku app
heroku create efootball-feeder

# 3. Set environment variable
heroku config:set RAPIDAPI_KEY=your_key_here

# 4. Deploy (push main branch to Heroku)
git push heroku main

# 5. Open app
heroku open

# 6. View logs
heroku logs --tail
```

**Verify deployment:**
- Open https://efootball-feeder.herokuapp.com
- Test fixtures endpoint: POST /api/fixtures
- Check logs: `heroku logs --tail`

### 10.3 Deployment Alternatives

**AWS Lambda + API Gateway:**
- Serverless option
- Pay per request
- More complex setup

**Google Cloud Run:**
- Container-based
- Auto-scaling
- Similar to Heroku

**DigitalOcean App Platform:**
- GitHub integration
- Affordable
- Easy CLI

**Docker + Your Own Server:**
- Full control
- More maintenance
- Self-hosted

### 10.4 Production Best Practices

**Before deploying:**
- [ ] All tests pass locally
- [ ] Code reviewed and merged to main
- [ ] No secrets in code
- [ ] Set FLASK_ENV=production
- [ ] Enable HTTPS/SSL
- [ ] Set up monitoring

**After deploying:**
- [ ] Test in production
- [ ] Monitor error logs
- [ ] Check response times
- [ ] Verify API key quotas
- [ ] Set up backups (if using DB)

---

## 🎯 Quick Reference

### Common Commands

```powershell
# Setup (one time)
git clone https://github.com/YOUR_USERNAME/pandascore-feeder.git
cd pandascore-feeder
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r services\feature-001\requirements.txt
$env:RAPIDAPI_KEY = "..."

# Daily workflow
.\.venv\Scripts\Activate              # Activate venv
python services\feature-001\app.py    # Run Flask
pytest services\feature-001\tests\ -v # Run tests

# Git workflow
git checkout -b feature-name
# Make changes...
git add -A
git commit -m "message"
git push -u origin feature-name
# Create PR on GitHub

# Deployment
git push heroku main
heroku logs --tail
heroku open
```

### Important Links

| Resource | URL |
|----------|-----|
| **Original Repo** | https://github.com/doriangry45-create/pandascore-feeder |
| **Your Fork** | https://github.com/YOUR_USERNAME/pandascore-feeder |
| **Issues** | https://github.com/doriangry45-create/pandascore-feeder/issues |
| **Discussions** | https://github.com/doriangry45-create/pandascore-feeder/discussions |
| **RapidAPI Docs** | https://rapidapi.com/api-sports/api/api-football |
| **Flask Docs** | https://flask.palletsprojects.com |
| **Git Docs** | https://git-scm.com/doc |
| **Heroku Docs** | https://devcenter.heroku.com |

---

## 📞 Troubleshooting

| Problem | Solution |
|---------|----------|
| **RAPIDAPI_KEY not set** | `$env:RAPIDAPI_KEY = "..."` or copy `.env` |
| **Port 5000 in use** | Change port in `app.py`: `app.run(port=5001)` |
| **Tests fail** | `pip install --upgrade pytest pytest-mock` |
| **.venv not found** | Create: `python -m venv .venv` |
| **Git push fails** | Verify SSH key or use HTTPS: `git remote set-url origin https://...` |
| **PR won't merge** | Check CI/CD status, address review comments |
| **Forgot commit message** | Use: `git commit --amend --no-edit` (don't push -f!) |

---

## 🚀 Next Steps

1. **Read** `ONBOARDING.md` (10 min)
2. **Set up** local environment (Section 3, 10 min)
3. **Run** Flask or CLI (Section 4, 5 min)
4. **Read** code (Section 5, 30 min)
5. **Make** first contribution (Section 6, 30 min)
6. **Create** PR (Section 7, 10 min)
7. **Wait** for review and merge (depends)
8. **Pick** next task from `TODO.md`
9. **Repeat** steps 6-8

---

**Total first-time setup: ~1-2 hours**  
**Per contribution cycle: ~30 min - 2 hours (depends on task complexity)**

---

## 📝 Your Checklist

### Day 1
- [ ] Create GitHub account
- [ ] Configure git
- [ ] Fork repository
- [ ] Clone locally
- [ ] Create virtual environment
- [ ] Install dependencies
- [ ] Run Flask UI
- [ ] Read ONBOARDING.md

### Day 2
- [ ] Read main.py, app.py
- [ ] Run tests
- [ ] Understand codebase
- [ ] Pick first task from TODO.md

### Day 3+
- [ ] Make code changes
- [ ] Write tests
- [ ] Create PR
- [ ] Address review feedback
- [ ] Merge PR
- [ ] Deploy (if applicable)

---

**Good luck! 🎉 You're ready to start contributing.**

*Last Updated: 2025-11-11*

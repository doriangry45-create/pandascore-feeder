# 📋 ONBOARDING GUIDE — efootball-feeder Project

**Yeni bir asistan için tam rehber. Aşağıdaki adımları sırasıyla takip et.**

---

## 🎯 Proje Nedir?

**efootball-feeder** — RapidAPI'den e-futbol maç verisi çeken ve web arayüzü üzerinden gösteren veri beslemesi.

- **Özellik 001** (`001-rapidapi-efootball-fetch`): RapidAPI e-football API entegrasyonu
- **Dil**: Python 3.13
- **Framework**: Flask (web UI), Requests (API client)
- **Test**: pytest + pytest-mock
- **CI/CD**: GitHub Actions (hazır değil, TODO)

---

## 📁 Proje Yapısı

```
efootball-feeder/
├── .github/
│   ├── copilot-instructions.md          ← AI ajanlar için rehber (ÖNEMLİ!)
│   └── workflows/                       ← CI/CD (TODO)
├── spec.yaml                            ← RapidAPI config ve endpoint tanımı
├── env                                  ← API key (RAPIDAPI_KEY=...)
├── services/feature-001/
│   ├── main.py                          ← CLI fetcher (EFootballFetcher sınıfı)
│   ├── app.py                           ← Flask web server
│   ├── requirements.txt                 ← Bağımlılıklar
│   ├── README.md                        ← Kullanım talimatları
│   ├── templates/
│   │   └── index.html                   ← Dashboard UI
│   └── tests/
│       ├── __init__.py
│       └── test_main.py                 ← 6 unit test (tümü PASS)
├── plans/001-rapidapi-efootball-fetch/
│   └── plan-001.md                      ← Implementation plan (SPECPULSE_METADATA)
├── specs/001-rapidapi-efootball-fetch/
│   ├── spec-001.md                      ← Spec (SPECPULSE_METADATA)
│   └── spec-002.md                      ← Spec (SPECPULSE_METADATA)
├── .specpulse/                          ← SpecPulse tool data (proje metadata)
├── memory/
│   └── context.md                       ← Aktif feature ve workflow history
└── ONBOARDING.md                        ← Bu dosya
```

---

## 🚀 Hızlı Başlangıç (İlk 10 dakika)

### 1. Repo'yu Clone et
```powershell
git clone https://github.com/doriangry45-create/pandascore-feeder.git
cd pandascore-feeder
git checkout 001-rapidapi-efootball-fetch
```

### 2. Ortamı Kur
```powershell
# Virtual env oluştur
python -m venv .venv
.\.venv\Scripts\Activate

# Bağımlılıkları yükle
pip install -r services\feature-001\requirements.txt
```

### 3. API Key'i Ayarla
```powershell
# Windows PowerShell
$env:RAPIDAPI_KEY = (Get-Content env).Trim()

# Veya direkt
$env:RAPIDAPI_KEY = "2936622ae4msh4569de3e35fcbf4p1af2c7jsn5440174f71aa"
```

### 4. Flask Web UI'ı Çalıştır
```powershell
python services\feature-001\app.py
```

👉 **Browser'de aç**: http://localhost:5000

### 5. CLI Fetcher'ı Test Et
```powershell
# Premier League 2023 fixtures'ı kaydet
python services\feature-001\main.py --league 39 --season 2023 --output fixtures.json

# Cıkısı: ✓ Saved 400 fixtures to fixtures.json
```

### 6. Tests Çalıştır
```powershell
pytest services\feature-001\tests\ -v

# Beklenen çıktı: ===== 6 passed in 0.68s =====
```

---

## 📚 Önemli Dosyalar

| Dosya | Amaç | Düzenle? |
|-------|------|---------|
| `.github/copilot-instructions.md` | AI ajanlar için rehber | Proje bilgisi güncellenirse |
| `spec.yaml` | RapidAPI endpoint config | API değişirse |
| `env` | `RAPIDAPI_KEY` | Gizli, commit etme! |
| `services/feature-001/main.py` | CLI fetcher | Bug fix, feature |
| `services/feature-001/app.py` | Flask web | UI feature, endpoint |
| `services/feature-001/templates/index.html` | Dashboard | UI design, feature |
| `services/feature-001/tests/test_main.py` | Birim testler | Test case ekle |
| `services/feature-001/README.md` | Kullanım kılavuzu | Talimat güncelle |
| `plans/001-...` | Implementation plan (SPECPULSE) | Adımları güncelle |

---

## 🔑 Key Concepts

### RapidAPI Integration
```yaml
# spec.yaml
apis:
  - base_url: https://api-football-v1.p.rapidapi.com/v3
    endpoints:
      - path: /fixtures
        headers:
          X-RapidAPI-Key: ${RAPIDAPI_KEY}
          X-RapidAPI-Host: api-football-v1.p.rapidapi.com
        query:
          league: 39  # Premier League ID
          season: 2023
```

**EFootballFetcher** sınıfı (main.py):
- `__init__(api_key)` — API key'i env'den okur veya argument olarak alır
- `fetch_fixtures(league, season)` — RapidAPI'ye HTTP GET çağrısı
- `save_fixtures(output_file)` — JSON olarak disk'e yazar

### Flask REST API
```
POST /api/fixtures
  Body: { "league": 39, "season": 2023 }
  Response: { "status": "success", "count": 400, "fixtures": [...] }

GET /api/leagues
  Response: [{ "id": 39, "name": "Premier League" }, ...]

GET /api/health
  Response: { "status": "healthy", "api_key_set": true }
```

### SpecPulse Metadata
Her plan/spec dosyasının başında:
```markdown
<!-- SPECPULSE_METADATA
FEATURE_DIR: 001-rapidapi-efootball-fetch
FEATURE_ID: 001
PLAN_ID: 001
STATUS: draft/in-progress/completed
-->
```

**UPDATE**: Dosya düzenlerken bu bloğu güncelle.

---

## 📊 Mevcut Status

✅ **Tamamlanan** (Commit'ler ee6f496 + 8c7363e):
- [x] Python CLI fetcher (main.py)
- [x] 6 unit test (100% PASS)
- [x] Flask web server (app.py)
- [x] Responsive dashboard (templates/index.html)
- [x] requirements.txt + README.md
- [x] Git branch `001-rapidapi-efootball-fetch` push'landı

❌ **TODO** (Next steps — aşağıdaki todo list'ten devam et):
- [ ] GitHub Pull Request aç ve merge et
- [ ] Docker containerization
- [ ] GitHub Actions CI/CD
- [ ] Production deployment
- [ ] Monitoring & logging
- [ ] Database storage (optional)
- [ ] API documentation (Swagger)

---

## 🛠️ Development Workflow

### Bug Fix veya Feature Ekle
1. **Branch oluştur**:
   ```powershell
   git checkout -b 001-bugfix/fixture-parsing
   ```

2. **Kod düzenle** (main.py, app.py, test_main.py, etc.)

3. **Testler çalıştır**:
   ```powershell
   pytest services\feature-001\tests\ -v
   ```

4. **Commit et**:
   ```powershell
   git add -A
   git commit -m "fix(001): Handle null goals in fixture parsing"
   ```

5. **Push et**:
   ```powershell
   git push origin 001-bugfix/fixture-parsing
   ```

6. **PR aç** GitHub'da ve merge'e kadar bekle

### SPECPULSE_METADATA Güncelleme
Eğer plan/spec düzenlediysen, dosyanın başındaki bloğu güncelle:
```markdown
<!-- SPECPULSE_METADATA
FEATURE_DIR: 001-rapidapi-efootball-fetch
FEATURE_ID: 001
PLAN_ID: 001
CREATED: 2025-11-10T21:11:18.192692
STATUS: in-progress  ← Burası güncelle!
-->
```

---

## 🐛 Troubleshooting

| Problem | Çözüm |
|---------|-------|
| **RAPIDAPI_KEY not set** | `$env:RAPIDAPI_KEY = "..."` set et |
| **Port 5000 already in use** | app.py'da port'u değiştir: `app.run(port=5001)` |
| **Tests fail** | `pip install --upgrade pytest pytest-mock` |
| **Import error** | Virtual env aktif mı? `.\.venv\Scripts\Activate` |
| **Git push fails** | Branch track mı? `git push -u origin 001-...` |

---

## 📖 Komut Cheat Sheet

```powershell
# Virtual env
python -m venv .venv
.\.venv\Scripts\Activate
deactivate

# Dependencies
pip install -r services\feature-001\requirements.txt
pip install --upgrade flask requests

# Run
python services\feature-001\app.py          # Flask web (localhost:5000)
python services\feature-001\main.py         # CLI fetcher

# Test
pytest services\feature-001\tests\ -v       # Run all tests
pytest services\feature-001\tests\ -k "test_fetch"  # Run specific test
pytest --cov=services/feature-001 services/feature-001/tests/  # Coverage

# Git
git status
git add -A
git commit -m "message"
git push origin branch-name
git pull origin main

# Docker (future)
docker build -t efootball-feeder:latest .
docker run -p 5000:5000 -e RAPIDAPI_KEY=... efootball-feeder:latest
```

---

## 📞 Sonraki Adım?

1. **Mevcut todo list'i aç**:
   ```
   Services/feature-001/README.md
   .github/copilot-instructions.md
   ONBOARDING.md (bu dosya)
   ```

2. **Hangi adım istiyorsan seç** (todo list'ten — item 12 ve sonrası):
   - [12] Create Pull Request on GitHub
   - [13] Code Review & Merge
   - [14] Docker Deployment
   - [15] CI/CD Pipeline
   - ... vs

3. **Her adımda**:
   - README.md ve comments'i oku
   - Tests yaz ve çalıştır
   - Commit et + push et
   - SpecPulse metadata güncelle

4. **Sorular varsa**:
   - `.github/copilot-instructions.md` oku (proje patterns)
   - `services/feature-001/README.md` oku (teknik details)
   - Bu dosyayı oku (workflow)

---

**Başarılar! 🚀**

*Bu dosya projeyle güncel tutul. Son güncelleme: 2025-11-11*

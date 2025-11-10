#!/usr/bin/env python3
"""
Flask Web UI for E-Football Fixtures Fetcher
Simple dashboard to browse and fetch fixtures via RapidAPI.
"""
import os
import json
from flask import Flask, render_template, request, jsonify
from main import EFootballFetcher

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"])
def index():
    """Main dashboard page."""
    return render_template("index.html")


@app.route("/api/fixtures", methods=["POST"])
def api_fixtures():
    """Fetch fixtures API endpoint."""
    try:
        league = request.json.get("league", 39)
        season = request.json.get("season", 2023)
        
        fetcher = EFootballFetcher()
        data = fetcher.fetch_fixtures(league=league, season=season)
        
        fixtures = data.get("response", [])
        return jsonify({
            "status": "success",
            "count": len(fixtures),
            "fixtures": fixtures[:50]  # Limit to 50 for UI performance
        })
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": f"Fetch failed: {str(e)}"}), 500


@app.route("/api/leagues", methods=["GET"])
def api_leagues():
    """Return popular leagues."""
    leagues = [
        {"id": 39, "name": "Premier League (England)"},
        {"id": 140, "name": "La Liga (Spain)"},
        {"id": 135, "name": "Serie A (Italy)"},
        {"id": 78, "name": "Bundesliga (Germany)"},
        {"id": 61, "name": "Ligue 1 (France)"},
        {"id": 1, "name": "World Cup"},
    ]
    return jsonify(leagues)


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint."""
    try:
        api_key = os.environ.get("RAPIDAPI_KEY")
        return jsonify({
            "status": "healthy",
            "api_key_set": bool(api_key)
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.errorhandler(404)
def not_found(e):
    """404 handler."""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def server_error(e):
    """500 handler."""
    return jsonify({"error": "Server error"}), 500


if __name__ == "__main__":
    # Check API key before running
    if not os.environ.get("RAPIDAPI_KEY"):
        print("⚠️  Warning: RAPIDAPI_KEY not set. Set it before running:")
        print("   $env:RAPIDAPI_KEY = 'your_key_here'")
    
    print("🚀 Flask app running on http://localhost:5000")
    print("📊 Dashboard: http://localhost:5000")
    print("🔗 API docs:")
    print("   POST /api/fixtures - Fetch fixtures")
    print("   GET /api/leagues - List popular leagues")
    print("   GET /api/health - Health check")
    
    app.run(debug=True, host="0.0.0.0", port=5000)

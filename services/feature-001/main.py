#!/usr/bin/env python3
"""
E-Football Fixtures Fetcher
Fetches match fixtures from RapidAPI e-football endpoint.
"""
import os
import json
import requests
from typing import Optional, Dict, Any


class EFootballFetcher:
    """Fetch e-football fixtures from RapidAPI."""
    
    BASE_URL = "https://api-football-v1.p.rapidapi.com/v3"
    HOST = "api-football-v1.p.rapidapi.com"
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize fetcher with RapidAPI key from env or argument."""
        self.api_key = api_key or os.environ.get("RAPIDAPI_KEY")
        if not self.api_key:
            raise ValueError("RAPIDAPI_KEY not set in environment or argument")
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.HOST,
        }
    
    def fetch_fixtures(self, league: int = 39, season: int = 2023, **kwargs) -> Dict[str, Any]:
        """
        Fetch fixtures for a given league and season.
        
        Args:
            league: League ID (default 39 = Premier League)
            season: Season year (default 2023)
            **kwargs: Additional query params
        
        Returns:
            JSON response dict
        
        Raises:
            requests.RequestException on network error
        """
        params = {"league": league, "season": season}
        params.update(kwargs)
        
        url = f"{self.BASE_URL}/fixtures"
        response = requests.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    
    def save_fixtures(self, output_file: str, league: int = 39, season: int = 2023) -> int:
        """
        Fetch fixtures and save to JSON file.
        
        Returns:
            Number of fixtures fetched
        """
        data = self.fetch_fixtures(league=league, season=season)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        count = len(data.get("response", []))
        print(f"✓ Saved {count} fixtures to {output_file}")
        return count


def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fetch e-football fixtures from RapidAPI")
    parser.add_argument("--league", type=int, default=39, help="League ID (default: 39 = Premier League)")
    parser.add_argument("--season", type=int, default=2023, help="Season year (default: 2023)")
    parser.add_argument("--output", "-o", default="fixtures.json", help="Output JSON file")
    args = parser.parse_args()
    
    try:
        fetcher = EFootballFetcher()
        fetcher.save_fixtures(args.output, league=args.league, season=args.season)
        print(f"✓ Fixtures saved to {args.output}")
    except ValueError as e:
        print(f"✗ Error: {e}", flush=True)
        return 1
    except requests.RequestException as e:
        print(f"✗ Network error: {e}", flush=True)
        return 1
    except Exception as e:
        print(f"✗ Unexpected error: {e}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    exit(main())

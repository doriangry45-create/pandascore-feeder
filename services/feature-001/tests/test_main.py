"""Unit tests for EFootballFetcher."""
import pytest
from unittest.mock import Mock, patch, MagicMock
import json
import sys
from pathlib import Path

# Add parent dir to path so we can import main
sys.path.insert(0, str(Path(__file__).parent.parent))
from main import EFootballFetcher


class TestEFootballFetcher:
    """Test EFootballFetcher class."""
    
    def test_init_with_env(self, monkeypatch):
        """Test initialization reads RAPIDAPI_KEY from env."""
        monkeypatch.setenv("RAPIDAPI_KEY", "test_key_123")
        fetcher = EFootballFetcher()
        assert fetcher.api_key == "test_key_123"
        assert fetcher.headers["X-RapidAPI-Key"] == "test_key_123"
    
    def test_init_no_key_raises(self, monkeypatch):
        """Test initialization fails if RAPIDAPI_KEY not set."""
        monkeypatch.delenv("RAPIDAPI_KEY", raising=False)
        with pytest.raises(ValueError, match="RAPIDAPI_KEY not set"):
            EFootballFetcher()
    
    def test_init_explicit_key(self):
        """Test initialization with explicit key argument."""
        fetcher = EFootballFetcher(api_key="explicit_key_456")
        assert fetcher.api_key == "explicit_key_456"
    
    @patch("main.requests.get")
    def test_fetch_fixtures_success(self, mock_get, monkeypatch):
        """Test successful fixture fetch."""
        monkeypatch.setenv("RAPIDAPI_KEY", "test_key")
        
        mock_response = Mock()
        mock_response.json.return_value = {
            "response": [
                {"fixture": {"id": 1}, "teams": {"home": {"name": "Team A"}}},
                {"fixture": {"id": 2}, "teams": {"home": {"name": "Team B"}}},
            ]
        }
        mock_get.return_value = mock_response
        
        fetcher = EFootballFetcher()
        result = fetcher.fetch_fixtures(league=39, season=2023)
        
        assert "response" in result
        assert len(result["response"]) == 2
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert "params" in call_args.kwargs
        assert call_args.kwargs["params"]["league"] == 39
        assert call_args.kwargs["params"]["season"] == 2023
    
    @patch("main.requests.get")
    def test_fetch_fixtures_network_error(self, mock_get, monkeypatch):
        """Test fetch raises RequestException on network error."""
        import requests
        monkeypatch.setenv("RAPIDAPI_KEY", "test_key")
        
        mock_get.side_effect = requests.RequestException("Connection timeout")
        fetcher = EFootballFetcher()
        
        with pytest.raises(requests.RequestException):
            fetcher.fetch_fixtures()
    
    @patch("main.requests.get")
    @patch("builtins.open", create=True)
    def test_save_fixtures(self, mock_open, mock_get, monkeypatch):
        """Test saving fixtures to JSON file."""
        monkeypatch.setenv("RAPIDAPI_KEY", "test_key")
        
        mock_response = Mock()
        mock_data = {"response": [{"id": 1}, {"id": 2}]}
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        
        fetcher = EFootballFetcher()
        count = fetcher.save_fixtures("test.json", league=39, season=2023)
        
        assert count == 2
        mock_open.assert_called_once_with("test.json", "w", encoding="utf-8")
        # write() may be called multiple times (json.dump streams)
        assert mock_file.write.called
        all_written = "".join(str(call[0][0]) for call in mock_file.write.call_args_list)
        assert '"response"' in all_written


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

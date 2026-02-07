"""
Pytest configuration and shared fixtures for GenAI4Humanists tests.
"""
import os
import pytest
from unittest.mock import Mock, patch
from pathlib import Path


@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock environment variables for testing."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key-123")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key-456")
    monkeypatch.setenv("MULTION_API_KEY", "test-multion-key-789")
    return {
        "OPENAI_API_KEY": "test-openai-key-123",
        "GEMINI_API_KEY": "test-gemini-key-456",
        "MULTION_API_KEY": "test-multion-key-789",
    }


@pytest.fixture
def temp_env_file(tmp_path):
    """Create a temporary .env file for testing."""
    env_file = tmp_path / ".env"
    env_file.write_text(
        "OPENAI_API_KEY=test-key-123\n"
        "GEMINI_API_KEY=test-gemini-456\n"
        "MULTION_API_KEY=test-multion-789\n"
    )
    return env_file


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client for testing."""
    mock_client = Mock()
    mock_client.chat.completions.create = Mock()
    return mock_client


@pytest.fixture
def mock_multion_client():
    """Mock MultiOn client for testing."""
    mock_client = Mock()
    mock_client.sessions.create = Mock()
    mock_client.sessions.step = Mock()
    mock_client.sessions.close = Mock()
    return mock_client


@pytest.fixture
def sample_screenshot_url():
    """Sample screenshot URL for testing."""
    return "https://example.com/screenshot.png"


@pytest.fixture
def project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent

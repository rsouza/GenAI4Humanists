"""
Tests for src/helper.py module.
"""
import os
import pytest
from unittest.mock import Mock, patch, MagicMock
from src import helper


class TestEnvironmentLoading:
    """Test environment variable loading functions."""

    def test_load_env_function_exists(self):
        """Test that load_env function is callable."""
        assert callable(helper.load_env)

    @patch('src.helper.load_dotenv')
    @patch('src.helper.find_dotenv')
    def test_load_env_calls_load_dotenv(self, mock_find_dotenv, mock_load_dotenv):
        """Test that load_env calls load_dotenv with find_dotenv result."""
        mock_find_dotenv.return_value = ".env"
        helper.load_env()
        mock_find_dotenv.assert_called_once()
        mock_load_dotenv.assert_called_once_with(".env")


class TestAPIKeyRetrieval:
    """Test API key retrieval functions."""

    def test_get_openai_api_key_returns_string(self, mock_env_vars):
        """Test that get_openai_api_key returns the correct key."""
        with patch('src.helper.load_env'):
            key = helper.get_openai_api_key()
            assert key == "test-openai-key-123"
            assert isinstance(key, str)

    def test_get_openai_api_key_returns_none_when_not_set(self):
        """Test that get_openai_api_key returns None when key is not set."""
        with patch('src.helper.load_env'):
            with patch.dict(os.environ, {}, clear=True):
                key = helper.get_openai_api_key()
                assert key is None

    def test_get_multi_on_api_key_returns_string(self, mock_env_vars):
        """Test that get_multi_on_api_key returns the correct key."""
        with patch('src.helper.load_env'):
            key = helper.get_multi_on_api_key()
            assert key == "test-multion-key-789"
            assert isinstance(key, str)


class TestClientCreation:
    """Test client creation functions."""

    @patch('src.helper.OpenAI')
    @patch('src.helper.get_openai_api_key')
    def test_get_openai_client_creates_client(self, mock_get_key, mock_openai):
        """Test that get_openai_client creates an OpenAI client."""
        mock_get_key.return_value = "test-key"
        mock_client = Mock()
        mock_openai.return_value = mock_client

        client = helper.get_openai_client()

        mock_get_key.assert_called_once()
        mock_openai.assert_called_once_with(api_key="test-key")
        assert client == mock_client

    @patch('src.helper.MultiOn')
    @patch('src.helper.get_multi_on_api_key')
    def test_get_multi_on_client_creates_client(self, mock_get_key, mock_multion):
        """Test that get_multi_on_client creates a MultiOn client."""
        mock_get_key.return_value = "test-multion-key"
        mock_client = Mock()
        mock_multion.return_value = mock_client

        client = helper.get_multi_on_client()

        mock_get_key.assert_called_once()
        mock_multion.assert_called_once_with(api_key="test-multion-key")
        assert client == mock_client


class TestVisualizeCourses:
    """Test visualizeCourses function."""

    @pytest.mark.asyncio
    async def test_visualize_courses_with_empty_result(self):
        """Test visualizeCourses with empty result."""
        # This function requires async testing and display mocking
        # Placeholder for future implementation
        assert callable(helper.visualizeCourses)

    def test_visualize_courses_callable(self):
        """Test that visualizeCourses is callable."""
        assert callable(helper.visualizeCourses)

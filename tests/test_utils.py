"""
Tests for src/utils.py module.
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from PIL import Image
from io import BytesIO
from src import utils


class TestEnvironmentUtils:
    """Test environment utility functions."""

    def test_load_env_function_exists(self):
        """Test that load_env function is callable."""
        assert callable(utils.load_env)

    def test_get_multi_on_api_key_returns_string(self, mock_env_vars):
        """Test that get_multi_on_api_key returns the correct key."""
        with patch('src.utils.load_env'):
            key = utils.get_multi_on_api_key()
            assert key == "test-multion-key-789"

    @patch('src.utils.MultiOn')
    @patch('src.utils.get_multi_on_api_key')
    def test_get_multi_on_client_creates_client(self, mock_get_key, mock_multion):
        """Test that get_multi_on_client creates a MultiOn client."""
        mock_get_key.return_value = "test-key"
        mock_client = Mock()
        mock_multion.return_value = mock_client

        client = utils.get_multi_on_client()

        mock_get_key.assert_called_once()
        mock_multion.assert_called_once_with(api_key="test-key")


class TestImageUtils:
    """Test ImageUtils class methods."""

    def test_get_screenshot_returns_none_for_invalid_url(self):
        """Test that get_screenshot returns None for invalid URLs."""
        result = utils.ImageUtils.get_screenshot(None)
        assert result is None

        result = utils.ImageUtils.get_screenshot("")
        assert result is None

        result = utils.ImageUtils.get_screenshot("not-a-url")
        assert result is None

    @patch('src.utils.requests.get')
    def test_get_screenshot_returns_none_for_404(self, mock_get):
        """Test that get_screenshot returns None for non-200 status codes."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = utils.ImageUtils.get_screenshot("https://example.com/test.png")
        assert result is None

    @patch('src.utils.requests.get')
    def test_get_screenshot_returns_image_for_valid_url(self, mock_get):
        """Test that get_screenshot returns PIL Image for valid response."""
        # Create a simple 1x1 red pixel PNG
        img = Image.new('RGB', (1, 1), color='red')
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = img_bytes.getvalue()
        mock_get.return_value = mock_response

        result = utils.ImageUtils.get_screenshot("https://example.com/test.png")
        assert isinstance(result, Image.Image)

    @patch('src.utils.requests.get')
    def test_get_screenshot_handles_request_exception(self, mock_get):
        """Test that get_screenshot handles network errors gracefully."""
        import requests
        mock_get.side_effect = requests.RequestException("Network error")

        result = utils.ImageUtils.get_screenshot("https://example.com/test.png")
        assert result is None


class TestVisualizeSession:
    """Test visualizeSession function."""

    def test_visualize_session_callable(self):
        """Test that visualizeSession is callable."""
        assert callable(utils.visualizeSession)

    def test_visualize_session_with_mock_response(self):
        """Test visualizeSession with a mock response object."""
        mock_response = Mock()
        mock_response.status = "DONE"
        mock_response.message = "Task completed"
        mock_response.url = "https://example.com"
        mock_response.screenshot = None

        # This would normally display HTML in Jupyter, but we're just testing it doesn't crash
        with patch('src.utils.display'):
            utils.visualizeSession(mock_response, show_screenshot=False)


class TestDisplayStepHeader:
    """Test display_step_header function."""

    def test_display_step_header_callable(self):
        """Test that display_step_header is callable."""
        assert callable(utils.display_step_header)

    def test_display_step_header_with_integer(self):
        """Test display_step_header with an integer step number."""
        with patch('src.utils.display'):
            utils.display_step_header(1)
            utils.display_step_header(99)


class TestSessionManager:
    """Test SessionManager class."""

    @patch('src.utils.MultiOn')
    def test_session_manager_initialization(self, mock_multion_class):
        """Test SessionManager initialization."""
        mock_client = Mock()
        mock_multion_class.return_value = mock_client

        manager = utils.SessionManager(
            base_url="https://example.com",
            multion_client=mock_client
        )

        assert manager.base_url == "https://example.com"
        assert manager.current_url == "https://example.com"
        assert manager.session_id is None

    @patch('src.utils.MultiOn')
    def test_session_manager_create_session(self, mock_multion_class):
        """Test SessionManager session creation."""
        mock_client = Mock()
        mock_session = Mock()
        mock_session.session_id = "test-session-123"
        mock_session.url = "https://example.com"
        mock_session.screenshot = "screenshot-data"

        mock_client.sessions.create.return_value = mock_session
        mock_multion_instance = Mock()
        mock_multion_instance.client = mock_client

        manager = utils.SessionManager(
            base_url="https://example.com",
            multion_client=mock_multion_instance
        )

        session = manager.create_session()

        assert session.session_id == "test-session-123"
        assert manager.session_id == "test-session-123"


class TestMultiOnDemo:
    """Test MultiOnDemo class."""

    @patch('src.utils.SessionManager')
    def test_multionddemo_initialization(self, mock_session_manager_class):
        """Test MultiOnDemo initialization."""
        mock_session_manager = Mock()
        mock_session_manager.session_id = "test-session"
        mock_session_manager_class.return_value = mock_session_manager

        demo = utils.MultiOnDemo(
            base_url="https://example.com",
            sessionManager=mock_session_manager,
            multion_client=Mock(),
            instructions=["Test instruction"],
            action_engine=None
        )

        assert demo.base_url == "https://example.com"
        assert demo.instructions == ["Test instruction"]

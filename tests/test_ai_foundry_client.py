"""
Tests for the AI Foundry Client module.

These tests validate the functionality of the AIFoundryClient class
including initialization, connection management, and error handling.
"""

import sys
import os
from unittest.mock import Mock, patch
import pytest

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from ai_foundry_client import AIFoundryClient  # noqa: E402


class TestAIFoundryClientInitialization:
    """Test cases for AIFoundryClient initialization."""

    def test_init_with_defaults(self):
        """Test initialization with default parameters."""
        client = AIFoundryClient()
        assert client.endpoint == AIFoundryClient.DEFAULT_ENDPOINT
        assert client.agent_id == AIFoundryClient.DEFAULT_AGENT_ID
        assert client.credential is not None
        assert not client.is_connected

    def test_init_with_custom_endpoint(self):
        """Test initialization with custom endpoint."""
        custom_endpoint = "https://custom.endpoint.com/api/projects/test"
        client = AIFoundryClient(endpoint=custom_endpoint)
        assert client.endpoint == custom_endpoint
        assert client.agent_id == AIFoundryClient.DEFAULT_AGENT_ID

    def test_init_with_custom_agent_id(self):
        """Test initialization with custom agent ID."""
        custom_agent_id = "asst_custom_id_12345"
        client = AIFoundryClient(agent_id=custom_agent_id)
        assert client.endpoint == AIFoundryClient.DEFAULT_ENDPOINT
        assert client.agent_id == custom_agent_id

    def test_init_with_custom_credential(self):
        """Test initialization with custom credential."""
        mock_credential = Mock()
        client = AIFoundryClient(credential=mock_credential)
        assert client.credential is mock_credential

    def test_init_with_all_custom_params(self):
        """Test initialization with all custom parameters."""
        custom_endpoint = "https://custom.endpoint.com/api/projects/test"
        custom_agent_id = "asst_custom_id_12345"
        mock_credential = Mock()
        client = AIFoundryClient(
            endpoint=custom_endpoint,
            agent_id=custom_agent_id,
            credential=mock_credential,
        )
        assert client.endpoint == custom_endpoint
        assert client.agent_id == custom_agent_id
        assert client.credential is mock_credential

    def test_init_with_empty_endpoint_raises_error(self):
        """Test initialization with empty endpoint raises ValueError."""
        with pytest.raises(ValueError, match="endpoint must be a non-empty string"):
            AIFoundryClient(endpoint="")

    def test_init_with_none_explicit_endpoint_uses_default(self):
        """Test initialization with None endpoint uses default."""
        client = AIFoundryClient(endpoint=None)
        assert client.endpoint == AIFoundryClient.DEFAULT_ENDPOINT

    def test_init_with_empty_agent_id_raises_error(self):
        """Test initialization with empty agent_id raises ValueError."""
        with pytest.raises(ValueError, match="agent_id must be a non-empty string"):
            AIFoundryClient(agent_id="")

    def test_init_with_invalid_endpoint_type_raises_error(self):
        """Test initialization with invalid endpoint type raises ValueError."""
        with pytest.raises(ValueError, match="endpoint must be a non-empty string"):
            AIFoundryClient(endpoint=123)

    def test_init_with_invalid_agent_id_type_raises_error(self):
        """Test initialization with invalid agent_id type raises ValueError."""
        with pytest.raises(ValueError, match="agent_id must be a non-empty string"):
            AIFoundryClient(agent_id=123)


class TestAIFoundryClientConnection:
    """Test cases for AIFoundryClient connection management."""

    @patch("ai_foundry_client.AIProjectClient")
    def test_connect_success(self, mock_ai_project_client):
        """Test successful connection to Azure AI Foundry."""
        mock_client_instance = Mock()
        mock_ai_project_client.return_value = mock_client_instance

        client = AIFoundryClient()
        client.connect()

        assert client.is_connected
        mock_ai_project_client.assert_called_once_with(
            credential=client.credential, endpoint=client.endpoint
        )

    @patch("ai_foundry_client.AIProjectClient")
    def test_connect_failure_raises_connection_error(self, mock_ai_project_client):
        """Test connection failure raises ConnectionError."""
        mock_ai_project_client.side_effect = Exception("Connection failed")

        client = AIFoundryClient()
        with pytest.raises(ConnectionError, match="Failed to connect to Azure AI"):
            client.connect()

        assert not client.is_connected

    @patch("ai_foundry_client.AIProjectClient")
    def test_disconnect(self, mock_ai_project_client):
        """Test disconnection from Azure AI Foundry."""
        mock_client_instance = Mock()
        mock_ai_project_client.return_value = mock_client_instance

        client = AIFoundryClient()
        client.connect()
        assert client.is_connected

        client.disconnect()
        assert not client.is_connected

    def test_disconnect_when_not_connected(self):
        """Test disconnect when not connected does not raise error."""
        client = AIFoundryClient()
        assert not client.is_connected
        client.disconnect()  # Should not raise error
        assert not client.is_connected

    @patch("ai_foundry_client.AIProjectClient")
    def test_is_connected_property(self, mock_ai_project_client):
        """Test is_connected property reflects connection state."""
        mock_client_instance = Mock()
        mock_ai_project_client.return_value = mock_client_instance

        client = AIFoundryClient()
        assert not client.is_connected

        client.connect()
        assert client.is_connected

        client.disconnect()
        assert not client.is_connected


class TestAIFoundryClientProperties:
    """Test cases for AIFoundryClient properties and getters."""

    def test_get_agent_id(self):
        """Test get_agent_id returns configured agent ID."""
        custom_agent_id = "asst_test_id"
        client = AIFoundryClient(agent_id=custom_agent_id)
        assert client.get_agent_id() == custom_agent_id

    def test_get_endpoint(self):
        """Test get_endpoint returns configured endpoint."""
        custom_endpoint = "https://test.endpoint.com/api/projects/test"
        client = AIFoundryClient(endpoint=custom_endpoint)
        assert client.get_endpoint() == custom_endpoint

    @patch("ai_foundry_client.AIProjectClient")
    def test_client_property_when_connected(self, mock_ai_project_client):
        """Test client property returns AIProjectClient when connected."""
        mock_client_instance = Mock()
        mock_ai_project_client.return_value = mock_client_instance

        client = AIFoundryClient()
        client.connect()

        assert client.client is mock_client_instance

    def test_client_property_when_not_connected_raises_error(self):
        """Test client property raises RuntimeError when not connected."""
        client = AIFoundryClient()
        with pytest.raises(RuntimeError, match="Not connected to Azure AI Foundry"):
            _ = client.client


class TestAIFoundryClientEdgeCases:
    """Test cases for edge cases and special scenarios."""

    def test_multiple_connect_calls(self):
        """Test multiple connect calls work correctly."""
        with patch("ai_foundry_client.AIProjectClient") as mock_ai_project_client:
            mock_client_instance = Mock()
            mock_ai_project_client.return_value = mock_client_instance

            client = AIFoundryClient()
            client.connect()
            first_client = client._client

            client.connect()
            second_client = client._client

            # Both should be valid instances
            assert first_client is not None
            assert second_client is not None

    def test_special_characters_in_endpoint(self):
        """Test endpoint with special characters."""
        endpoint = "https://test.com/api/projects/test@123"
        client = AIFoundryClient(endpoint=endpoint)
        assert client.endpoint == endpoint

    def test_special_characters_in_agent_id(self):
        """Test agent_id with special characters."""
        agent_id = "asst_test_id_123@#$"
        client = AIFoundryClient(agent_id=agent_id)
        assert client.agent_id == agent_id

    def test_whitespace_only_endpoint_raises_error(self):
        """Test endpoint with only whitespace raises ValueError."""
        with pytest.raises(ValueError, match="endpoint must be a non-empty string"):
            AIFoundryClient(endpoint="   ")

    def test_whitespace_only_agent_id_raises_error(self):
        """Test agent_id with only whitespace raises ValueError."""
        with pytest.raises(ValueError, match="agent_id must be a non-empty string"):
            AIFoundryClient(agent_id="   ")

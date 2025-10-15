"""
AI Foundry Client module for integrating with Azure AI Foundry services.

This module provides a client class to interact with Azure AI Foundry
for agent functionality.
"""

from typing import Optional
from azure.ai.projects import AIProjectClient
from azure.core.credentials import TokenCredential
from azure.identity import DefaultAzureCredential


class AIFoundryClient:
    """
    Client for interacting with Azure AI Foundry agent services.

    This class provides methods to connect to Azure AI Foundry and
    interact with configured agents.

    Attributes:
        endpoint (str): The Azure AI Foundry project endpoint URL
        agent_id (str): The unique identifier for the agent
        credential (TokenCredential): Azure credential for authentication
    """

    # Default configuration constants
    DEFAULT_ENDPOINT = (
        "https://magro-agent-resource.services.ai.azure.com/api/projects/magro-agent"
    )
    DEFAULT_AGENT_ID = "asst_5mhh5YN0lkowT6S2Kcw45X8V"

    def __init__(
        self,
        endpoint: Optional[str] = None,
        agent_id: Optional[str] = None,
        credential: Optional[TokenCredential] = None,
    ) -> None:
        """
        Initialize the AI Foundry Client.

        Args:
            endpoint (Optional[str]): The Azure AI Foundry project endpoint URL.
                Defaults to the configured endpoint.
            agent_id (Optional[str]): The unique identifier for the agent.
                Defaults to the configured agent ID.
            credential (Optional[TokenCredential]): Azure credential for
                authentication. If not provided, uses DefaultAzureCredential.

        Raises:
            ValueError: If endpoint or agent_id is empty or invalid
        """
        # Set values, using defaults if None is provided
        if endpoint is None:
            self.endpoint = self.DEFAULT_ENDPOINT
        else:
            self.endpoint = endpoint

        if agent_id is None:
            self.agent_id = self.DEFAULT_AGENT_ID
        else:
            self.agent_id = agent_id

        self.credential = credential or DefaultAzureCredential()

        # Validate inputs
        if not isinstance(self.endpoint, str) or not self.endpoint.strip():
            raise ValueError("endpoint must be a non-empty string")
        if not isinstance(self.agent_id, str) or not self.agent_id.strip():
            raise ValueError("agent_id must be a non-empty string")

        self._client: Optional[AIProjectClient] = None

    def connect(self) -> None:
        """
        Establish connection to Azure AI Foundry service.

        Creates an AIProjectClient instance with the configured
        endpoint and credentials.

        Raises:
            ConnectionError: If connection to Azure AI Foundry fails
            ValueError: If credentials are invalid
        """
        try:
            self._client = AIProjectClient(
                credential=self.credential, endpoint=self.endpoint
            )
        except Exception as e:
            raise ConnectionError(
                f"Failed to connect to Azure AI Foundry: {str(e)}"
            ) from e

    def disconnect(self) -> None:
        """
        Close the connection to Azure AI Foundry service.

        Cleans up the client connection and resources.
        """
        if self._client is not None:
            self._client = None

    @property
    def is_connected(self) -> bool:
        """
        Check if the client is connected to Azure AI Foundry.

        Returns:
            bool: True if connected, False otherwise
        """
        return self._client is not None

    @property
    def client(self) -> AIProjectClient:
        """
        Get the underlying AIProjectClient instance.

        Returns:
            AIProjectClient: The Azure AI Project client instance

        Raises:
            RuntimeError: If not connected to Azure AI Foundry
        """
        if not self.is_connected:
            raise RuntimeError(
                "Not connected to Azure AI Foundry. Call connect() first."
            )
        return self._client

    def get_agent_id(self) -> str:
        """
        Get the configured agent ID.

        Returns:
            str: The agent identifier
        """
        return self.agent_id

    def get_endpoint(self) -> str:
        """
        Get the configured endpoint URL.

        Returns:
            str: The Azure AI Foundry endpoint URL
        """
        return self.endpoint

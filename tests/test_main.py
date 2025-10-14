"""
Tests for the main module.

These tests demonstrate how to write tests that GitHub Copilot
can help you generate and maintain.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import greet


def test_greet():
    """Test the greet function returns expected message."""
    result = greet("Alice")
    assert "Alice" in result
    assert "Hello" in result
    assert "agentic-ghc-demo-00" in result


def test_greet_empty_string():
    """Test greet function with empty string."""
    result = greet("")
    assert result == "Hello, ! Welcome to agentic-ghc-demo-00."


def test_greet_special_characters():
    """Test greet function with special characters."""
    result = greet("Test@123")
    assert "Test@123" in result

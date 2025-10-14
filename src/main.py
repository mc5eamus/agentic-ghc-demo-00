"""
Main application module for agentic-ghc-demo-00.

This module demonstrates a simple Python application structure
that works well with GitHub Copilot.
"""


def greet(name: str) -> str:
    """
    Generate a greeting message for the given name.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A formatted greeting message
    """
    return f"Hello, {name}! Welcome to agentic-ghc-demo-00."


def main() -> None:
    """
    Main entry point for the application.
    
    Demonstrates basic functionality and can be extended
    with GitHub Copilot assistance.
    """
    print("=" * 50)
    print("GitHub Copilot Demo - Python Project")
    print("=" * 50)
    
    # Greet the user
    message = greet("Developer")
    print(f"\n{message}\n")
    
    # Example: Calculate and display fibonacci sequence
    # GitHub Copilot can help extend this with more features
    print("This is a starter Python project.")
    print("Use GitHub Copilot to help you build amazing things!")
    print("\nTips:")
    print("- Write comments describing what you want")
    print("- Use Copilot Chat for explanations and assistance")
    print("- Follow Python best practices for better suggestions")


if __name__ == "__main__":
    main()

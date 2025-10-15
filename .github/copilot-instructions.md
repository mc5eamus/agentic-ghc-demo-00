# GitHub Copilot Instructions

This file provides guidelines for GitHub Copilot to generate code that adheres to the project's quality standards and best practices.

## Code Quality Standards

### Python Style Guidelines

- **Follow PEP 8**: All Python code must adhere to PEP 8 style guidelines
- **Use type hints**: Always include type hints for function parameters and return values
- **Write docstrings**: All functions and classes must have descriptive docstrings following Google or NumPy style
- **Maximum line length**: Keep lines under 100 characters
- **Use meaningful names**: Variable, function, and class names should be descriptive and follow Python naming conventions

### Documentation

- **Module docstrings**: Every Python module should start with a docstring describing its purpose
- **Function docstrings**: Include description, Args, Returns, and Raises sections where applicable
- **Inline comments**: Use clear, concise comments to explain complex logic
- **Keep documentation up-to-date**: Update docstrings and comments when code changes

### Code Structure

- **Modular design**: Break down complex functions into smaller, focused functions
- **Single Responsibility Principle**: Each function should have one clear purpose
- **DRY (Don't Repeat Yourself)**: Avoid code duplication
- **Proper imports**: Group imports in the standard order (standard library, third-party, local)

### Testing

- **Write tests first**: Follow test-driven development when appropriate
- **Test coverage**: Aim for high test coverage of all functions
- **Descriptive test names**: Test function names should clearly describe what they test
- **Test edge cases**: Include tests for empty inputs, special characters, and boundary conditions
- **Use pytest**: All tests should use pytest framework with clear assertions

### Code Quality Tools

- **Black formatter**: Code must pass black formatting checks
- **Flake8 linter**: Code must pass flake8 checks with no warnings
- **pytest**: All tests must pass before committing

### Best Practices

- **Error handling**: Use appropriate exception handling with specific exception types
- **Input validation**: Validate function inputs and handle invalid cases gracefully
- **Avoid magic numbers**: Use named constants instead of hardcoded values
- **Type safety**: Leverage Python's type hints for better code clarity
- **Security**: Never commit credentials, API keys, or sensitive data

### Git and Version Control

- **Clear commit messages**: Use descriptive commit messages that explain what and why
- **Small commits**: Make focused, incremental commits
- **Feature branches**: Create feature branches following the pattern `feature/description`

### Project-Specific Guidelines

- **Python version**: Target Python 3.8 or higher
- **Virtual environments**: Always work within a virtual environment
- **Dependencies**: Keep requirements.txt updated with pinned versions

## Copilot Usage Tips

When using GitHub Copilot with this project:

1. **Provide context**: Write clear comments describing what you want to achieve
2. **Review suggestions**: Always review and test Copilot's suggestions before accepting
3. **Use Copilot Chat**: Leverage `/explain`, `/tests`, and `/fix` commands
4. **Maintain consistency**: Ensure generated code matches the existing code style
5. **Generate tests**: Ask Copilot to generate tests for new functions

## Example Code Pattern

```python
"""
Module description goes here.
"""

from typing import List, Optional


def example_function(param: str, count: int = 0) -> List[str]:
    """
    Brief description of what the function does.
    
    Args:
        param (str): Description of param
        count (int): Description of count, defaults to 0
        
    Returns:
        List[str]: Description of return value
        
    Raises:
        ValueError: When param is empty
    """
    if not param:
        raise ValueError("param cannot be empty")
    
    return [param] * max(count, 1)
```

## Code Review Checklist

Before submitting code, ensure:

- [ ] Code follows PEP 8 guidelines
- [ ] All functions have type hints and docstrings
- [ ] Tests are written and passing
- [ ] Black formatting is applied
- [ ] Flake8 shows no warnings
- [ ] No sensitive data or credentials in code
- [ ] Documentation is updated if needed

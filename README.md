# agentic-ghc-demo-00

A Python project demonstrating GitHub Copilot integration and best practices.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- GitHub Copilot extension (for your IDE)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mc5eamus/agentic-ghc-demo-00.git
cd agentic-ghc-demo-00
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
agentic-ghc-demo-00/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── __init__.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Usage

Run the main application:
```bash
python src/main.py
```

## GitHub Copilot Tips

This project is designed to work seamlessly with GitHub Copilot. Here are some tips:

### 1. Use Descriptive Comments
Write clear comments describing what you want to achieve, and Copilot will suggest implementations:
```python
# Function to calculate fibonacci sequence up to n terms
```

### 2. Follow Python Conventions
- Use PEP 8 style guidelines
- Write docstrings for functions and classes
- Use type hints for better suggestions

### 3. Copilot Chat Commands
- Ask Copilot to explain code: `/explain`
- Request tests: `/tests`
- Fix issues: `/fix`
- Optimize code: Help me optimize this function

### 4. Context is Key
Keep related code in the same file or open multiple files to give Copilot better context for suggestions.

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
This project follows PEP 8 guidelines. Use tools like `black` and `flake8` to maintain code quality:
```bash
black src/
flake8 src/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.
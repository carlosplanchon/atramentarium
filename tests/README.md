# Tests for atramentarium

## Overview

This directory contains the comprehensive test suite for the atramentarium library.

## Test Coverage

- **test_command_completer.py**: Tests for the `CommandCompleter` class
  - Initialization tests
  - History management tests
  - Auto-completion functionality tests
  - Edge cases and sorting tests

- **test_parse_command_list.py**: Tests for the `parse_command_list` function
  - Empty list handling
  - Single and multiple list parsing
  - Order preservation
  - Duplicate handling

- **test_prompt.py**: Tests for the `prompt` function
  - Basic execution flow
  - History file management
  - Custom configuration options
  - Command processing

## Running Tests

### Install dependencies

```bash
# Create virtual environment
uv venv .venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows

# Install development dependencies
uv pip install -e ".[dev]"
```

### Run all tests

```bash
pytest
```

### Run with coverage report

```bash
pytest --cov=atramentarium --cov-report=html
```

### Run specific test file

```bash
pytest tests/test_command_completer.py
```

### Run specific test

```bash
pytest tests/test_command_completer.py::TestCommandCompleter::test_init_empty_list
```

### Run with verbose output

```bash
pytest -v
```

## Test Statistics

Current coverage: **100%**
Total tests: **26**

## Contributing

When adding new features to atramentarium, please ensure:
1. All new code has corresponding unit tests
2. Tests maintain 100% code coverage
3. All tests pass before submitting a PR
4. Test names clearly describe what they test

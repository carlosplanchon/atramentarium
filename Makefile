.PHONY: help test test-cov test-verbose clean install dev-install

help:
	@echo "Available targets:"
	@echo "  test         - Run all tests"
	@echo "  test-cov     - Run tests with coverage report (HTML)"
	@echo "  test-verbose - Run tests with verbose output"
	@echo "  clean        - Remove generated files and cache"
	@echo "  install      - Install package in development mode"
	@echo "  dev-install  - Install with development dependencies"

test:
	uv run pytest

test-cov:
	uv run pytest --cov=atramentarium --cov-report=html --cov-report=term-missing

test-verbose:
	uv run pytest -v

clean:
	rm -rf .pytest_cache htmlcov .coverage
	rm -rf atramentarium.egg-info dist build
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

install:
	uv pip install -e .

dev-install:
	uv pip install -e ".[dev]"

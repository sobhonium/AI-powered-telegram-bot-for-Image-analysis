.PHONY: help install test lint format clean run setup

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

setup: ## Set up the project (install dependencies and create .env)
	@echo "Setting up the project..."
	pip install -r requirements.txt
	@if [ ! -f .env ]; then \
		echo "Creating .env file from template..."; \
		cp env.example .env; \
		echo "Please edit .env file with your API keys"; \
	else \
		echo ".env file already exists"; \
	fi

test: ## Run tests
	python test_bot.py

lint: ## Run linting checks
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format: ## Format code with black
	black .

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf images/

run: ## Run the bot
	python main.py

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install black flake8

check: ## Run all checks (lint, test, format check)
	@echo "Running all checks..."
	@make lint
	@make test
	@black --check .

docker-build: ## Build Docker image
	docker build -t imageinsight-bot .

docker-run: ## Run with Docker
	docker run --env-file .env imageinsight-bot 
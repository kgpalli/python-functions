.PHONY: install test format lint help

install:
	python3 -m pip install -r requirements.txt

test:
	pytest
	python3 -m pytest test_wikibot.py

format:
	black .

lint:
	pylint wikibot.py

help:
	@echo "Available commands:"
	@echo "  make install - Install dependencies from requirements.txt"
	@echo "  make test    - Run pytest"
	@echo "  make format  - Format code with black"
	@echo "  make lint    - Lint code with pylint"

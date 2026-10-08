install:
	pip install -e '.[dev]'
	playwright install chromium

quality:
	ruff check .
	mypy atlas

unit:
	pytest tests/framework

api:
	pytest -m api

e2e:
	pytest -m e2e

smoke:
	pytest -m smoke

all:
	pytest -n auto

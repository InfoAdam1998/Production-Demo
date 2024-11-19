.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner

run: install
	cd app && poetry run python run.py

install: pyproject.toml
	poetry install

clean:
	powershell -Command "Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force"

check:
	poetry run flake8 app/

runner: check run clean

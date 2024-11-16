.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner

run:
	cd src && poetry run python runner.py

install: pyproject.toml
	poetry install

clean:
	powershell -Command "Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force"

check:
	poetry run flake8 src/

runner: check run clean 
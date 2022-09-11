VENV_BIN=venv/bin


clean:
	rm -rf venv .out .pytest_cache .tox  dist build
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

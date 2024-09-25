NAME = $(shell basename $(CURDIR))
PYNAME = $(subst -,_,$(NAME))

check:
	ruff check *.py
	flake8 *.py
	mypy *.py
	pyright *.py
	vermin -vv --no-tips -i *.py

build:
	rm -rf dist
	python3 -m build

upload: build
	uv-publish

clean:
	@rm -vrf *.egg-info .venv/ build/ dist/ __pycache__

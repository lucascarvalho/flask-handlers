SHELL := /bin/bash
.DEFAULT_GOAL=help
.PHONY: help

define HELP_TEXT
Help:
-------------------------
+ DEVELOPMENT
    $$ make setup                   - Setup your project installing all the dependencies.
    $$ make test                    - Run tests.
    $$ make publish                 - Publish package on PyPi.
endef
export HELP_TEXT
help:
	@echo "$$HELP_TEXT"

setup:
	@echo 'Installing dependencies...'
	@pip install -r development.txt

test:
	@echo "Running tests..."
	@py.test -s -v tests

publish:
	@echo "Uploading..."
	@python setup.py register -r pypi
	@python setup.py sdist upload -r pypi

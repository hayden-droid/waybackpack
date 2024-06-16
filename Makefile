.PHONY: tests

format:
	black memeitizer tests
	isort memeitizer tests

lint:
	black --check memeitizer tests
	isort --check memeitizer tests
	flake8 memeitizer tests --ignore E501

tests:
	pytest tests -sv --cov

usage:
	COLUMNS=80 memeitizer -h

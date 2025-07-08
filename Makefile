install:
	pipx install --force -e .

build:
	uv build -o /home/charaeva/python-project-50/dist

package-install:
	uv run pipx install --force dist/*.whl

gendiff:
	uv run gendiff

lint:
	ruff check gendiff

diff:
	uv run gendiff gendiff/file1.json gendiff/file2.json

test:
	PYTHONPATH=$(shell pwd) pytest -v tests/

.PHONY: test lint install
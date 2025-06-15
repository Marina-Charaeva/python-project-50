install:
	uv sync --force-reinstall

build:
	uv build -o /home/charaeva/python-project-50/dist

package-install:
	uv run pipx install --force dist/*.whl

gendiff:
	uv run gendiff

lint:
	uv run flake8 gendiff

diff:
	uv run gendiff gendiff/file1.json gendiff/file2.json

test:
	uv run pytest -v tests/

.PHONY: test install
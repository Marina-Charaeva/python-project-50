install:
	uv sync --force-reinstall

build:
	uv build -o /home/charaeva_ma/python/python-project-50/dist

package-install:
	uv tool pipx install --force dist/*.whl

gendiff:
	uv run gendiff

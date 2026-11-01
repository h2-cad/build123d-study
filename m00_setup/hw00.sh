#!/bin/bash

uv export --format requirements.txt > requirements.txt
grep -E "^(build123d|ocp-vscode|cadquery-ocp-novtk)==" requirements.txt
uv run python -c "from importlib.metadata import version as v; print('\n', v('build123d'), '\n', v('cadquery-ocp-novtk'), '\n', v('ocp-vscode'))"
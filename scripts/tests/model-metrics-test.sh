#!/bin/sh

set -e

python -m pytest -rA --cov-report term tests/test_model_metrics.py

# -r displays extra test summary info and test logs
# -A configures -r for (A)ll tests, or (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed, (p)assed, (P)assed with output, (a)ll except passed (p/P) tests
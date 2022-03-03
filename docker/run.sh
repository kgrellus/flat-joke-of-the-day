#!/usr/bin/env bash

set -eo pipefail
#SCRIPT_DIR="$(cd "$(dirname "$0")" ; pwd -P)"

pipenv install
pipenv run python -u main.py

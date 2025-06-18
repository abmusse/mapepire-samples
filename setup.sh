#!/usr/bin/env bash

set -x
set -e

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

mv mapepire.ini.example mapepire.ini

python setup.py


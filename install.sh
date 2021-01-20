#!/bin/bash

# python scripts personal project installation script
#
# usage: ./install.sh
#
# 2020-01-20

set -euo pipefail
# initalise submodule
git submodule update --init --recursiv
# install virtual environment
virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt


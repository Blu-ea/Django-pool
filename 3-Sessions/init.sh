#!/bin/sh

RACINE="$(realpath "$(dirname "$0")")"

cd $RACINE

VENV_NAME=".venv"
SOURCE="bin/activate"

python3 -m venv $VENV_NAME
source $VENV_NAME/$SOURCE
python3 -m pip install --upgrade --log log.log -r requirements.txt

cd - > /dev/null
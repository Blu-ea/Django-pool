#!/bin/usr/sh

VENV_NAME=".venv"
SOURCE="bin/activate"

python3 -m venv $VENV_NAME
source $VENV_NAME/$SOURCE
python3 -m pip install --upgrade --log pip.log -r requirements.txt

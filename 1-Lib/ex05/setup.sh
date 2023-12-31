#!/bin/usr/sh

VENV_NAME="django_venv"
SOURCE="bin/activate"

python3 -m venv $VENV_NAME
source $VENV_NAME/$SOURCE
python3 -m pip install --upgrade -r requirement.txt  --log pip.log 

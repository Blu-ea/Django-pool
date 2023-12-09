#!/usr/bin/sh

echo -n '\033[33m'
pip3 -V
echo -n '\033[30m'
python3 -m pip install -q --force-reinstall --upgrade --log path.log -t local_lib git+https://github.com/jaraco/path.git#egg=path
echo '\033[00m'

python3 my_program.py
#!/usr/bin/sh
curl $1 -s | grep body | cut -d '"' -f 2 
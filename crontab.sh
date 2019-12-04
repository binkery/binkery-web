#!/bin/sh
cd /usr/share/nginx/binkery-web/
git pull
cd /usr/share/nginx/binkery-web/python/
python3 run.py

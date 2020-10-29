#!/bin/sh
cd /root/html/binkery-web/
COUNT=$(git pull | grep "Already up-to-date" | grep -v "grep" | wc -l)
if [ $COUNT -eq 1 ]; then
    exit 0
fi
cd /root/html/binkery-web/python/
python3 run.py

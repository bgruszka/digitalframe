#!/usr/bin/env bash

xset -dpms; xset s off

cd /home/pi/digitalframe && source venv/bin/activate && PYTHONPATH=. python run.py

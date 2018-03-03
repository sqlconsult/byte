#!/usr/bin/env bash

# run wsgi.py immune to hangups, with output to non-tty
nohup python3 run/wsgi.py &

#!/usr/bin/env bash

clear
rm logs/*
python3 seed.py
chmod +w debit.db
python3 controller.py
rm -rf __pycache__/
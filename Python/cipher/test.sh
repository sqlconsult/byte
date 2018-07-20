#!/usr/bin/env bash


clear
pytest -s -v test_cipher.py
rm -rf __pycache__/
rm -rf .pytest_cache/
#!/usr/bin/env bash

clear
pytest -s -v test_candy.py
pytest -s -v test_controller.py
pytest -s -v test_file_exists.py
pytest -s -v test_isnumber.py
pytest -s -v test_read.py
pytest -s -v test_write.py
rm -rf .pytest_cache
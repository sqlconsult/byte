#!/usr/bin/env bash
python3 sanitize_input.py

python3 create_controllers.py
python3 create_core.py
python3 create_desc.py
python3 create_structure.py
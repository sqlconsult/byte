#!/usr/bin/env bash
clear

rm -rf run/core/controllers/__pycache__
rm -rf run/core/__pycache__

echo $PWD
tree -a --dirsfirst -I ".git|venv|.idea"
echo ''
git status
echo ''

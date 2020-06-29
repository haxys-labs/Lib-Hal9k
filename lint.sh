#!/bin/bash
isort hal9k/*.py tests/*.py
black -l 79 hal9k/ tests/
pydocstyle hal9k/* tests/*
pycodestyle hal9k/* tests/*
pylint hal9k/

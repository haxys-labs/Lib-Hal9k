#!/bin/bash

rm -fr build/ dist/ *.egg-info/
python setup.py sdist bdist_wheel
echo Checking distribution...
twine check dist/*
echo
echo If distribution is ready, run the following:
echo * twine-test.sh
echo * twine-push.sh

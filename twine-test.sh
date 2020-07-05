#!/bin/bash

twine upload --repository-url https://test.pypi.org/legacy/ dist/*
echo If all is well, run twine-push.sh.

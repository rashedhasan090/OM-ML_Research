#!/bin/bash

for py_file in $(find -name *.py)
do
    python $py_file
done

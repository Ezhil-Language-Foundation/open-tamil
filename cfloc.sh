#!/bin/bash -x
echo "Classes Functions and LOC for `pwd`"
echo "LOC"
find ./ -iname '*.py' | xargs wc -l
echo "Class"
find ./ -iname '*.py' | xargs grep 'class ' | wc -l
echo "Functions"
find ./ -iname '*.py' | xargs grep 'def ' | wc -l

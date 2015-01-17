#!/bin/bash
for i in `ls *.py`; 
do 
  echo $i; 
  echo ##########################; 
  echo python $i; 
  python $i; 
done


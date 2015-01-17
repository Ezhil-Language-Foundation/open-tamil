#!/bin/bash
for i in `ls *.py`; 
do 
  echo $i; 
  echo ######## P Y T H O N / 3 ##################; 
  echo python3 $i; 
  python3 $i; 
done


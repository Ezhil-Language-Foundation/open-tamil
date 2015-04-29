#!/bin/bash
for i in `ls *.tgz`;
do
echo '########## unpacking data file ' $i ' into ' `pwd`' ################'
sleep 1
tar -xzvf  $i
done
mv TaWiktionary/tamil-wikipedia-031615/*.txt -vi ./
rm -fr ./TaWiktionary


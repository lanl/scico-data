#! /bin/bash

git checkout main -- ../notebooks

for f in ../notebooks/*.ipynb; do
    b=`basename $f`
    if [ "$b" != "index.ipynb" ]; then
      python colabmodipynb.py $f $f
    fi
done

exit 0

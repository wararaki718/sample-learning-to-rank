#!/bin/bash

cd elasticsearch-learning-to-rank/demo

## download data & ranklib
# python prepare.py
cp /work/demo/* .

## wait for statup the elasticsearch
status='red'
while [ "$status" != "green" ]
do
    echo "elasticsearch status: $status"
    sleep 10
    response=`curl ${ES_HOST}:${ES_PORT}/_cat/health?h=status`
    status=`echo "$response" | sed -r 's/^[[:space:]]+|[[:space:]]+$//g'`
done

python index_ml_tmdb.py

python load_features.py

python train.py

echo "learning-to-rank setup is complemeted!!"

# python search.py Rambo
#python search_with_ltr.py --keyword Ramob

echo "DONE"

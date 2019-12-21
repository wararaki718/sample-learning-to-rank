#!/bin/bash

cd elasticsearch-learning-to-rank/demo

## download data & ranklib
# python prepare.py

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

echo "unused learning-to-rank" 
python search.py Rambo

python load_features.py

python train.py

echo "use learning-to-rank"
python search.py Rambo

echo "DONE"

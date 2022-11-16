#!/bin/bash

if [[ -z $1 ]]
then
echo "key DB name container is required. Exiting."
else
echo Building fake grabber
docker build --rm --no-cache -t fake-grabber grabber_app/.
echo Running fake grabber with args: "$@"
HOST=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' $1) # get the keydb host
echo HOST "$HOST"
if [[ -z $2 ]];
then
echo "Running fake grabber container without test"
docker run --rm --name fake-grabber-container -t fake-grabber $HOST
else
echo "Running fake grabber container with test"
docker run --rm --name fake-grabber-container -t fake-grabber $HOST $2
fi
fi

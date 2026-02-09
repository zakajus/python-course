#!/bin/bash

command=$1

case $command in
    run)
        docker run -d --name pydb -p 27017:27017 mongo
        ;;
    kill)
        docker kill pydb
        ;;
    rm)
        docker rm pydb
        ;;
    shell)
        docker exec -it pydb mongosh
        ;;
    clean)
        docker kill pydb && docker rm pydb
        docker run -d --name pydb -p 27017:27017 mongo
        ;;
esac

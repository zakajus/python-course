#!/bin/bash

command=$1

case $command in
    run)
        docker run -d --name restaurants -p 27017:27017 mongo
        ;;
    kill)
        docker kill restaurants
        ;;
    rm)
        docker rm restaurants
        ;;
    shell)
        docker exec -it restaurants mongosh
        ;;
    clean)
        docker kill restaurants && docker rm restaurants
        docker run -d --name restaurants -p 27017:27017 mongo
        ;;
esac

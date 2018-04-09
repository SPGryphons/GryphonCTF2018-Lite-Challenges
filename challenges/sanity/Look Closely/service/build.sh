#!/bin/sh
docker build -t look_closely .
docker run --restart always --memory 64M -d -p 18112:80 --name sanity-look_closely look_closely
docker start san-look_closely

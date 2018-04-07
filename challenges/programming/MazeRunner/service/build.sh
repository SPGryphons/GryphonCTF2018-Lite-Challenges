#!/bin/bash
docker build -t mazerunner .
docker run -d --restart always --memory 128M -p 10000:50000 --name mazerunner mazerunner
docker start mazerunner
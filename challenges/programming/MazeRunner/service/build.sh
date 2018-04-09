#!/bin/bash
docker build -t prog-mazerunner .
docker run -d --restart always --memory 128M -p 18174:50000 --name prog-mazerunner prog-mazerunner
docker start prog-mazerunner
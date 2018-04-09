#!/bin/sh
docker build -t mathgenius .
docker run --restart always --memory 64M -d -p 18171:30152 --name prog-math mathgenius
docker start prog-math

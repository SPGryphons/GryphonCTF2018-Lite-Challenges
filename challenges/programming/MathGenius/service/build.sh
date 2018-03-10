#!/bin/sh
docker build -t mathgenius .
docker run --restart always --memory 64M -d -p 16341:30152 --name prog-math mathgenius
docker start prog-math

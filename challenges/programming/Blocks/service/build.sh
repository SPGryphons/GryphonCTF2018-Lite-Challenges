#!/bin/sh
docker build -t prog-blocks .
docker run -d --restart always --memory 128M -p 10000:50000 --name prog-blocks prog-blocks
docker start prog-blocks
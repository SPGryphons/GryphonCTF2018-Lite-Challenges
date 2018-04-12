#!/bin/bash
docker build -t web-teamlist .
docker run --restart always -d -p 18136:80 --name web-teamlist web-teamlist
docker start web-teamlist
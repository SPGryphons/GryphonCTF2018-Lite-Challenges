#!/bin/sh
docker build -t freeflag .
docker run --restart always --memory 128M -d --cap-drop=all -p 18111:5003 --name sanity-freeflag freeflag
docker start sanity-freeflag
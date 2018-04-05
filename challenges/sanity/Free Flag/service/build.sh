#!/bin/sh
docker build -t freeflag .
docker run --restart always --memory 128M -d --cap-drop=all -p 5003:5003 --name sanity-freeflag freeflag
docker start sanity-freeflag
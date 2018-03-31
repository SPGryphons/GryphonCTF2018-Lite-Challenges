#!/bin/sh
docker build -t crystalball .
docker run --restart always --memory 128M -d --cap-drop=all -p 5002:5002 --name reverse-crystalball crystalball
docker start reverse-crystalball

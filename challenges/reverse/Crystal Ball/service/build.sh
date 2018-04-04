#!/bin/sh
docker build -t crystalball .
docker run --restart always --memory 128M -d --cap-drop=all -p 18211:5002 --name reverse-crystalball crystalball
docker start reverse-crystalball

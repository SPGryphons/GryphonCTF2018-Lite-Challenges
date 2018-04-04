#!/bin/sh
docker build -t optimusprime .
docker run --restart always --memory 128M -d --cap-drop=all -p 18172:5001 --name prog-optimusprime optimusprime
docker start prog-optimusprime

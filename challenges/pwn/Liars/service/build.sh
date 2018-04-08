#!/bin/sh
docker build -t liars .
docker run --restart always --memory 128M -d --cap-drop=all -p 18154:5001 --name pwn-liars liars
docker start pwn-liars

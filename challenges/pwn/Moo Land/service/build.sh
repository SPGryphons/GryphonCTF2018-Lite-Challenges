#!/bin/sh
docker build -t mooland .
docker run --restart always --memory 128M -d --cap-drop=all -p 5000:5000 --name pwn-mooland mooland
docker start pwn-mooland

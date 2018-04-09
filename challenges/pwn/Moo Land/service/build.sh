#!/bin/sh
docker build -t mooland .
docker run --restart always --memory 128M -d --cap-drop=all -p 18151:5000 --name pwn-mooland mooland
docker start pwn-mooland

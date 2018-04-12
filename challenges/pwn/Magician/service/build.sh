#!/bin/sh
docker build -t magician .
docker run --restart always --memory 128M -d -p 18155:5000 --name pwn-magician magician
docker start pwn-magician

#!/bin/sh
docker build -t MooLand .
docker run --restart always --memory 128M -d -p 5000:5000 --name pwn-MooLand MooLand
docker start pwn-MooLand
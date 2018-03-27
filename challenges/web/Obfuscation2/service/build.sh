#!/bin/sh
docker build -t obfuscation2 .
docker run --restart always --memory 128M -d -p 8081:80 --name web-obfuscation2 obfuscation2
docker start web-obfuscation2
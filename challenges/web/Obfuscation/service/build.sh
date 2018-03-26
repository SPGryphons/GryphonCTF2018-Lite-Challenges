#!/bin/sh
docker build -t obfuscation .
docker run --restart always --memory 128M -d -p 8080:80 --name web-obfuscation obfuscation
docker start web-obfuscation
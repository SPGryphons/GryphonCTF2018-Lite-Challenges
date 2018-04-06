#!/bin/sh
docker build -t savemycat .
docker run --restart always --memory 128M -d -p 18155:22 --name pwn-savemycat savemycat
docker start pwn-savemycat

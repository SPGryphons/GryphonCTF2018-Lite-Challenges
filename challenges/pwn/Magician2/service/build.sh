#!/bin/bash

docker build -t pwn-magic2 .
docker run --restart always --memory 128M --name pwn-magic2 -dt -p 18156:12345 pwn-magic2

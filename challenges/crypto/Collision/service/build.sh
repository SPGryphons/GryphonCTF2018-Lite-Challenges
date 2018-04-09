#!/bin/bash
docker build -t collision .
docker run --restart always -d -p 18191:80 --name crypto-collision collision
docker start crypto-collision
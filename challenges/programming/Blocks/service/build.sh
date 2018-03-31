#!/bin/bash
docker build -t blocks .
docker run -d --restart always --memory 128M -p 10000:50000 --name blocks blocks
docker start blocks
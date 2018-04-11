#!/bin/bash
docker build -t prog-socketz .
docker run -d --restart always --memory 128M -p 18177:18177 --name prog-socketz prog-socketz
docker start prog-socketz
#!/bin/sh
docker build -t lookitup .
docker run --restart always -d -p 18173:18173 --name prog-lookitup lookitup
docker start lookitup

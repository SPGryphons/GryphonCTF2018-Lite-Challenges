#!/bin/bash

docker build -t candyflow .
docker run --restart always --memory 128M --name pwn-candyflow -dt -p 18152:12345 candyflow

#!/bin/bash

docker build -t prog-giffpassword .

docker run --name prog-giffpassword -d -p 18176:12345 prog-giffpassword


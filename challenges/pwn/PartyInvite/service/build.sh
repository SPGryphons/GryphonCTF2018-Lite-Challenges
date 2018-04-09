#!/bin/sh
docker build -t pwn-partyinvite .
docker run -d --restart always --memory 64M -p 18153:50000 --name pwn-partyinvite pwn-partyinvite
docker start pwn-partyinvite
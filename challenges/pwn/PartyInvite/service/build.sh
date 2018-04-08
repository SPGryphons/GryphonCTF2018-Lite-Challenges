#!/bin/sh
docker build -t partyinvite .
docker run -d --restart always --memory 64M -p 18153:50000 --name partyinvite partyinvite
docker start partyinvite
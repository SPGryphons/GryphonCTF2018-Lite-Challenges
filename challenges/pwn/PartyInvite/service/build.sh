#!/bin/bash
docker build -t partyinvite .
docker run -d --restart always --memory 64M -p 10000:50000 --name partyinvite partyinvite
docker start partyinvite
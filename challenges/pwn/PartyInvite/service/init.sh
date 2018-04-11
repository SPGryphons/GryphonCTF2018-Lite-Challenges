#!/bin/sh
tar -xzvf partyinviteImage.zip
docker load -i partyinviteImage
docker run -dit --restart always --memory 64M -p 18153:50000 --name pwn-partyinvite pwn-partyinvite
docker start pwn-partyinvite
rm partyinviteImage

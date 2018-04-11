#!/bin/sh
docker build -t pwn-partyinvite .
docker save pwn-partyinvite -o ../partyinviteImage
tar -cvzf ../partyinviteImage.zip ../partyinviteImage
rm ../partyinviteImage

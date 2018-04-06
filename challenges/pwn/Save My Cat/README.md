# Save My Cat

## Question Text

I lost my cat! Help me find it please!!!

`ssh player@pwn.chal.gryphonctf.com -p <port>` Password is `gryphonctflite2018`

*Creator - PotatoDrug*

## Setup Guide

Run `./build.sh`

## Solution
The players are suppose to cat the hidden file `.flag.txt` however if they try to cat it using `cat .flag.txt` there will be an error because in `.bashrc` cat is set to be the alias of nothing.

So to cat the flag u need to remove the alias `alias cat='` by running `unalias cat`, then you can run `cat .flag.txt`.

sftp is disable so users cannot sftp in to retrieve `.flag.txt`

### Flag
`GCTF{jU57_5AY1n9_1_PR3F3r_D092}`

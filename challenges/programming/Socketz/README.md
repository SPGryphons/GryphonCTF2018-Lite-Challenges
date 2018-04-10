# Socketz

## Question Text

I am here to teach you about socket programming with python! Sounds intimidating? Let me be the first to tell you it's not :D

Connect to the server at `prog.chal.gryphonctf.com` at port `18177` and send over 64 bytes with the value FF to get the flag!

It would be nice to use the python script provided, *just sayin*

*Creator - Chuan Kai (@exetr)*

## Setup Guide
1. run `sudo ./build.sh`

## Distribution
- pysocket.py
    - SHA1: `277e46f67d64f5c1c97e564e474d8e8f8dc7a0de`
    - A sample socket coded in python

## Solution
1. Since the requested value of 64 0xFF cannot be physically typed out using a keyboard, make use of encoding in python! `msg = "\xFF"*64`
2. Send that to the server and the flag will be revealed

### Flag
`GCTF{s0ck3tz_ar3_amaz1ng!!}`
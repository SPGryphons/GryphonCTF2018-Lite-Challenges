# File Transfer

## Question Text

I wonder why is TCP port 21 open

*Creator - @Infinitide*

## Setup Guide
1. Copy the files in service to your FTP root directory
2. Ensure that anonymous login for FTP is enabled

## Solution
There are 2 ways to do this
1. Browse to `ftp://192.168.8.31`
2. Run the command `ftp 192.168.8.31`. Login using `anonymous` as the username. You will be able to view the files using normal linux commands

### Flag
`GCTF{1_f0rg07_7o_d15ab1e_an0nym0u5_l0gin_}`

## Recommended Reads
* https://en.wikipedia.org/wiki/File_Transfer_Protocol

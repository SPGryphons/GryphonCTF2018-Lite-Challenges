# Teamlist

## Question Text
Here's a database with your team inforamtion, try it out!

Although, some part of me feels that I might have left a flag or two inside

`http://web.chal.gryphonctf.com:18136`

*Creator - Chuan Kai (@exetr)*

### Hint
1. SQL Injection may help you

## Setup Guide
1. Run `sudo ./build.sh` in the `distrib` folder

## Solution
1. A simple SQL injection exploit, enter `' OR '1'='1` to dump out the entire table
### Flag
`GCTF{GCTF{a1way5_us3_pr3par3d_stat3m3ntz!}`

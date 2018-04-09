# Collision

## Question Text
Ever heard of the concept that there can be no same hash value for two different files? Well, let me be the first to tell you that that is entirely possible. 
I want two different files that have the same SHA1 checksum value. Additionally, once a pair of files have been accepted, they cannot be used again to solve this challenge. 
Up for the challenge? Head over to `http://crypto.chal.gryphonctf.com:18191`

*Creator - Chuan Kai (@exetr)*

## Setup Guide
1. Run `sudo ./build.sh` in the `distrib` folder

## Solution
1. This challenge banks on the concept that there are ways to generate files whcih result in collided SHA1 hash checksums
2. Recommended solution is to utilise tools that can be found online which can generate a pair of colliding PDF files - https://github.com/nneonneo/sha1collider and  https://alf.nu/SHA1
3. A pair of colliding PDF files has been provided in the `generate` folder
### Flag
`GCTF{c0llisi0n_av0id4nc3_f0r_n00b5}`

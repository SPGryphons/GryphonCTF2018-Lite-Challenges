# Candy Overflow

## Question Text

Mummy said I can have as many candy as I want if I can't count my candies from countable candies.

*Creator - @IncompetentDev*

## Setup Guide
1. Build binaries: `make` in generate
2. Build docker image: `./build.sh` in service
3. Run docker image: `./run.sh` in service

## Solution
This is an integer overflow problem, where two numbers(unsigned long long, 64bit integer) are added together and casted into a 32 bit integer (signed "normal"/long int).

Connect with `nc` and enter `2147483647` (2^31-1), then enter `2147483648` (2^31) as the second number. 

An overflow will always happen because a 64-bit integer is assigned to a 32-bit integer (higher order bits are ignored). The goal here is to get the binary repreesentation of -1 (two's complement, signed integer: all 32 digits have value of 1). 

### Flag
`GCTF{c4ndy_f0r_d4y5}`



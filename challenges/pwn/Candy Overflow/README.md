# Candy Overflow

## Question Text

Mummy said I can have as many candy as I want if I can't count my candies from countable candies.

Connect with `nc pwn.chal.gryphonctf.com 18152`.

*Creator - @IncompetentDev*

## Setup Guide
1. Build binaries: `make` in generate
2. Build docker image: `./build.sh` in service
3. Run docker image: `./run.sh` in service

## Solution
This is an integer overflow problem, where two numbers(unsigned long long, 64bit integer) are added together and casted into a 32 bit integer (signed "normal"/long int).

Connect with `nc` and enter `2147483647` (2^31-1), then enter `2147483648` (2^31) as the second number. 

The goal here is to get the binary representation of -1 stored in a 32-bit integer (using two's complement) by adding two numbers together.

An illustration is shown below:

Input		| Binary 										|
----		| ---											|
2147483647	|`0111 1111, 1111 1111, 1111 1111, 1111 1111`	| 
2147483648	|`1000 0000, 0000 0000, 0000 0000, 0000 0000`	|
**Total**	|`1111 1111, 1111 1111, 1111 1111, 1111 1111`	|	

### Flag
`GCTF{c4ndy_f0r_d4y5}`


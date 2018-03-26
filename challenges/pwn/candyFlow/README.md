# Candy Overflow

Creator - @IncompetentDev

## Question Text

Mummy said I can have as many candy as I want if I can't count my candies from countable candies.

## Setup Guide
1. Build binaries: `make` in generate
2. Build docker image: `./build.sh` in service
3. Run docker image: `./run.sh` in service

## Solution
This is an integer overflow problem, where two numbers must be added to yield a negative number.

Connect with `nc` and enter `2147483647` (2^31 -1), then enter a second non-zero number, which should cause an overflow.

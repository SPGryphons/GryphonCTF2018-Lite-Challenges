# Chinese Calligraphy

## Question Text
Traditionally, Chinese text was written in vertical columns which were read from top to bottom, right-to-left; the first column being on the right side of the page, and the last column on the left. -https://en.wikipedia.org/wiki/Written_Chinese 

*Creator - ccs*

## Hint
8 bits = 1 byte

## Setup Guide
1. Generate image with cc.py

## Distribution
cc1.png `SHA1: 0bb3d0631dda7b92756e6fed1d951381c38ac58c`

## Solution
1. Take each "pixel" as one bit and each 8 pixel tall column as one byte, read from right to left and convert to ascii.

### Flag
`GCTF{chin4_numb3r_0n3}`
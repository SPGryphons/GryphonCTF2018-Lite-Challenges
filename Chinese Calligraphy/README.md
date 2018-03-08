Traditionally, Chinese text was written in vertical columns which were read from top to bottom, right-to-left; the first column being on the right side of the page, and the last column on the left. -https://en.wikipedia.org/wiki/Written_Chinese 

Hint: why is the height 8 pixels?

Setup Guide
1. Generate image with cc.py

Distribution
cc1.png `SHA1: e71ca72ad8df20a6dfbccaefc31ffb27cbef27fd`


Solution
1. Take each pixel as one bit and each 8 pixel tall column as one byte, read from right to left and convert to ascii.

Flag: GCTF{chin4_numb3r_0n3}
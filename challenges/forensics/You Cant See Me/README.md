# You Cant See Me

## Question Text

My friend send me this textfile with a hidden message inside and he told me there are some things that just can't be seen.

Created by PotatoDrug

## Hints (Optional)
1. https://en.wikipedia.org/wiki/Zero-width_space

## Distribution
Distribute all the contents inside `distrib` folder to the users

## Solution
The text in the text file has been encoded with zero width characters. If the letter in the text file is trailed by a zero width character it represents a binary 1, if it is not trailed by a zero width character then it represents a binary 0. Using this we can decode the text to the a binary string which we can then convert to ascii which will be the flag.

Run solution.py to get the flag.

**Flag:** GCTF{z3r0_w1d7h_ch4r4ct3r5}
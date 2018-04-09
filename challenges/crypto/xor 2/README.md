# XOR 2

## Question Text

I found out that the key length is 18 and the message starts with `On a beautiful day`

Note: Each character is 8 bits.

*Creator - PotatoDrug*

## Hints
1. What happens if you xor ciphertext with the plaintext?

## Distribution
- xor2.txt 
  - SHA1: `d966353848dbc308aaee5a9b41451f803809b35f`
  - Contains binary string

## Solution
To solve this you need to know that `ciphertext ^ msg = key` so by doing xoring the first 18 * 8 bits (18 characters) of the cipher text with the known plaintext `On a beautiful day` we will get the key `1wZCt3Jxb#YcQ6Nn0O` which we can then use to decrypt the ciphertext and get the flag.

### Flag 

`GCTF{s33_1N70_7H3_UnkN0Wn}`
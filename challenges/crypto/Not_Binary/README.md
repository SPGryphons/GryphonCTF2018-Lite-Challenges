# Not_Binary

## Question Text

This looks like binary but it's not?

Note: Submit the flag in this format GCTF{\<decrypted text goes here\>}

*Creator - PotatoDrug*

### Hints

1. http://practicalcryptography.com/cryptanalysis/text-characterisation/identifying-unknown-ciphers/

## Distribution
- not_binary.txt 
  - SHA1: `f8ebb7a654a2b7213458ee15a75934e9658eb4ea`
  - Long string of 0s and 1s

## Solution
The flag is encrypted using Baconian Cipher using distinct codes, can be decrypted by submitting it to http://rumkin.com/tools/cipher/baconian.php

### Flag 

`GCTF{ILIKEBACONHOPEULIKEITTOO}`
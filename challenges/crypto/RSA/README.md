# RSA

## Question Text

I found this encrypted message with the private key, can you decrypt it for me?

Created by PotatoDrug

## Distribution
Distribute all the contents inside `distrib` folder to the users

## Solution
Run `openssl rsautl -decrypt -in 785c79b5b98aca1fad5aafaffa6b3d5e.rsa -inkey private.pem` to get the flag.

**Flag:** GCTF{45ymM37Ric\_or\_5ymM37Ric\_3nCryP7ION}

## Recommended Reads
* https://en.wikipedia.org/wiki/RSA_(cryptosystem)
* https://en.wikipedia.org/wiki/OpenSSL

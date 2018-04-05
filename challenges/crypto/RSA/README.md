# RSA

## Question Text

I found this encrypted message and the private key, can you decrypt it for me?

Created by PotatoDrug

## Distribution  

`785c79b5b98aca1fad5aafaffa6b3d5e.rsa` - encrypted file  

`e7899cd4e3d4a8a1a076118553fbd27f.pem` - private key

## Solution  

Run `openssl rsautl -decrypt -in 785c79b5b98aca1fad5aafaffa6b3d5e.rsa -inkey private.pem` to get the flag.

### Flag  

`GCTF{45ymM37Ric_or_5ymM37Ric_3nCryP7ION}`

## Recommended Reads  
* https://en.wikipedia.org/wiki/RSA_(cryptosystem)
* https://en.wikipedia.org/wiki/OpenSSL

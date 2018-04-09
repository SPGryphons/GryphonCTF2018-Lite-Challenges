# RSA

## Question Text

I found this encrypted message and the private key, can you decrypt it for me?

*Creator - PotatoDrug*

### Hints

1. https://en.wikipedia.org/wiki/OpenSSL

## Distribution  

- encrypted.rsa 
  - SHA1: `c56135a79a877918ca640da6e12d6ce0124142ff`
  - Encrypted file 
- privatekey.pem 
  - SHA1: `635358112c371ef86e0897485114c701c9d416b4`
  - RSA Private key

## Solution  

RSA is an asymmetric encryption algorithm where the public key is used to encrypt messages and private key is used to decrypt messages, so given the encrypted message and the private key you are able to decrypt the message.

Run `openssl rsautl -decrypt -in encrypted.rsa -inkey privatekey.pem` to get the flag.

### Flag  

`GCTF{45ymM37Ric_or_5ymM37Ric_3nCryP7ION}`

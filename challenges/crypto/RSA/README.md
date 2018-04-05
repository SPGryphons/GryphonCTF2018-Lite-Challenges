# RSA

## Question Text

I found this encrypted message and the private key, can you decrypt it for me?

*Creator - PotatoDrug*

## Distribution  

- encrypted.rsa `785c79b5b98aca1fad5aafaffa6b3d5e`
  - Encrypted file 
- privatekey.pem `e7899cd4e3d4a8a1a076118553fbd27f`
  - RSA Private key

## Solution  

RSA is an asymmetric encryption algorithm where the public key is used to encrypt messages and private key is used to decrypt messages, so given the encrypted message and the private key you are able to decrypt the message.

Run `openssl rsautl -decrypt -in encrypted.rsa -inkey privatekey.pem` to get the flag.

### Flag  

`GCTF{45ymM37Ric_or_5ymM37Ric_3nCryP7ION}`

## Recommended Reads  
* https://en.wikipedia.org/wiki/RSA_(cryptosystem)
* https://en.wikipedia.org/wiki/OpenSSL

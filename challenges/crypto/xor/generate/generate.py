#!/usr/bin/env python3
import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def encrypt(message, key):
    # generate key with same length as message
    length = len(message)
    while len(key) < length:
        key += key
    if len(key) != length:
        key = key[:length-len(key)]
    tmp = bin(int(text_to_bits(message), 2) ^ int(text_to_bits(key), 2))[2:]
    print(text_to_bits(key))
    while len(tmp) % 8 != 0:
        tmp = '0' + tmp
    return tmp

def main():
    print(encrypt('GCTF{5xc1us1v5_0r_0r_x0r}', 'K5QS1NkXAzwvl4yC4b4rD1HpP'))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import binascii, sys
from string import ascii_letters, digits

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def binaryToText(num):
    n = int(num, 2)
    try:
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8')
    except UnicodeDecodeError:
        return ''

def decrypt(ciphertext, key):
    length = len(ciphertext) // 8
    # generate key with same length as message
    while len(key) < length:
        key += key
    if len(key) != length:
        key = key[:length-len(key)]
    return binaryToText(bin(int(ciphertext, 2) ^ int(text_to_bits(key), 2))[2:])

def main():
    if len(sys.argv) != 2:
        print('Usage: {} <file>'.format(sys.argv[0]))
        sys.exit()
    with open(sys.argv[1], 'r') as f:
        unknown = f.read()
    key = decrypt(unknown[:18 * 8], 'On a beautiful day')
    print(decrypt(unknown, key))

if __name__ == '__main__':
    main()

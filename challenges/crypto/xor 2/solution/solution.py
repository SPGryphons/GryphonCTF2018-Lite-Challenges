#!/usr/bin/env python3
import binascii
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

from itertools import chain, product
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

def main():
    unknown = '011111110001001000100100000111000100001100111111010000000110101000001000000011100000010000110010000010110000111000011011011010010100000100001110000001110011101101001011000011100000010001101010000010000000111000000111001111110101100100111010000110110011000101000101'
    for key in bruteforce(ascii_letters + digits, 10):
        plaintext = decrypt(unknown, key)
        if 'GCTF{' in plaintext:
            print(plaintext)
            break

if __name__ == '__main__':
    main()

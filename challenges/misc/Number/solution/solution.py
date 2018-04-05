#!/usr/bin/env python3

secret = 42845235478864399078938707580578182161112283111191491281129481369162793604474181848504741958519875255579654124669

def decimalToAscii(num):
    tmp = num.to_bytes((num.bit_length() + 7) // 8, 'big')
    return tmp.decode('ascii')

print('Flag: {}'.format(decimalToAscii(secret)))


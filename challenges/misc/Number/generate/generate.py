#!/usr/bin/env python3
from binascii import hexlify

msg = 'GCTF{c0m1ng_up_w1th_fl4g5_15_the_h4rdest_pa4rt}'

def asciiToDecimal(msg):
    return int.from_bytes(bytearray(msg, 'ascii'), byteorder='big', signed=False)

with open('number.txt', 'w') as f:
    f.write(str(asciiToDecimal(msg)))


#!/usr/bin/env python3
import base64

flag = 'GCTF{e1ght_s1xt55n_th1rtytw0_s1xtyf0ur}'

b8 = ''
for char in flag:
    b8 += '{} '.format(oct(ord(char))[2:])
b8 = b8.rstrip()
b16 = base64.b16encode(b8.encode('ascii'))
b32 = base64.b32encode(b16)
b64 = str(base64.b64encode(b32))[2:-1]
print(b64)
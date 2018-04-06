#!/usr/bin/env python3
import base64, sys

if len(sys.argv) != 2:
    print('Usage: {} <file>'.format(sys.argv[0]))

with open(sys.argv[1], 'r') as f:
    content = f.read()

b32 = base64.b64decode(content.encode('ascii'))
b16 = base64.b32decode(b32)
b8 = base64.b16decode(b16).split()

flag = ''
for num in b8:
    # convert octal number to int, then to a char
    flag += chr(int(num, 8))

print(flag)

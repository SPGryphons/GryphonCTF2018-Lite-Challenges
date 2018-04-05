#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print('Usage: {} <textfile>'.format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    dirtyString = f.read()
zerowidthc = '​'
# decode the hidden zero width characters to binary
binString = ''
i = 0
while i < len(dirtyString)-1:
    # if a zero width char is found
    if dirtyString[i+1] == zerowidthc:
        binString += '1'
        i += 2 # plus 2 to skip the zero width char
    # if a zero width char is not found
    else:
        binString += '0'
        i += 1
# convert binary string to ascii
n = int(binString, 2)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
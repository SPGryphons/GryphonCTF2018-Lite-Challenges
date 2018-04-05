#!/usr/bin/python3

# string length must be the bit length of the flag
textString = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in ex et ligula molestie tincidunt. Nam vel eros porta, gravida erat vel, cursus mi. Morbi placerat nibh nec lorem fringilla, in tempor massa orci aliquam.'
flag = 'GCTF{z3r0_w1d7h_ch4r4ct3r5}'
# convert flag to binary string
binString = ''.join('{:08b}'.format(ord(c), 'b') for c in flag)
zerowidthc = '​'
# do the encoding here
newstr = ''
for i in range(len(textString)):
    if binString[i] == '1': # append a zero width char to encode a 1
        newstr += textString[i] + zerowidthc
    else: # do not append to encode a 0
        newstr += textString[i]
with open('2358a7b800730bb71f4fa06842ec910f.txt', 'w') as f:
    f.write(newstr)
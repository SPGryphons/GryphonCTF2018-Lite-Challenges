#!/usr/bin/python3

#usage: ./cc.py <enter text here>
#this program height is 8 pixels

from PIL import Image
import numpy as np
import sys
import binascii



def toBinary(string):
    return "".join([format(ord(char),'#010b')[2:] for char in string])

def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])


print(len(sys.argv[1]) * 8)

newarray = np.zeros(shape = (8, len(sys.argv[1]), 4), dtype=int)

z = len(sys.argv[1]) - 1
y = 0

for x in toBinary(sys.argv[1]):
	if (x == "0"):
		newarray[y][z] = [255, 255, 255, 255]
	if (x == "1"):
		newarray[y][z] = [0, 0, 0, 255]
	y = y + 1
	if (y == 8):
		y = 0
		z = z - 1

print(toBinary(sys.argv[1]))

im = Image.fromarray(newarray.astype('uint8'))
im.save("your_file.png")
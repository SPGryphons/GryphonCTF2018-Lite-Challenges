#!/usr/bin/python3

#usage: ./cc2.py <target file.txt>
#this program gives image height of 500 pixels

from PIL import Image
import numpy as np
import sys
import binascii



def toBinary(string):
    return "".join([format(ord(char),'#010b')[2:] for char in string])

def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])


f = open(sys.argv[1], "r")
text = f.read()
f.close()

newarray = np.zeros(shape = (500, 1 + int(len(text) * 8 / 500), 4), dtype=int)

z = int(len(text) * 8 / 500)
y = 0



for x in toBinary(text):
	if (x == "0"):
		newarray[y][z] = [255, 255, 255, 255]
	if (x == "1"):
		newarray[y][z] = [0, 0, 0, 255]
	y = y + 1
	if (y == 500):
		y = 0
		z = z - 1
		

im = Image.fromarray(newarray.astype('uint8'))
im.save("your_file.png")
#!/usr/bin/python3

from PIL import Image
import numpy as np
import sys
import binascii

#image must be png
#usage: ./solve.py <target image.png>

def toBinary(string):
    return "".join([format(ord(char),'#010b')[2:] for char in string])

def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])


i = Image.open(sys.argv[1])
iarray = np.asarray(i)

binary = ''

for x in range(len(iarray[0]) - 1, -1, -1):
	for y in range(0, len(iarray)):
		if (iarray[y][x][3] == 255):
			if (iarray[y][x][0] == 0):
				binary = binary + str(1)
			if (iarray[y][x][0] == 255):
				binary = binary + str(0)

#this saves the entire text into txt file solve.txt

f = open("solve.txt", "w")
f.write(toString(binary))
f.close()

#if you can't ctrl f solve.txt due to lagging from too much text use this instead
'''
text = toString(binary)
for x in range(0, len(text)):
	if text[x] == 'G' and text[x+1] == 'C':
		print(text[x:x+50])
'''
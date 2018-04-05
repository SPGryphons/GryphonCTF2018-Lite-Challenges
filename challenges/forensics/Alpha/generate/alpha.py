#!/usr/bin/python3

#usage: ./alpha.py <target image.png>

from PIL import Image
import numpy as np
import sys


i = Image.open(sys.argv[1])

#i.show()

iarray = np.asarray(i)

iarray.flags.writeable = True

for x in range(0, len(iarray)):
	for y in range(0, len(iarray[0])):
		iarray[x][y][3] = 0

im = Image.fromarray(iarray.astype('uint8'))
im.save("image.png")

#i.show()

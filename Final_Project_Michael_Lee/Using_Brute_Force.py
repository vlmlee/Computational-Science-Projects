from PIL import Image
import os, sys
import pprint
import time

begin_time = time.time()

im = Image.open("water_1280.bmp")
pix = im.load()

water = 0.0
count = 0.0
wol = 0

Aboxes = []
Bboxes = []

Aregions = []
Bregions = []

for i in range(0,4):
	for j in range(0,4):
		box = (160*i, 200*j, 160*(i+1), 200*(j+1))
		region = im.crop(box)
		aregion = region.transpose(Image.FLIP_TOP_BOTTOM)
		Aboxes.append(box)
		Aregions.append(aregion)

for i in range(4,8):
	for j in range(0,4):
		box = (160*i, 200*j, 160*(i+1), 200*(j+1))
		region = im.crop(box)
		Bboxes.append(box)
		Bregions.append(region)

for k in range(0, 16):
	for i in range(0, 160):
		for j in range(0,200):
			if (k>=0 and k <=3):
				if ((Aregions[k].getpixel((i,j)) == 0 and Bregions[(3-k)].getpixel((i,j)) == wol)):
					water += 1
					count += 1
				else:
					count += 1

			elif (k>=4 and k<=7):
				if ((Aregions[k].getpixel((i,j)) == 0 and Bregions[(11-k)].getpixel((i,j)) == wol)):
					water += 1
					count += 1
				else:
					count += 1

			elif (k>=8 and k<=11):
				if ((Aregions[k].getpixel((i,j)) == 0 and Bregions[(19-k)].getpixel((i,j)) == wol)):
					water += 1
					count += 1
				else:
					count += 1

			elif (k>=12 and k<=15):
				if ((Aregions[k].getpixel((i,j)) == 0 and Bregions[(27-k)].getpixel((i,j)) == wol)):
					water += 1
					count += 1
				else:
					count += 1 

print "The probability of hitting water on both sides is: %f " % (water/count)
print "%s seconds" % (time.time() - begin_time)

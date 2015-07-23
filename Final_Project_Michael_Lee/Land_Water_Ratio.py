from PIL import Image
import random as r
import time

im = Image.open("water_1280.bmp")
pix = im.load()

water = 0.0
land = 0.0
count = 0.0
pixwater = 0.0
pixland = 0.0
pixtotal = 800.*1280.

brute_force_time = time.time()
for i in range(0,1280):
	for j in range(0,800):
		if pix[i,j]:
			pixland += 1
		else:
			pixwater += 1
print "Brute force of land/water surface ratio:"
print "Land percentage: %f " % (pixland/pixtotal)
print "Water percentage: %f " % (pixwater/pixtotal)
print "%s seconds\n" % (time.time() - brute_force_time)

monte_carlo_time = time.time()
while count < 250000:
	x = r.randint(1,1279)
	y = r.randint(1, 799)

	if x <= 639:
		X, Y = x + 640, 800 - y
	elif x >= 640:
		X, Y = x - 640, 800 - y

	if (pix[x,y]):
		land += 1
		count += 1
	else:
		water += 1
		count += 1

print "Monte Carlo Sim. of land/water surface ratio:"
print "Land percentage: %f" % (land/count)
print "Water percentage: %f" % (water/count)
print "%s seconds\n" % (time.time() - monte_carlo_time)
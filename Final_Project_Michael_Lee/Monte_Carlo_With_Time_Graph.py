"""
Written by Michael Lee.

PHYS440: Computational Physics
Final Project, Using Image Processing and Monte Carlo Simulations to Analyze Earth's 
Antipodes
"""

from PIL import Image
import random as r
import time
import matplotlib.pyplot as plt

begin_time = time.time()
im = Image.open("water_1280.bmp")
pix = im.load()

water = 0.0
count = 0.0
wol = 0
timearray = []
probabilityarray = []
coordinates = []

for n in range(100, 100000, 100):
	while count < n:
		x = r.randint(1,1279)  # Use 1279 because the pix max indices are (1279, 799)
		y = r.randint(1, 799)  # The index starts from 1 as well.

		if x <= 639:
			X, Y = x + 640, 800 - y
		elif x >= 640:
			X, Y = x - 640, 800 - y

		# Makes the time complexity O(n^2) if you're
		# searching for the coordinates as well

		if (pix[x,y] == 1 and pix[X,Y] == 1):
			if ((x,y) and (X,Y)) not in coordinates:
				coordinates.append((x,y))
				coordinates.append((X,Y))
			water += 1
			count += 1
		else:
			count += 1

	timearray.append((time.time()-begin_time))
	probabilityarray.append(water/count)

	print "The probability of hitting water on both sides is: %f" % (water/count)
	print "%s seconds" % (time.time() - begin_time)

x = range(100,100000,100)
y = probabilityarray
z = timearray
x_scatter = [item[0] for item in coordinates]
y_scatter = [item[1] for item in coordinates]

plt.subplot(311)
plt.plot(x, y, 'r', label="Monte Carlo")
plt.title('Monte Carlo')
plt.xlabel('Number of Samples Per Trial')
plt.ylabel('Probability')
plt.legend()

plt.subplots_adjust(hspace=.5)

plt.subplot(312)
plt.title('Survey of Time Complexity')
plt.plot(x, timearray, 'b', label="time")
plt.xlabel('Number of Samples Per Trial')
plt.ylabel('Time (seconds)')

plt.subplots_adjust(hspace=.5)

plt.subplot(313)
plt.title('Coordinates for land-land Antipodes')
plt.scatter(x_scatter, map(lambda x: x*-1, y_scatter))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


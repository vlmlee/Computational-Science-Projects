"""
Written by Michael Lee.

PHYS440: Computational Physics
Project 2, Differentiation, Integration, and Root Finding
"""

import numpy as np

def f(x):
	# Use this as your test function.
	return x**2

def weight(index, step_size, number_of_steps):
	if ((index == 0) or (index == number_of_steps)):
		weight = step_size / 3.0
	elif (index%2 == 1):
		weight = 4*step_size / 3.0
	elif (index != 0) and (index != number_of_steps) and (index%2 == 0):
		weight = 2*step_size / 3.0
	return weight

def simpson(function, xmin, xmax, number_of_steps):
	step = float((xmax - xmin)/number_of_steps)
	sum = 0
	for i in range(0, number_of_steps+1):
		x = xmin+i*step
		w = weight(i, step, number_of_steps)
		sum = sum + w*function(x)
	return sum

if __name__ == '__main__':

	a = simpson(f, 0, 1.0, 500)
	error = np.abs(a-1/3.)
	print "The value of the integral for Simpson's rule is %.8f and its error is %e." \
										% (a, error)

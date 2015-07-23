"""
Written by Michael Lee.

PHYS440: Computational Physics
Project 2, Differentiation, Integration, and Root Finding
"""
import numpy as np

def f(x):
	# Use this as a test function.
	return x**2

def weight(index, step_size, number_of_steps):
	# Returns the weight depending on the index.
	# If it equals 0 or N, returns h.
	# if it does not equal 0 or N, returns h/2.
	if (index == 0) or (index == number_of_steps):
		weight = step_size / 2.0
	else:
		weight = step_size
	return weight

def integral(function, xmin, xmax, number_of_steps):
	# Adds up the trapezoid areas by using
	# the function values and the
	# weight function.
	step = float((xmax - xmin) / number_of_steps)
	sum = 0
	for i in range(0, number_of_steps+1):
		x = xmin + i * step
		w = weight(i, step, number_of_steps)
		sum = sum + w * function(x)
	return sum

if __name__ == "__main__":

	a = integral(f, 0, 1.0, 500)
	error = np.abs(a - (1/3.))
	print "The value of the integral by the trapezoid rule is %.8f " \
						"and its error value is %e." % (a, error)
"""
Written by Michael Lee

PHYS440: Computational Physics
Project 2, Differentiation, Integration, and Root Finding
"""

import numpy as np

def f(x):
	# We use f(x) as our test function to test our differentiation program.
	return x**3

def forward_difference(x, h):
	a = (f(x+h) - f(x)) / (h)
	forward_error = np.fabs(round(a) - a)
	return {'value': a, 'error': forward_error}

def central_difference(x, h):
	b = (f(x+h/2) - f(x-h/2)) / h
	central_error = np.fabs(round(b) - b)
	return {'value': b, 'error': central_error}

def extrapolated_difference(x, h):
	c = (4*((f(x+h/4) - f(x-h/4)) / (h/2)) - ((f(x+h/2) - f(x-h/2))/ h)) / 3.0
	extrapolated_error = np.fabs(round(c) - c)
	return {'value': c, 'error': extrapolated_error}

if __name__ == '__main__':
	
	i = 4
	h = 1e-10
	
	test1 = forward_difference(i, h)
	test2 = central_difference(i, h)
	test3 = extrapolated_difference(i, h)
	Actual_value = 3 * 4**2
	
	print "The actual value is %f." % Actual_value
	print "The value of the forward difference is %.8f and its error is %e."
	 % (test1['value'], test1['error'])
	print "The value of the central difference is %.8f and its error " \
								"is %e." % (test2['value'], test2['error'])
	print "The value of the extrapolated difference is %.8f and its error " \
								"is %e." % (test3['value'], test3['error'])			

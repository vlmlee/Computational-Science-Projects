"""
Written by Michael Lee.

PHYS440: Computational Physics
Project 2, Differentiation, Integration, and Root Finding

"""
import numpy as np

def f(x):
	# Our test function
	return x*x - x

def newton(x, dx, imax, eps):
	for i in range(0, imax + 1):
		A = f(x)
		if (abs(A) <= eps):
			# Ends program if f(x) < eps
			print "Root found, tolerance eps = ", eps
			break
		print "Iteration # = ", i, ", x = ", x, ", f(x) =", A
		"""
		The next series of calulations finds the
		new value x to recalculate f(x).
		"""
		df = (f(x+dx/2) - f(x-dx/2)) / dx
		dx = -A/df
		x += dx
	return x

if __name__ == '__main__':

	test = newton(3, 1e-3, 100, 1e-6)
	print "The root(s) are: %f" % test
"""
Written by Michael Lee.
Based on "LaplaceFD.py" from "A SURVEY OF COMPUTATIONAL PHYSICS" by 
RH Landau, MJ Paez, and CC Bordeianu.

PHYS440: Computational Physics
Project 5, Square Conductors and One Dimensional Electrostatics

"""

from numpy import *
import matplotlib.pylab as plt;
from mpl_toolkits.mplot3d import Axes3D

def functz(V):
    z = V[X,Y]
    return z

def voltage(xvolt1, xvolt2, yvolt1, yvolt2, x_edge1, x_edge2, y_edge1, y_edge2):
    for j in range(y_edge1, y_edge2+1):
        V[x_edge1, j] = xvolt1
        V[x_edge2, j] = xvolt2
    for i in range(x_edge1, x_edge2+1):
        V[i, y_edge1] = yvolt1
        V[i, y_edge2] = yvolt2
    return V[i,j]

def finite_difference(V, x_edge1, x_edge2, y_edge1, y_edge2, max_range):
    for iter in range(Niter):
        if iter%10 == 0: print(iter)

        for i in range(x_edge1):
            for j in range(1, max_range+1):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

        for i in range(x_edge2+1, max_range):
            for j in range(1, max_range+1):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

        for j in range(y_edge1):
            for i in range(x_edge1, x_edge2+1):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

        for j in range(y_edge2+1, max_range):
            for i in range(x_edge1, x_edge2+1):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

        """
        The finite difference method takes points on the graph and calculates
        its potential, V[i,j], based on the potentials of its four nearest neighbors.
        If its neighbors have V[i,j] = 0, then it is also zero. Since we seeded the
        graph with lines of V = 100, we will get points of decreasing potential near those
        lines, since we take the average of the four values. We iterate the calculation of
        each point's potential for 'Niter' times, with the values V[i,j] still on the stack.

        The code below is probably more efficient since it contains one less
        nested for-loop. However, because the above uses the same loop pattern
        for X and Y, I think the above is easier to understand.

        """

        # for i in range(x_edge1, x_edge2):
        #     for j in range(1, y_edge1):
        #         V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
        #     for j in range(y_edge2+1, 90):
        #         V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

    return V[i,j]

if __name__ == '__main__':

  print("Initializing")
  Nmax = 100; Niter = 70; V = zeros((Nmax+1, Nmax+1), float)
  max_range = 90 # Required: max_range < Nmax

  print("Working hard, wait for the figure while I count to 60")

  voltage(100, 100, 100, 100, 30, 60, 30, 60)
  finite_difference(V, 30, 60, 30, 60, max_range)

  x = range(0, max_range, 2);  y = range(0, max_range, 2)
  X, Y = plt.meshgrid(x,y)

  Z = functz(V)

  fig = plt.figure()
  ax = Axes3D(fig)
  ax.plot_wireframe(X, Y, Z, color='r')
  ax.contour(X, Y, Z, offset=0)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Potential')

  plt.show()

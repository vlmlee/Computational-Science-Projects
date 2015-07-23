"""
Written by Michael Lee.

PHYS440: Computational Physics
Project 5, Square Conductors and One Dimensional Electrostatics

"""

from numpy import *
import matplotlib.pylab as plt;
from mpl_toolkits.mplot3d import Axes3D

def functz(V):
    z = V[X,Y]
    return z

def voltage(volt, x_edge1, x_edge2, y_edge1, y_edge2):
    for j in range(y_edge1, y_edge2+1):
        V[x_edge1, j] = volt
        V[x_edge2, j] = volt
    for i in range(x_edge1, x_edge2+1):
        V[i, y_edge1] = volt
        V[i, y_edge2] = volt
    return V[i,j]

def finite_difference(V, x_edge1, x_edge2, y_edge1, y_edge2):
    for iter in range(Niter):
        if iter%10 == 0: print(iter)

        for i in range(x_edge1):
            for j in range(1, 91):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

        for i in range(x_edge2+1, 90):
            for j in range(1, 91):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

        for j in range(y_edge1):
            for i in range(x_edge1, x_edge2+1):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

        for j in range(y_edge2+1, 90):
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
        nested for-loop. However, because the above uses the same pattern
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

  print("Working hard, wait for the figure while I count to 60")

  voltage(100, 30, 60, 30, 60)
  finite_difference(V, 30, 60, 30, 60)

  x = range(0, 90, 2);  y = range(0, 90, 2)
  X, Y = p.meshgrid(x,y)

  Z = functz(V)

  fig = plt.figure()
  ax = Axes3D(fig)
  ax.plot_wireframe(X, Y, Z, color='r')
  ax.contour(X, Y, Z, offset=0)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Potential')

  p.show()

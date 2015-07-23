"""
Written by Michael Lee.
Adapted from Random Walk simulation by matplotlib.

PHYS440: Computational Physics
Project 1, Random Walk
"""

import numpy as np
import matplotlib
matplotlib.use('TKAgg') # For OSX users
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

def randomwalk(length, dims=3):
    linedata = np.empty((dims, length))
    linedata[:,0] = np.random.rand(dims)
    for index in range(1, length):
        step = (np.random.rand(dims) - 0.5)*.5
        linedata[:, index] = linedata[:, index-1] + step
    return linedata

def animate(num, datalines, lines):
    for line, data in zip(lines, datalines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

# Index accounts for the number of random walk simulations in one trial
def walk_range(data, index, dims=3):
    xyzranges = []
    for i in range(index):
        for j in range(0, dims):
            max_range = max(data[i][j])
            min_range = min(data[i][j])
            xyzranges.append((min_range, max_range))
    return xyzranges

# RMS is the _average_ distance from the origin of all the
# steps. The actual scalar distance from the origin is calculated
# and given in the array R.
def distance_from_origin_and_rms(data, steps, index, dims=3):
    sum = 0
    rms_sum = 0
    rms = []
    RMS = []
    r = []
    R = []
    for i in range(index):
        for j in range(dims):
            for k in range(steps-1):
                sum = sum + (data[i][j][k+1] - data[i][j][k])
                rms_sum = rms_sum + (data[i][j][k+1] - data[i][j][k])**2
            r.append(sum)
            rms.append(rms_sum)
            sum = 0
            rms_sum = 0
    for l in range(len(r)/3):
        xyz = r[3*l]**2 + r[3*l+1]**2 + r[3*l+2]**2
        R.append(xyz)
        xyz_rms = np.sqrt(rms[3*l] + rms[3*l+1]+ rms[3*l+2]) / np.sqrt(steps)
        RMS.append(xyz_rms)
    return map(np.sqrt, R), RMS

if __name__ == '__main__':

    fig = plt.figure()
    ax = p3.Axes3D(fig, xlim=(-10,10), ylim = (-10, 10), zlim = (-10,10))
    ax.set_xlabel('X'), ax.set_ylabel('Y'), ax.set_zlabel('Z')
    ax.set_title('Random Walk in 3 Dimensions')

    steps = 1000
    number_of_walks = 1
    data = [randomwalk(steps) for index in range(number_of_walks)]
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
    rang = walk_range(data, number_of_walks)
    distance = distance_from_origin_and_rms(data, steps, number_of_walks)

    for i in range(number_of_walks):
        print "Ranges for plot %d : X = %f to %f; Y = %f to %f; Z = %f to %f" %\
            (i+1, rang[3*i][0], rang[3*i][1], rang[(3*i)+1][0], rang[(3*i)+1][1], 
            rang[(3*i)+2][0], rang[(3*i)+2][1])

    for i in range(number_of_walks):
        print "The scalar distance from the origin for plot %d is: %f" %\
            (i+1, distance[0][i])

        print "The RMS (Quadratic mean) for plot %d is: %f" %\
            (i+1, distance[1][i])

    ani = animation.FuncAnimation(fig, animate, steps, fargs=(data, lines),
        interval=100, repeat=False)

    plt.show()
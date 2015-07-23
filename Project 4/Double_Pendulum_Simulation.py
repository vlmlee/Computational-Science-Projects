"""
Written by Michael Lee.
Adapted from Double Pendulum simulation by matplotlib.

"Double pendulum formula translated from the C code at
http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c"

PHYS440: Computational physics
Project 4, Double Pendulum

"""

import matplotlib
matplotlib.use('TkAgg')
from numpy import sin, cos, pi, array
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.8 # Acceleration due to gravity, in m/s^2

def double_pendulum(state, t, L1, L2, M1, M2):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]
    del_ = state[2]-state[0]
    den1 = (M1+M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_)
               + M2*G*sin(state[2])*cos(del_) + M2*L2*state[3]*state[3]*sin(del_)
               - (M1+M2)*G*sin(state[0]))/den1
    dydx[2] = state[3]
    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_)
               + (M1+M2)*G*sin(state[0])*cos(del_)
               - (M1+M2)*L1*state[1]*state[1]*sin(del_)
               - (M1+M2)*G*sin(state[2]))/den2
    return dydx

def parameters(theta1, theta2, ang_v1, ang_v2, L1, L2, M1, M2):
    return {'angle1': theta1, 'angle2': theta2, 'velocity1': ang_v1, 'velocity2': ang_v2,
            'L1': L1, 'L2': L2, 'M1': M1, 'M2': M2}

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template%(i*dt))
    return line, time_text

if __name__ == '__main__':

  """
  Parameters: angle of top pendulum, angle of bottom pendulum, angular velocity of
  top pendulum, angular velocity of bottom pendulum, length of string on top pendulum,
  length of string on bottom pendulum, mass of top pendulum, and mass of bottom
  pendulum.

  Change parameters for different situations. Use float or better precision for better
  results.
  """

  initial_parameters = parameters(30., 20., 0., 0., 1, 2, 1, 3)
  state = np.array([initial_parameters['angle1'], initial_parameters['velocity1'],
          initial_parameters['angle2'], initial_parameters['velocity2']])*pi/180.

  dt = 0.05
  t = np.arange(0.0, 20, dt)

  y = integrate.odeint(double_pendulum, state, t, (initial_parameters['L1'],
          initial_parameters['L2'], initial_parameters['M1'], initial_parameters['M2']))

  x1 = initial_parameters['L1']*sin(y[:,0])
  y1 = -initial_parameters['L1']*cos(y[:,0])

  x2 = initial_parameters['L2']*sin(y[:,2]) + x1
  y2 = -initial_parameters['L2']*cos(y[:,2]) + y1

  fig = plt.figure()
  ax = fig.add_subplot(111, autoscale_on=False, xlim=(-4, 4), ylim=(-4, 1))
  ax.grid()
  plt.title('Double Pendulum; L1=%s, L2=%s, M1=%s, M2=%s,\n Ang Velocity Top=%s, Ang Velocity Bot=%s,' \
        'Angle1=%s, Angle2=-%s' % (initial_parameters['L1'], initial_parameters['L2'], initial_parameters['M1'], \
        initial_parameters['M2'], initial_parameters['velocity1'], initial_parameters['velocity2'], \
        initial_parameters['angle1'], initial_parameters['angle2']))
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.plot(x2, y2)
  line, = ax.plot([], [], 'o-', lw=2)

  time_template = 'time = %.1fs'
  time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

  ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
      interval=25, blit=True, init_func=init)

  plt.show()

"""
Written by Michael Lee.

PHYS440: Computational Physics
Project 3, Fast Fourier Transform, Curve Fitting, and Ordinary Differential Equations

"""

import numpy as np
import math
import matplotlib.pyplot as plt

time, amplitude = np.loadtxt("signal3.dat", unpack=True)
N = len(time)
signal_fit = np.sin(440*2*np.pi*time)*.25142

plt.plot(time, amplitude, 'r', label="Noisy Signal")
plt.plot(time, signal_fit, 'b', label="Original SIgnal")

plt.title('Noisy Signal with Original Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

plt.show()
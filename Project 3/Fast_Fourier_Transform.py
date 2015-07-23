"""
Written by Michael Lee

PHYS440: Computational Physics
Project 3, Fast Fourier Transform, Curve Fitting, and Ordinary Differential Equations

"""

import numpy as np
import scipy
import scipy.fftpack
import matplotlib.pyplot as plt
import matplotlib.figure

time, amplitude = np.loadtxt("signal3.dat", unpack=True)
N = len(time)

normalized_time = np.linspace(0.0,1.0,N)
fast_fourier_transform_of_amplitude = scipy.fft(amplitude)
freq = scipy.fftpack.fftfreq(amplitude.size, normalized_time[1]-normalized_time[0])

plt.subplot(211)
plt.subplots_adjust(hspace=.3)
plt.plot(time2, amplitude, 'b')
plt.title("signal3.dat")
plt.xlabel("Time (seconds) ")
plt.ylabel("Amplitude")

plt.subplot(212)
plt.title("FFT of signal3.dat")
plt.ylabel("Number of Samples")
plt.xlabel("Frequency (Hz)")
plt.plot(freq, abs((fast_fourier_transform_of_amplitude)), 'r')

plt.show()
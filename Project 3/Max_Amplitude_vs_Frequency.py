"""
Written by Michael Lee

PHYS440: Computational Physics
Project 3, Fast Fourier Transform, Curve Fitting, and Ordinary Differential Equations
"""

from pylab import *
import numpy as np
import matplotlib.pyplot as plt

omega = .44*2*np.pi
time = np.arange(0, 40, .1)

def max_amplitude_of_beat_frequency(signal1, signal2):
	beat_function = signal1 + signal2
	max_amp = max(beat_function)
	return max_amp

if __name__ == '__main__':

	list_of_max_amps = []
	frequency_range = np.arange(.044, 4.4, .0044)

	function_1 = -omega**2*sin(omega*time)

	for i in frequency_range:
		function_2 = 7.6*sin(i*2*np.pi*time)
		list_of_max_amps.append(max_amplitude_of_beat_frequency(function_1, function_2))

	plt.plot(frequency_range, list_of_max_amps, 'r')
	plt.title("Maximum Amplitude vs Frequency (KHz)")
	plt.xlabel("Frequency (KHz)")
	plt.ylabel("Amplitude")
	plt.show()

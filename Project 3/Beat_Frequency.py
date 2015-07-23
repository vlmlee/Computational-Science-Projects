"""
Written by Michael Lee.

PHYS440: Computational Physics
Project 3, Fast Fourier Transform, Curve Fitting, and Ordinary Differential Equations

"""

import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0,40,.1)
omega = .44*2*np.pi
signal1 = -omega**2*np.sin(omega*time)
signal2 = 7.6*np.sin(.5*2*np.pi*time)
beat_frequency = signal1 + signal2
sixty_hertz_signal = 15.2*np.sin(.06*2*np.pi*time)
envelope = 15.2*np.sin(.06*np.pi*time)

plt.subplot(211)
plt.subplots_adjust(hspace=.3)
plt.plot(time, signal1, 'r', label=".44KHz")
plt.plot(time, signal2, 'b', label=".50KHz")
plt.legend()
plt.title("Signal of f=.44KHz and f=.50KHz")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.subplot(212)
plt.plot(time, beat_frequency, 'r', label="Beat Freq.")
plt.plot(time, sixty_hertz_signal, 'b', label=".06KHz")
plt.plot(time, envelope, 'g', label="Envelope")
plt.legend()
plt.title("Beat Frequency")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.show()
import numpy as np


def generate_sine(freq, sample_rate, duration):
    t = np.arange(0, duration, 1 / sample_rate)
    return t, np.sin(2 * np.pi * freq * t)

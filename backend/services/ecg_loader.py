import numpy as np

def load_ecg():
    t = np.linspace(0, 10, 1000)

    signal = np.sin(2 * np.pi * 1.5 * t)

    return signal
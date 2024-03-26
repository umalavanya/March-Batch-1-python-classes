import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, omega, y0, v0):
        self.omega = omega  # Angular frequency
        self.y0 = y0        # Initial position
        self.v0 = v0        # Initial velocity

    def solve(self, t):
        """
        Solves the harmonic oscillator equation and returns the position and velocity at given time points.
        """
        A = self.y0
        B = self.v0 / self.omega
        y = A * np.cos(self.omega * t) + B * np.sin(self.omega * t)
        v = -A * self.omega * np.sin(self.omega * t) + B * self.omega * np.cos(self.omega * t)
        return y, v

# Parameters
omega = 2*np.pi  # Angular frequency (1 Hz)
y0 = 1.0         # Initial position
v0 = 0.0         # Initial velocity

# Time array
t = np.linspace(0, 10, 1000)

# Create HarmonicOscillator object
oscillator = HarmonicOscillator(omega, y0, v0)

# Solve the harmonic oscillator equation
y, v = oscillator.solve(t)

# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='Position (y)')
plt.plot(t, v, label='Velocity (v)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Harmonic Oscillator')
plt.legend()
plt.grid(True)
plt.show()

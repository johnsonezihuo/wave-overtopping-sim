import numpy as np
import matplotlib.pyplot as plt

# parameters
A = [0.3, 0.2, 0.15, 0.1]   # amplitudes(m)
f = [0.2, 0.4, 0.6, 0.8]  # frequencies(Hz)
phi = np.random.rand(len(A)) * 2 * np.pi  # random phase angeles
omega = 2 * np.pi * np.array(f)  # angular frequencies

# time vector
t = np.linspace(0, 100, 1000)  # 100 seconds, 1000 samples

# superimpose multiple sine waves to create irregular wave
eta = np.zeros_like(t)
for i in range(len(A)):
    eta += A[i] * np.sin(omega[i] * t + phi[i])

#statistics
max_height = np.max(eta) - np.min(eta)
std_dev = np.std(eta)
Hs = 4 * std_dev # approximation using rayleigh distribution

print(f"max height of the wave: {max_height:.2f} m")
print(f"significant wave height (Hs): {Hs:.2f} m")

# plot time series
plt.figure(figsize=(10, 5))
plt.plot(t, eta, label='irregular wave')
plt.title('Simulated Irregular Wave (time domain)')
plt.xlabel('Time (s)')
plt.ylabel('Surface Elevation (m)')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()




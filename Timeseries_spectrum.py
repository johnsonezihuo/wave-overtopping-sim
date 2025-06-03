import numpy as np
import matplotlib.pyplot as plt

#constants
g = 9.81  # acceleration due to gravity (m/s^2)
alpha = 0.0081  # philip constant parameter
gamma = 3.3  # peak enhancement factor
fp = 0.33 # peak frequency (Hz)

# frequency range
f = np.linspace(0.05, 1.0, 500) # frequency range (Hz)
df = f[1] - f[0]  # frequency step

# sigma definition
sigma = np.where(f <= fp, 0.07, 0.09)

# JONSWAP spectrum parameters
def jonswap(f, alpha, gamma, fp, sigma):
    r = np.exp(- ((f - fp)**2) / (2 * sigma**2 * fp**2))
    S = (alpha * g**2 * (2 * np.pi)**(-4) *
         f**(-5) * np.exp(-1.25 * (fp / f)**4) * gamma**r)
    return S
S = jonswap(f, alpha, gamma, fp, sigma)

#time domain
T_total = 200  # total simulation time in seconds
dt = 0.1  # time step in seconds
t = np.arange(0, T_total, dt)

# Generate random phases
phi = np.random.uniform(0, 2*np.pi, len(f))

#wave elevation synthesis
eta = np.zeros_like(t)
for i in range(len(f)):
    Ai = np.sqrt(2 * S[i] * df)  # amplitude from spectral density
    eta += Ai * np.cos(2 * np.pi * f[i] * t + phi[i])

#method 1-statistical summary
H_max = np.max(eta) - np.min(eta)  # maximum wave height
H_s_std = 4 * np.std(eta) # standard deviation
print(f"Maximum wave height: {H_max:.2f} m")
print(f"Significant wave height (H_s ~ 4_std): {H_s_std:.2f} m")

# method 2-zero upcrossing wave height estimation
zero_crossings = np.where(np.diff(np.signbit(eta)))[0]  # find zero crossings
wave_heights = []
for i in range(0, len(zero_crossings) - 1, 2):# every wave between crossings
    segment = eta[zero_crossings[i]:zero_crossings[i+1]]
    if len(segment) > 0:
        wave_heights.append(np.max(segment) - np.min(segment))

wave_heights = np.array(wave_heights)
H_s_13 = np.mean(np.sort(wave_heights)[-len(wave_heights)//3:])  # H_s as average of highest 1/3 of waves

print(f"Significant wave height (H_s 1/3): {H_s_13:.2f} m")
print(f"Total number of waves: {len(wave_heights)}")


# Plotting the time series of wave elevation
plt.figure(figsize=(12, 4))
plt.plot(t, eta, color='teal')
plt.title("Simulated Irregular Wave Time Series")
plt.xlabel("Time (s)")
plt.ylabel("Surface Elevation η(t) [m]")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Plot histogram of wave heights ===
plt.figure(figsize=(8, 4))
plt.hist(wave_heights, bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Individual Wave Heights")
plt.xlabel("Wave Height (m)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
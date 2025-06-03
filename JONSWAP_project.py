import numpy as np
import matplotlib.pyplot as plt

# constants
g = 9.81  # acceleration due to gravity (m/s^2)
alpha = 0.0081  # philip constant parameter
gamma = 3.3  # peak enhancement factor
fp = 0.33 # peak frequency (Hz)

# freguency range
f = np.linspace(0.05, 1.0, 500) # frequency range (Hz)

#sigma varies with frequency
sigma = np.where(f <= fp, 0.07, 0.09) # spectral width parameter

# JONSWAP spectrum parameters
def jonswap_spectrum(f,alpha,gamma,fp,sigma):
    r = np.exp(-(f-fp)**2 / (2 * sigma**2 * fp**2))
    Sf = (alpha * g**2 *(2 * np.pi)**(-4) * f**(-5) * np.exp(-1.25 * (fp/f)**4) * gamma**r) 
    return Sf
S = jonswap_spectrum(f, alpha, gamma, fp, sigma)

# Plotting the JONSWAP spectrum
plt.figure(figsize=(10, 5))
plt.plot(f, S, label='JONSWAP Spectrum', color='blue')
plt.title('JONSWAP Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectral Density (Sf) (m^2/Hz)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

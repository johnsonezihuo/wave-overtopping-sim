## wave-overtopping-sim
Simulation and Analysis of Irregular Wave Trains Based on JONSWAP Spectrum for Coastal Overtopping Risk
## Objective
This project simulates realistic irregular ocean waves based on the JONSWAP energy spectrum, and extracts key parameters relevant to coastal wave overtopping design. The goal is to understand how spectral characteristics (e.g., peak frequency, peakedness) affect surface elevation and wave height statistics, which are crucial in estimating overtopping rates for coastal defense structures.

## Technical Approach
Implemented the JONSWAP wave spectrum formula to model sea state energy distribution

Applied inverse Fourier synthesis to generate irregular surface elevation time series

Extracted wave parameters:

Significant Wave Height (Hs)

Max Wave Height

Zero-upcrossing wave count

Histogram of wave heights

Tools used: Python, NumPy, Matplotlib, SciPy

## Sample Output
JONSWAP energy spectrum plot

Simulated wave time series

Wave height distribution histogram

Estimated Hs using standard deviation and statistical 1/3 methods

## Relevance to PhD: "Wind Forcing on Overtopping"
Overtopping predictions rely heavily on Hs and wave period. This project simulates wave fields that resemble real storm sea states, and can be extended to explore how wind forcing would modify wave shapes and increase overtopping rates — a core goal of the proposed PhD project at Imperial.

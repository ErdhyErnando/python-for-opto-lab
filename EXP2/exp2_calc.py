import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Load CSV
data = pd.read_csv('your_data.csv')

# Define solar cell model
def solar_cell_model(V, I_s, n, R_s, R_p):
    q = 1.602e-19  # Elementary charge
    k = 1.381e-23  # Boltzmann constant
    T = 293  # Example: 20°C in Kelvin
    return I_s * (np.exp(q * (V + R_s) / (n * k * T)) - 1) + (V + R_s) / R_p

# Fit data
V = data['Voltage']
I = data['Current']
initial_guess = [1e-10, 1.5, 0.01, 1000]  # Adjust initial guesses
params, _ = curve_fit(solar_cell_model, V, I, p0=initial_guess)

I_s, n, R_s, R_p = params
print(f"I_s: {I_s}, n: {n}, R_s: {R_s}, R_p: {R_p}")

# Plot
plt.plot(V, I, 'o', label='Data')
plt.plot(V, solar_cell_model(V, *params), label='Fit')
plt.legend()
plt.show()

# Calculate W_g
temperatures = np.array([18, 20, 22]) + 273  # Temperatures in Kelvin
I_s_values = []  # List of I_s at different temperatures
# Populate I_s_values by repeating the above fitting for each temperature
T_inv = 1 / temperatures
ln_Is_T3 = np.log(np.array(I_s_values) / temperatures**3)
coeffs = np.polyfit(T_inv, ln_Is_T3, 1)
W_g = -coeffs[0] * k
print(f"W_g: {W_g} eV")

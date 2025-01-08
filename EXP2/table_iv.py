import numpy as np
import pandas as pd

# Load the I-V data (replace with your file)
data = pd.read_csv('/table_4_data/18100.csv', delim_whitespace=True)  # Ensure the file contains 'Voltage' and 'Current' columns
voltage = data['VOLT1'].to_numpy()
current = data['CURR1'].to_numpy()

# Calculate Power
power = voltage * current

# Find Maximum Power Point (MPP)
idx_mpp = np.argmax(power)  # Index of max power
U_MPP = voltage[idx_mpp]    # Voltage at MPP
I_MPP = current[idx_mpp]    # Current at MPP
P_MPP = power[idx_mpp]      # Max power

# Find Short-Circuit Current (I_SC) and Open-Circuit Voltage (U_OC)
I_SC = current[np.argmax(voltage == 0)]  # Current where voltage is zero
U_OC = voltage[np.argmax(current == 0)]  # Voltage where current is zero

# Calculate Fill Factor (FF)
FF = P_MPP / (I_SC * U_OC)

# Assume input power (P_in) and cell area (A)
P_in = 1000  # Example: Light intensity in W/m²
A = 0.01     # Example: Cell area in m²
efficiency = P_MPP / (P_in * A)

# Print results
print(f"I_MPP: {I_MPP:.4f} A")
print(f"U_MPP: {U_MPP:.4f} V")
print(f"P_MPP: {P_MPP:.4f} W")
print(f"FF: {FF:.4f}")
print(f"Efficiency (η): {efficiency * 100:.2f} %")

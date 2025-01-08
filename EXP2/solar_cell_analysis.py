import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.constants import k, e
import warnings
warnings.filterwarnings('ignore')

# Constants
T = 300  # Temperature in Kelvin
kT = k * T
VT = kT / e  # Thermal voltage

def solar_cell_equation(V, Is, Rs, Rp):
    """Solar cell equation for dark conditions"""
    return Is * (np.exp((V + Rs * Is) / VT) - 1) + (V + Rs * Is) / Rp

def extract_parameters(voltage, current):
    """Extract solar cell parameters using curve fitting"""
    
    # Initial parameter guesses
    Is_guess = 1e-9  # Initial guess for saturation current
    Rs_guess = 1.0   # Initial guess for series resistance
    Rp_guess = 1000  # Initial guess for parallel resistance
    
    # Perform curve fitting
    try:
        popt, _ = curve_fit(solar_cell_equation, voltage, current, 
                           p0=[Is_guess, Rs_guess, Rp_guess],
                           bounds=([0, 0, 0], [1e-6, 100, 1e6]))
        Is, Rs, Rp = popt
        
        # Calculate bandgap energy (Wg)
        # For silicon at room temperature, typically around 1.1-1.2 eV
        # Using the relationship Is ∝ exp(-Wg/2kT)
        Wg = -2 * kT * np.log(Is / 1e-3)  # Approximate calculation
        
        return Is, Rs, Rp, Wg
        
    except RuntimeError:
        return None, None, None, None

def analyze_solar_cell(csv_file):
    """Analyze solar cell parameters from CSV data"""
    
    # Load data
    data = pd.read_csv(csv_file)
    voltage = data['VOLT1'].values
    current = data['CURR1'].values
    
    # Extract parameters
    Is, Rs, Rp, Wg = extract_parameters(voltage, current)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(voltage, current * 1000, 'bo-', label='Measured Data')
    
    if Is is not None:
        # Plot fitted curve
        V_fit = np.linspace(min(voltage), max(voltage), 1000)
        I_fit = solar_cell_equation(V_fit, Is, Rs, Rp)
        plt.plot(V_fit, I_fit * 1000, 'r-', label='Fitted Curve')
        
        print(f"\nExtracted Parameters:")
        print(f"Saturation Current (Is): {Is:.2e} A")
        print(f"Series Resistance (Rs): {Rs:.2f} Ω")
        print(f"Parallel Resistance (Rp): {Rp:.2f} Ω")
        print(f"Bandgap Energy (Wg): {Wg:.2f} eV")
    else:
        print("Failed to extract parameters. Try adjusting initial guesses or bounds.")
    
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (mA)')
    plt.title('Solar Cell I-V Characteristics (Dark)')
    plt.grid(True)
    plt.legend()
    plt.savefig('iv_curve_fit.png')
    plt.close()

if __name__ == "__main__":
    csv_file = "Dark18_2.csv"
    analyze_solar_cell(csv_file)

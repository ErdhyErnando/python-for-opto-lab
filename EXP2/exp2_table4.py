# Solar Cell Parameters Calculator

def calculate_solar_parameters(Isc, Voc, P_in, IMPP, UMPP):
    """
    Calculate solar cell parameters based on Isc, Voc, IMPP, and UMPP.

    Parameters:
    Isc : float : Short-circuit current in Amperes
    Voc : float : Open-circuit voltage in Volts
    P_in : float : Incident power in Watts per square meter (W/m²)
    IMPP : float : Maximum power point current in Amperes
    UMPP : float : Maximum power point voltage in Volts

    Returns:
    dict : Calculated parameters including PMAX, FF, and efficiency
    """

    # Calculate maximum power
    PMAX = IMPP * UMPP

    # Calculate fill factor (FF)
    FF = PMAX / (Voc * Isc)

    # Calculate efficiency
    efficiency = (PMAX / P_in) * 100  # Efficiency in percentage

    return {
        'Isc': Isc,
        'Voc': Voc,
        'IMPP': IMPP,
        'UMPP': UMPP,
        'PMAX': PMAX,
        'FF': FF,
        'Efficiency (%)': efficiency
    }

# Input parameters
Isc = float(input("Enter the short-circuit current (Isc) in Amperes: "))
Voc = float(input("Enter the open-circuit voltage (Voc) in Volts: "))
# P_in = float(input("Enter the incident power (P_in) in Watts per square meter: "))
# IMPP = float(input("Enter the maximum power point current (IMPP) in Amperes: "))
# UMPP = float(input("Enter the maximum power point voltage (UMPP) in Volts: "))

# Calculate parameters
results = calculate_solar_parameters(Isc, Voc, P_in, IMPP, UMPP)

# Display results
print("\nCalculated Solar Cell Parameters:")
for key, value in results.items():
    print(f"{key}: {value:.4f}")
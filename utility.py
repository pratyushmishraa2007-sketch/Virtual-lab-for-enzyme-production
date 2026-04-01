import numpy as np

def enzyme_yield(temp, ph, substrate, time):
    """
    Simulate enzyme production yield based on conditions.
    """

    # Optimal conditions
    optimal_temp = 37
    optimal_ph = 7

    # Gaussian-like response
    temp_factor = np.exp(-((temp - optimal_temp) ** 2) / 50)
    ph_factor = np.exp(-((ph - optimal_ph) ** 2) / 2)

    yield_value = substrate * temp_factor * ph_factor * (1 - np.exp(-time / 10))

    return round(yield_value, 2)
import numpy as np
import matplotlib.pyplot as plt

R = 8.314
a = 0.1382
b = 3.19*10**(-5)
def van_der_waals(V, T):
    return (R * T) / (V - b) - a / (V**2)
T = -130 + 273.15
V_min = b + 1e-5
V_max = 1e-3
area, error = spi.quad(van_der_waals, V_min, V_max, args=(T,))
print(f'Площадь под графиком P-V при T = -130 °C: {area:.4f} (с ошибкой {error:.4e})')

import numpy as np
import matplotlib.pyplot as plt

R = 8.314
a = 0.1382
b = 3.19*10**(-5)

def van_der_waals(T, V):
    return (R * T) / (V - b) - a / (V**2)

V = np.linspace(b + 10**(-5), 10**(-3), 1000)
temperatures = [-140 + 273.15, -130 + 273.15, -120 + 273.15, -110 + 273.15, -100 + 273.15]
plt.figure(figsize=(10, 6))

for i in temperatures:
    P = van_der_waals(i, V)
    plt.plot(V, P, label=f'T = {i - 273.15:.1f} °C')

P_high_temp = van_der_waals(-100 + 273.15, V)
plt.plot(V, P_high_temp, 'r-', linewidth=2, label='T = -100 °C')

plt.title('Графики уравнения Ван-дер-Ваальса')
plt.xlabel('Объем')
plt.ylabel('Давление')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

plt.legend()
plt.grid()

plt.show()
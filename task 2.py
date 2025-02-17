import numpy as np
import matplotlib.pyplot as plt

R = 8.314
a = 0.1382
b = 3.19 * 10**(-5)
def van_der_waals(V, T):
    return (R * T) / (V - b) - a / (V**2)
T = -130 + 273.15
def find_local_minimum(start, learning_rate=1e-6, tol=1e-6, max_iter=1000):
    V = start
    for _ in range(max_iter):
        gradient = (van_der_waals(V + tol, T) - van_der_waals(V, T)) / tol
        V -= learning_rate * gradient
        if V <= b:
            return None
    return V
def find_local_maximum(start, learning_rate=1e-6, tol=1e-6, max_iter=1000):
    V = start
    for _ in range(max_iter):
        gradient = (van_der_waals(V + tol, T) - van_der_waals(V, T)) / tol
        V += learning_rate * gradient
        if V <= b:
            return None
    return V
start_min = b + 1e-5
start_max = b + 1e-5
V_min = find_local_minimum(start_min)
V_max = find_local_maximum(start_max)

P_min = van_der_waals(V_min, T) if V_min is not None else None
P_max = van_der_waals(V_max, T) if V_max is not None else None
print(f'Локальный минимум: V = {V_min:.4e}, P = {P_min:.4f}')
print(f'Локальный максимум: V = {V_max:.4e}, P = {P_max:.4f}' if V_max is not None else 'Максимум не найден')
V_range = np.linspace(b + 1e-5, 1e-3, 1000)
P = van_der_waals(V_range, T)
dP_dV = np.gradient(P, V_range)
plt.figure(figsize=(10, 6))
plt.plot(V_range, P, label='Изотерма (-130 °C)', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
if P_min is not None:
    plt.scatter([V_min], [P_min], color='red', zorder=5, label='Локальный минимум')
if P_max is not None:
    plt.scatter([V_max], [P_max], color='green', zorder=5, label='Локальный максимум')
for i in range(len(dP_dV) - 1):
    if dP_dV[i] > 0 and dP_dV[i + 1] <= 0:
        plt.fill_between(V_range[i:i + 2], P[i:i + 2], color='blue', alpha=0.5, label='Запрещенная зона')
plt.title('График изотермы Ван-дер-Ваальса при -130 °C')
plt.xlabel('Объем')
plt.ylabel('Давление')
plt.ylim(min(P) - 0.5, max(P) + 0.5)
plt.xlim((b + 10**(-5), 10**(-3)))
plt.legend()
plt.grid()
plt.show()
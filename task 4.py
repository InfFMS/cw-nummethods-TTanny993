import numpy as np
import matplotlib.pyplot as plt

P_130 = 3664186.998
R = 8.314
a = 0.1382
b = 3.19*10**(-5)

def van_der_waals(V, T):
    return (R * T) / (V - b) - a / (V**2)

def equation(V, T):
    return van_der_waals(V, T) - P_130

def bisection_method(func, a, b, T, tol=1e-6, max_iter=1000):
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(func(c, T)) < tol:
            return c
        elif func(a, T) * func(c, T) < 0:
            b = c
        else:
            a = c
    return c

T = -130 + 273.15
V_initial_guesses = [-5, 1]

roots = []
for i in range(len(V_initial_guesses) - 1):
    root = bisection_method(equation, V_initial_guesses[i], V_initial_guesses[i + 1], T)
    roots.append(root)

roots.sort()

V_values = np.linspace(b + 10**(-5), 10**(-3), 1000)
P_values = van_der_waals(V_values, T)

plt.figure(figsize=(10, 6))
plt.plot(V_values, P_values, label='P(V)', color='blue')
plt.axhline(y=P_130, color='red', linestyle='--', label='P_130 = {:.2f} Па'.format(P_130))
plt.scatter(roots, van_der_waals(np.array(roots), T), color='green', zorder=5, label='Корни (Vl, V_center, Vg)')
plt.title('График зависимости давления от объема')
plt.xlabel('Объем (м³)')
plt.ylabel('Давление (Па)')
plt.legend()
plt.grid()
plt.show()
# Libraries
import matplotlib.pyplot as plt 
import numpy as np

# Initialization and Declaration
m, w, hbar, n = 1, 1, 1, 10
psi_list, psi_2_list = [], []
x_list = np.linspace(-10, 10, 1000)

# Calculation
def hermite(x, n):
    herm_coeffs = np.zeros(n + 1)
    herm_coeffs[n] = 1
    return np.polynomial.hermite.hermval(np.sqrt(m * w / hbar) * x, herm_coeffs)
def psi(x, n, m, w):
    factor = (m * w / (np.pi * hbar)) ** .25 * (2 ** n * np.math.factorial(n)) ** -.5
    exponent = np.exp(-.5 * (np.sqrt(m * w / hbar) * x) ** 2)
    return factor * exponent * hermite(x,n)
def psi_2(x, n, m, w):
    return np.square(psi(x, n, m, w))
for x in x_list:
    psi_list.append(psi(x, n, m, w))
    psi_2_list.append(psi_2(x, n, m, w))

# Visualization
plt.suptitle(f'Wave Functions n = {n}')
plt.subplot(2, 1, 1)
plt.plot(x_list, psi_list, '#05BAB6')
plt.ylabel("Ψ")
plt.subplot(2, 1, 2)
plt.plot(x_list, psi_2_list, '#6FA4FF')
plt.xlabel("x")
plt.ylabel("Ψ²")
plt.show()
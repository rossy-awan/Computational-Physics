# Libraries
import matplotlib.pyplot as plt
import numpy as np

# Initialization and Declaration
L, n = 1, 2
h, m = 6.626e-34, 9.11e-31
psi_list, psi_2_list = [], []
x_list = np.linspace(0,1,1000)

# Calculation
def psi(n, L, x):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
def psi_2(n, L, x):
    return np.square(psi(n, L, x))
for x in x_list:
    psi_list.append(psi(n, L, x))
    psi_2_list.append(psi_2(n, L, x))

# Visualization
plt.suptitle(f'Wave Functions n = {n}')
plt.subplot(2, 1, 1)
plt.plot(x_list, psi_list, '#05BAB6')
plt.ylabel("Ψ")
plt.subplot(2, 1, 2)
plt.plot(x_list, psi_2_list, '#6FA4FF')
plt.xlabel("L")
plt.ylabel("Ψ²")
plt.show()
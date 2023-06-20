# Libraries
import matplotlib.pyplot as plt
import numpy as np

# Initialize and Declaration
R = np.linspace(1, 10, 1000) # Resistance
C = np.linspace(1e-9, 1e-8, 1000) # Capacitance

# Calculation
def f(r, c):
    return 1 / (2 * np.pi * r * c)
X, Y = np.meshgrid(R, C)
Z = f(X, Y)

# Visualization 3D
fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot_surface(X, Y, Z, cmap = "hot")
ax.grid(False)
ax.set_title("3D Visualization of Cut-Off Frequency")
ax.set_xlabel("Resistance")
ax.set_ylabel("Capacitance")
ax.set_zlabel("Frequency")
plt.show()

# Visualization 2D
Z = Z[:-1, :-1]
fig, ax = plt.subplots()
ax.set_title("2D Visualization of Cut-Off Frequency")
plt.pcolormesh(X, Y, Z, cmap = "hot")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.show()
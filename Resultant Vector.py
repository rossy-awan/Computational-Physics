# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Calculation
A = np.array([2, 3, 0]) # 2i + 3j + 0k
B = np.array([4, -2, 6]) # 4i - 2j + 6k
C = A + B
D = (sum(C[0:3] ** 2)) ** .5
print(C)
print(D)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot([0, A[0]], [0, A[1]], [0, A[2]], color = 'gray') # A
ax.plot([0, B[0]], [0, B[1]], [0, B[2]], color = 'gray') # B
ax.plot([0, C[0]], [0, C[1]], [0, C[2]], color = 'blue') # C = A + B
ax.scatter3D(0, 0, 0, color = 'gray')
ax.scatter3D(A[0], A[1], A[2], color = 'gray')
ax.scatter3D(B[0], B[1], B[2], color = 'gray')
ax.scatter3D(C[0], C[1], C[2], color = 'blue')
ax.text(1.05 * A[0], 1.05 * A[1], 1.05 * A[2], 'A', color = 'gray')
ax.text(1.05 * B[0], 1.05 * B[1], 1.05 * B[2], 'B', color = 'gray')
ax.text(1.05 * C[0], 1.05 * C[1], 1.05 * C[2], 'A + B', color = 'blue')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.grid(False)
plt.show()
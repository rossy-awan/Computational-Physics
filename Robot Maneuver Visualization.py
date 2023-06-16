# Libraries
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

rnd, exp, pi, cos, sin = np.round, np.exp, np.pi, np.cos, np.sin
period = 1
data = .15

# START
# Visualization of Functions
print("START")
print("Visualization of Functions")
t = np.arange(0, period, .001)
x = lambda t: np.array([.5 * i - .5 * data * sin(pi*i/data) / pi if 0<i<data else i - .5 * data for i in t])
v = lambda t: np.array([.5 - .5 * cos(pi*i/data) if 0<i<data else 1 for i in t])
plt.plot(t, x(t), label = "Position")
plt.plot(t, v(t), label = "Velocity")
plt.xlabel("Time (s)")
plt.legend(loc = "best")
plt.xlim(-0.1, 1.1)
plt.show()

a = lambda t: np.array([.5 * pi * sin(pi*i/data) / data if 0<i<data else 0 for i in t])
j = lambda t: np.array([.5 * cos(pi*i/data) * (pi / data) ** 2 if 0<i<data else 0 for i in t])
plt.plot(t, a(t), color = "red", label = "Acceleration")
plt.plot(t, j(t), color = "green", label = "Jerk")
plt.xlabel("Time (s)")
plt.legend(loc = "best")
plt.xlim(-0.1, 1.1)
plt.show()

# Positional Visualization
print("Positional Visualization")
t = np.linspace(0, 1, 100)
x1 = .5 * t - .5 * data * sin(pi*t/data) / pi
x2 = t - .5 * data
y = sin(0 * t)
dataSet1, dataSet2 = np.array([x1, y]), np.array([x2, y])
counts = len(t)

def animate_func(i):
    ax.clear()
    if i < data * 100:
        ax.scatter(dataSet1[0, i], dataSet1[1, i], color='blue')
    else:
        ax.scatter(dataSet2[0, i], dataSet2[1, i], color='blue')
    ax.set_xlim([-0.25, 1.25])
    ax.set_ylim([-1, 1])
    ax.set_title('Position\nTime = ' + str(rnd(t[i], decimals = 2)) + ' Second')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')

fig = plt.figure()
ax = plt.axes()
animate = animation.FuncAnimation(fig, animate_func, interval = 10, frames = counts)
plt.show()

# STOP
# Visualization of Functions
print("\nSTOP")
print("Visualization of Functions")
t = np.arange(0, 5 * data, .001)
x = lambda t: np.array([i if 0<i<4*data else .5 * i - .5 * data * cos(pi*i/data + .5*pi) / pi + 2 * data for i in t])
v = lambda t: np.array([1 if 0<i<4*data else .5 + .5 * sin(pi*i/data + .5*pi) for i in t])
plt.plot(t, x(t), label = "Position")
plt.plot(t, v(t), label = "Velocity")
plt.xlabel("Time (s)")
plt.legend(loc = "best")
plt.xlim(-0.1, 0.9)
plt.show()

a = lambda t: np.array([0 if 0<i<4*data else .5 * pi * cos(pi*i/data + .5*pi) / data for i in t])
j = lambda t: np.array([0 if 0<i<4*data else - .5 * sin(pi*i/data + .5*pi) * (pi / data) ** 2 for i in t])
plt.plot(t, a(t), color = "red", label = "Acceleration")
plt.plot(t, j(t), color = "green", label = "Jerk")
plt.xlabel("Time (s)")
plt.legend(loc = "best")
plt.xlim(-0.1, 0.9)
plt.show()

# Positional Visualization
print("Positional Visualization")
t = np.linspace(0, 5 * data, 100)
x1 = t
x2 = .5 * t - .5 * data * cos(pi*t/data + .5*pi) / pi + 2 * data
y = sin(0 * t)
dataSet1, dataSet2 = np.array([x1, y]), np.array([x2, y])
counts = len(t)

def animate_func(i):
    ax.clear()
    if i < 5 * data * 100:
        ax.scatter(dataSet1[0, i], dataSet1[1, i], color='orange')
    else:
        ax.scatter(dataSet2[0, i], dataSet2[1, i], color='orange')
    ax.set_xlim([-0.25, 1.25])
    ax.set_ylim([-1, 1])
    ax.set_title('Position\nTime = ' + str(rnd(- (t[i] - 5 * data), decimals = 2)) + ' Last Second')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')

fig = plt.figure()
ax = plt.axes()
animate = animation.FuncAnimation(fig, animate_func, interval = 10, frames = counts)
plt.show()
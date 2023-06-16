# Libraries
from matplotlib import animation
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# Initialize and Declaration
rnd, exp, pi, cos, sin = np.round, np.exp, np.pi, np.cos, np.sin
theta0, length, time_step, total_time = pi / 8, 2, 0.01, 5

# Numerical Solving and Simulation
def pendulum(theta, t, length):
    g = 9.81  # Earth's Gravity Acceleration
    dtheta_dt = theta[1]
    d2theta_dt2 = -g / length * sin(theta[0])
    return [dtheta_dt, d2theta_dt2]

t = np.arange(0, total_time, time_step) # Arrays
sol = odeint(pendulum, [theta0, 0], t, args=(length,)) # ODEInt Numerical Solution

# Angle and Angular Velocity Data from Numerical Solutions
theta = sol[:, 0]
omega = sol[:, 1]
    
# Pendulum Position on X and Y Coordinates
x = length * sin(theta)
y = -length * cos(theta)

# Calculating Periods
for i in range(1, len(theta)):
    if theta[i] >= 0 and theta[i-1] < 0:
        t_up = t[i]
    elif theta[i] <= 0 and theta[i-1] > 0:
        t_down = t[i]
    
period = 2 * (t_down - t_up) # 2πdt/dθ
print(f'Period: {abs(period)}')
        
# Pendulum Kinematics Visualization
plt.plot(t, theta, label = 'Angle (rad)')
plt.plot(t, omega, label = 'Angular Velocity (rad/s)')
plt.xlabel('Time (s)')
plt.title('Pendulum Kinematics')
#plt.grid(True)
plt.legend(loc = "best")
plt.show()
    
# Pendulum Trajectory
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Pendulum Trajectory')
plt.axis('equal')
plt.show()

# Trajectory Animation
print("Trajectory Animation")

def animate_func(i):
    ax.clear()
    ax.scatter(x[i], y[i])
    ax.plot([x[i], 0], [y[i], 0])
    ax.axis('equal')
    ax.set_title(f'Pendulum Trajectory\nTime = {rnd(t[i], decimals = 2)} s')
    ax.set_xlim([np.min(x) - 1, np.max(x) + 1])
    ax.set_ylim([np.min(y) - 1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

fig = plt.figure()
ax = plt.axes()
animate = animation.FuncAnimation(fig, animate_func, interval = 10, frames = len(theta))
plt.show()
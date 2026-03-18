# Lab Topic: Discrete System Simulation (Monte Carlo Method – Estimating π)
# This program estimates the value of π using random sampling with the Monte Carlo method.

import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(num_samples):
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)

    distance = np.sqrt(x**2 + y**2)

    inside_circle = np.sum(distance <= 1)

    pi_estimate = (inside_circle / num_samples) * 4

    return inside_circle, pi_estimate

num_samples = 1000000

inside_circle, pi_estimate = monte_carlo_pi(num_samples)

print(f"Points inside the circle: {inside_circle}")
print(f"Estimated value of π with {num_samples} samples: {pi_estimate}")
x = np.random.uniform(-1, 1, num_samples)
y = np.random.uniform(-1, 1, num_samples)
plt.figure(figsize=(6, 6))
plt.scatter(x, y, c=np.sqrt(x**2 + y**2) <= 1, cmap='bwr', s=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Monte Carlo Simulation for π - Bibek Singh')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
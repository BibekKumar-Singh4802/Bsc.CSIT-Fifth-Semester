# Lab Topic: Continuous System Simulation – Chemical Reactions
# This program simulates chemical reaction dynamics using continuous system models.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # Import pandas

print("Simulating reaction of chemicals c1, c2 and c3...")

# Simulation parameters
dt = 0.001
time = 100.0
steps = int(time / dt)

k1 = 0.025
k2 = 0.01

# Arrays to store results
t_values = np.linspace(0, time, steps + 1)
c1 = np.zeros(steps + 1)
c2 = np.zeros(steps + 1)
c3 = np.zeros(steps + 1)

# Initial values
c1[0] = 70.0
c2[0] = 30.0
c3[0] = 0.0

# Simulation loop (Euler's method)
for i in range(steps):
    c1[i + 1] = c1[i] + (k2 * c3[i] - k1 * c1[i] * c2[i]) * dt
    c2[i + 1] = c2[i] + (k2 * c3[i] - k1 * c1[i] * c2[i]) * dt
    c3[i + 1] = c3[i] + 2.0 * (k1 * c1[i] * c2[i] - k2 * c3[i]) * dt

# Save data to file
output_data = np.column_stack((t_values, c1, c2, c3))
np.savetxt("lab1_output.txt", output_data, fmt="%.6f", header="time  c1  c2  c3")

print("Simulation completed. File saved as lab1_output.txt.")

# Read the generated file and display its content
print("\nReading the generated file 'lab1_output.txt':")

df_output = pd.read_csv("lab1_output.txt", sep='\s+', skiprows=1, names=['time', 'c1', 'c2', 'c3'])
print(df_output.head(200))
 # Display the first 5 rows

# ------------------------------
# Plot the results
# ------------------------------
plt.figure(figsize=(10, 6))
plt.plot(t_values, c1, label="C1", linewidth=2)
plt.plot(t_values, c2, label="C2", linewidth=2)
plt.plot(t_values, c3, label="C3", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("Chemical Reaction Simulation- Shishir Ghimire")
plt.legend()
plt.grid(True)
plt.show()
# Lab Topic: Kolmogorov-Smirnov (KS) Test for Uniformity
# This program tests whether a set of random numbers follows a uniform distribution using the KS test.


import numpy as np

# User inputs the random numbers
sample_size = int(input("Enter the number of random numbers: "))
random_numbers = []

print(f"Enter {sample_size} random numbers (between 0 and 1):")
for i in range(sample_size):
    num = float(input(f"Enter number {i+1}: "))
    random_numbers.append(num)

random_numbers.sort()  # Sorting the numbers

# Calculate Fn(Ri), i/N, and (i-1)/N
i_values = np.arange(1, sample_size + 1)
Fn_Ri = i_values / sample_size
Fn_minus_1_Ri = (i_values - 1) / sample_size

# Calculate D+ and D-
D_plus = Fn_Ri - random_numbers
D_minus = random_numbers - Fn_minus_1_Ri
D_statistic = max(max(D_plus), max(D_minus))

# Critical D value for α = 0.05 (assuming standard table values)
D_alpha = 1.36 / np.sqrt(sample_size)

# Print formatted output
print("\nSorted Random Numbers:")
print(" ".join(f"{num:.4f}" for num in random_numbers))

print("\nTable: [Bibek Singh]")
print("------------------------------------------------------------")
print(f"{'Ri':<10}{'i/N':<10}{'(i-1)/N':<10}{'Fn(Ri)':<10}{'D+':<10}{'D-':<10}")
print("------------------------------------------------------------")

for i in range(sample_size):
    print(f"{random_numbers[i]:<10.4f}{Fn_Ri[i]:<10.4f}{Fn_minus_1_Ri[i]:<10.4f}"
          f"{Fn_Ri[i]:<10.4f}{D_plus[i]:<10.4f}{D_minus[i]:<10.4f}")

print("------------------------------------------------------------")
print(f"D+ = {max(D_plus):.6f}")
print(f"D- = {max(D_minus):.6f}")
print(f"D statistic (D) = {D_statistic:.6f}")
print(f"Critical D value (D_alpha) = {D_alpha:.6f}")

# Hypothesis testing
print("\nConclusion:")
if D_statistic < D_alpha:
    print("Since D_statistic < D_alpha \nFail to reject H0: No significant difference detected. The sample follows a uniform distribution.")
else:
    print("Since D_statistic > D_alpha \nReject H0: Significant difference detected. The sample does not follow a uniform distribution.")
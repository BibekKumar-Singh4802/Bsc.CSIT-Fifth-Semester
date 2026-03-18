# Lab Topic: Chi-Square Test for Uniformity
# This program tests the uniformity of random numbers using the Chi-Square test.
#
import numpy as np
from scipy.stats import chi2
from tabulate import tabulate

# Step 1: Take user inputs
num_intervals = int(input("Enter the number of intervals: "))

intervals = []
observed_frequencies = []

# Step 2: Get interval ranges from the user
print("\nEnter the interval ranges:")
for i in range(num_intervals):
    start, end = map(float, input(f"Interval {i+1} (start end): ").split())
    intervals.append((start, end))

# Step 3: Get observed frequencies from the user
print("\nEnter the observed frequencies for each interval:")
for i in range(num_intervals):
    freq = int(input(f"Observed frequency for interval {intervals[i]}: "))
    observed_frequencies.append(freq)

# Step 4: Compute expected frequency assuming uniform distribution
total_observed = sum(observed_frequencies)
expected_frequency = total_observed / num_intervals  # Assuming uniform distribution
expected_frequencies = [expected_frequency] * num_intervals

# Step 5: Calculate Chi-Square statistic
chi_square_values = [( (O - E) ** 2 ) / E for O, E in zip(observed_frequencies, expected_frequencies)]
chi_square_statistic = sum(chi_square_values)

# Step 6: Calculate critical value automatically
alpha = 0.05  # Significance level (5%)
df = num_intervals - 1  # Degrees of freedom
critical_value = chi2.ppf(1 - alpha, df)

# Step 7: Display results in a formatted table
table_data = []
for i in range(num_intervals):
    table_data.append([intervals[i], observed_frequencies[i], expected_frequencies[i], chi_square_values[i]])

headers = ["Interval", "Observed (O)", "Expected (E)", "(O - E)² / E"]
print("\nChi-Square Test Results [Bibek Singh]:\n")
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Step 8: Conclusion based on calculated vs. critical value
print("\nConclusion:")
print(f"Calculated χ² = {chi_square_statistic:.4f}")
print(f"Critical χ² (α={alpha}, df={df}) = {critical_value:.4f}")

if chi_square_statistic > critical_value:
    print("Since χ²_calculated > χ²_critical, the null hypothesis is REJECTED.")
else:
    print("Since χ²_calculated ≤ χ²_critical, the null hypothesis is NOT rejected.")
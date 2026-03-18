# Lab Topic: Linear Congruential Method of Random Number Generation
# This program implements the Linear Congruential Generator (LCG) for pseudo-random numbers.

# Function to generate random numbers using Linear Congruential Method
def linear_congruential_method(X0, a, c, m, n):
    Xn = X0  # Initialize seed value
    print("\nGenerated Random Numbers [ Bibek Singh ]:")
    for i in range(n):
        Xn = (a * Xn + c) % m  # LCM formula
        print(f"X{i} = {Xn}")  # Print the generated number

# Taking user input
X0 = int(input("Enter seed value (X0): "))
a = int(input("Enter multiplier (a): "))
c = int(input("Enter increment (c): "))
m = int(input("Enter modulus (m): "))
n = int(input("Enter number of random numbers to generate: "))

# Generate and display random numbers
linear_congruential_method(X0, a, c, m, n)


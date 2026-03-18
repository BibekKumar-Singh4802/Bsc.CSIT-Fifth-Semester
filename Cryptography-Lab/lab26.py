# Lab Topic: Co-primality Check
# This program checks whether two given numbers are co-prime using gcd.

def check_coprime(a, b):
    # Standard Euclidean Algorithm
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    res = gcd(a, b)
    if res == 1:
        print(f"{a} and {b} are co-prime.")
    else:
        print(f"{a} and {b} are NOT co-prime (GCD is {res}).")

# ---- Main Program ----
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

check_coprime(a, b)

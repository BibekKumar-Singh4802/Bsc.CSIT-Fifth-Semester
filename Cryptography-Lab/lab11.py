def extended_gcd_steps(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    orig_a, orig_b = a, b
    
    print(f"{'q':<5} | {'r':<5} | {'x':<5} | {'y':<5}")
    print("-" * 25)
    
    while b != 0:
        q = a // b
        r = a % b
        # Update coefficients
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        print(f"{q:<5} | {r:<5} | {x0:<5} | {y0:<5}")
        a, b = b, r
        
    print("-" * 25)
    print(f"GCD: {a}")
    print(f"Equation: ({x0})*{orig_a} + ({y0})*{orig_b} = {a}")
    return a, x0, y0


# ---- Main Program ----
print("Extended Euclidean Algorithm")
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

gcd, x, y = extended_gcd_steps(a, b)
print(f"\nResult: gcd({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")

def miller_rabin_detailed(n, a):
    print(f"Testing n={n} with base a={a}")
    # Step 1: Find k, m such that n-1 = 2^k * m
    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    print(f"  n-1 = 2^{k} * {m}")

    # Step 2: Compute x = a^m mod n
    x = pow(a, m, n)
    print(f"  Initial x = {a}^{m} mod {n} = {x}")
    
    if x == 1 or x == n - 1:
        return "Probably Prime"

    # Step 3: Repeat x = x^2 mod n
    for i in range(k - 1):
        x = pow(x, 2, n)
        print(f"  Squaring {i+1}: x = {x}")
        if x == n - 1:
            return "Probably Prime"
    return "Composite"


# ---- Main Program ----
print("Miller–Rabin Primality Test")
n = int(input("Enter n (number to test): "))
a = int(input("Enter a (base): "))

result = miller_rabin_detailed(n, a)
print(f"\nResult: {result}")

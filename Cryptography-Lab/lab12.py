def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def implement_theorems(n, a):
    # 1. Euler's Totient (φ(n))
    coprimes = [i for i in range(1, n) if gcd(i, n) == 1]
    phi = len(coprimes)
    print(f"Coprimes of {n}: {coprimes}")
    print(f"φ({n}) = {phi}")

    # 2. Euler's Theorem: a^φ(n) ≡ 1 (mod n) if gcd(a,n)=1
    if gcd(a, n) == 1:
        res = pow(a, phi, n)
        print(f"Euler's Theorem: {a}^{phi} mod {n} = {res}")
    else:
        print(f"Euler's Theorem not applicable since gcd({a},{n}) ≠ 1")

    # 3. Fermat's Little Theorem (only if n is prime)
    if all(n % i != 0 for i in range(2, int(n**0.5)+1)):
        fermat = pow(a, n-1, n)
        print(f"Fermat's Theorem: {a}^{n-1} mod {n} = {fermat}")
    else:
        print(f"Fermat's Theorem not applicable since {n} is not prime")


# ---- Main Program ----
print("Euler & Fermat Theorems")
n = int(input("Enter n: "))
a = int(input("Enter a: "))

implement_theorems(n, a)

# Lab Topic: Diffie–Hellman Key Exchange Simulation
# This program demonstrates how two parties (Alice and Bob) can agree on a shared secret key
# over an insecure channel using modular exponentiation. It shows the public parameters,
# private keys, public values, and the final shared secret calculation step by step.

def simulate_dh():
    q, alpha = 23, 5  # Public prime and primitive root
    print(f"Public: q={q}, alpha={alpha}")

    # Alice
    xa = 6  # Private key
    ya = pow(alpha, xa, q)  # Public value
    print(f"Alice: Private={xa}, Public(Ya)={ya}")

    # Bob
    xb = 15  # Private key
    yb = pow(alpha, xb, q)  # Public value
    print(f"Bob: Private={xb}, Public(Yb)={yb}")

    # Shared Secret Calculation
    ka = pow(yb, xa, q)  # Alice computes
    kb = pow(ya, xb, q)  # Bob computes
    print(f"Calculated Keys: Alice={ka}, Bob={kb}")

simulate_dh()

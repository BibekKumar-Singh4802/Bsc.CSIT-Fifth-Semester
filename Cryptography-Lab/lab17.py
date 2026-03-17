"""
Lab Topic: ElGamal Cryptosystem

This program simulates encryption and decryption using the ElGamal public-key scheme.
It demonstrates key generation, encryption with a random session key, and decryption
using modular arithmetic. The security is based on the discrete logarithm problem.
"""

def elgamal_detailed():
    # Public parameters (prime q and primitive root alpha)
    q, alpha = 23, 5
    print(f"Public parameters: q={q}, alpha={alpha}")

    # Alice's private and public keys
    xa = 12  # Alice's private key
    ya = pow(alpha, xa, q)  # Alice's public key
    print(f"Alice: Private={xa}, Public={ya}")

    # Message to encrypt
    m = 10
    print(f"Message to encrypt: {m}")

    # Random integer for encryption
    k = 15
    print(f"Random k chosen: {k}")

    # Encryption
    K = pow(ya, k, q)
    c1 = pow(alpha, k, q)
    c2 = (K * m) % q
    print(f"Ciphertext: (C1={c1}, C2={c2})")

    # Decryption
    K_back = pow(c1, xa, q)
    k_inv = pow(K_back, q-2, q)  # Fermat’s theorem since q is prime
    recovered_m = (c2 * k_inv) % q
    print(f"Decrypted Message: {recovered_m}")

elgamal_detailed()

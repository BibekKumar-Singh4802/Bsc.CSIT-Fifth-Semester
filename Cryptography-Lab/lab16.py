def rsa_detailed():
    p, q = 45,30
    n = p * q
    phi = (p-1) * (q-1)
    e = 7  # Must be coprime to phi
    
    # Finding d manually: (e*d) % phi == 1
    d = 0
    for i in range(1, 1000):
        if (e * i) % phi == 1:
            d = i
            break
    print(f"Keys: Public(e={e}, n={n}), Private(d={d})")

    msg = 99
    # Encrypt
    cipher = (msg ** e) % n
    print(f"Encryption: {msg}^{e} mod {n} = {cipher}")

    # Decrypt
    plain = (cipher ** d) % n
    print(f"Decryption: {cipher}^{d} mod {n} = {plain}")

rsa_detailed()
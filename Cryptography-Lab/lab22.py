import hashlib

def rsa_signature_verbose():
    print("--- RSA DIGITAL SIGNATURE VERBOSE ---")
    
    # 1. Key Generation
    p, q = 200, 175
    n = p * q
    phi = (p-1) * (q-1)
    e = 17
    d = pow(e, -1, phi)
    
    print(f"[STEP 1] Keys Generated:")
    print(f"         Public Key: (e={e}, n={n})")
    print(f"         Private Key: (d={d}, n={n})")

    # 2. Message and Hashing
    message = "Approved_Lab_Report"
    # We turn the string hash into an integer to perform math on it
    h_hex = hashlib.sha256(message.encode()).hexdigest()
    m = int(h_hex, 16) % n
    print(f"\n[STEP 2] Hashing Message:")
    print(f"         Message: '{message}'")
    print(f"         Full Hash: {h_hex[:16]}...")
    print(f"         Message Integer (m = hash mod n): {m}")

    # 3. Signing
    print(f"\n[STEP 3] Signing with Private Key (d):")
    print(f"         Calculating: S = {m}^{d} mod {n}")
    signature = pow(m, d, n)
    print(f"         Generated Signature (S): {signature}")

    # 4. Verification
    print(f"\n[STEP 4] Verifying with Public Key (e):")
    print(f"         Calculating: V = {signature}^{e} mod {n}")
    decrypted_m = pow(signature, e, n)
    print(f"         Decrypted Value (V): {decrypted_m}")

    # 5. Final Comparison
    print(f"\n[STEP 5] Integrity Check:")
    if m == decrypted_m:
        print("         Result: SUCCESS! m == V. The signature is valid.")
    else:
        print("         Result: FAILED! Signature is invalid.")

rsa_signature_verbose()
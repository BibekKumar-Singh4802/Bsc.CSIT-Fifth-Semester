# Lab Topic: SHA-256 and SHA-512 Hash Functions
# This program implements SHA-2 family algorithms for strong cryptographic hashing.

import hashlib

def sha_comparison(message):
    print(f"--- SHA-256 vs SHA-512 ---")
    data = message.encode()
    
    sha256 = hashlib.sha256(data).hexdigest()
    sha512 = hashlib.sha512(data).hexdigest()
    
    print(f"SHA-256 (Length {len(sha256)*2} \nbits): {len(sha256)*2} bits): {sha256}")
    print("-" * 20)
    print(f"SHA-512 (Length {len(sha512)*2} \nbits): {sha512}")

sha_comparison("Lab_Report_2082_Testing")
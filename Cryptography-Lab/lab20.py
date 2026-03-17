# Lab Topic: MD5 Hash Function
# This program demonstrates the MD5 hashing algorithm for message integrity verification.

import hashlib

def implement_md5(text):
    print("--- MD5 Implementation ---")
    # Step 1: Input
    print(f"Input String: {text}")
    
    # Step 2: Generate Hash using hashlib
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    
    # Step 3: Output
    print(f"Step 1: Message Digest generated.")
    print(f"Resulting MD5: {md5_hash}")

implement_md5("Cryptography_Lab_Report(20)")
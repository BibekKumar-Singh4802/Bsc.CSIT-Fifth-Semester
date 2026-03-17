"""
Lab 8: Meet-in-the-Middle Attack on Double DES
"""

def simple_encrypt(plaintext, key):
    """Simple DES-like encryption"""
    result = 0
    for i in range(16):
        bit = (plaintext >> i) & 1
        key_bit = (key >> i) & 1
        result |= ((bit ^ key_bit) << i)
    return result

def double_des_encrypt(plaintext, key1, key2):
    """Double DES encryption"""
    intermediate = simple_encrypt(plaintext, key1)
    ciphertext = simple_encrypt(intermediate, key2)
    return ciphertext

def meet_in_middle_attack(plaintext, ciphertext, key_space=256):
    """Meet-in-the-Middle Attack"""
    print(f"Plaintext: {plaintext} (0x{plaintext:04x})")
    print(f"Ciphertext: {ciphertext} (0x{ciphertext:04x})")
    print("-" * 40)
    
    # Phase 1: Forward encryptions
    print("Phase 1: Computing forward encryptions...")
    forward_table = {}
    
    for key1 in range(key_space):
        intermediate = simple_encrypt(plaintext, key1)
        forward_table[intermediate] = key1
    
    print(f"Forward table size: {len(forward_table)}")
    
    # Phase 2: Backward decryptions
    print("Phase 2: Matching with decryptions...")
    candidates = []
    
    for key2 in range(key_space):
        intermediate = simple_encrypt(ciphertext, key2)
        
        if intermediate in forward_table:
            key1 = forward_table[intermediate]
            candidates.append((key1, key2))
    
    return candidates

print("Meet-in-the-Middle Attack on Double DES")
choice = input("1:Attack with keys 2:Demo: ")

if choice == '1':
    plaintext = int(input("Enter plaintext (hex): "), 16)
    ciphertext = int(input("Enter ciphertext (hex): "), 16)
    key_space = int(input("Key space size (e.g., 256): "))
    
    candidates = meet_in_middle_attack(plaintext, ciphertext, key_space)
    print(f"\nFound {len(candidates)} candidate(s):")
    for k1, k2 in candidates[:3]:
        print(f"Key1: 0x{k1:04x}, Key2: 0x{k2:04x}")
        verify = double_des_encrypt(plaintext, k1, k2)
        if verify == ciphertext:
            print("✓ Valid!")

elif choice == '2':
    key1 = 0x42
    key2 = 0x7F
    plaintext = 0x1234
    ciphertext = double_des_encrypt(plaintext, key1, key2)
    
    print(f"Secret Key1: 0x{key1:04x}")
    print(f"Secret Key2: 0x{key2:04x}")
    print(f"Plaintext: 0x{plaintext:04x}")
    print(f"Ciphertext: 0x{ciphertext:04x}")
    
    candidates = meet_in_middle_attack(plaintext, ciphertext, 256)
    print(f"\nFound {len(candidates)} match(es)")
    if (key1, key2) in candidates:
        print("✓ Correct key pair found!")

else:
    print("Invalid")
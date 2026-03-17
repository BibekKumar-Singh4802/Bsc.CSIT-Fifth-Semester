def idea_round_detailed(p, keys):
    # p = [p1, p2, p3, p4] (16-bit blocks)
    # 1. Multiply & Add
    s1 = (p[0] * keys[0]) % 65537
    s2 = (p[1] + keys[1]) % 65536
    s3 = (p[2] + keys[2]) % 65536
    s4 = (p[3] * keys[3]) % 65537
    
    # 2. The MA Structure (Inner transformations)
    s5 = s1 ^ s3
    s6 = s2 ^ s4
    s7 = (s5 * keys[4]) % 65537
    s8 = (s6 + s7) % 65536
    s9 = (s8 * keys[5]) % 65537
    s10 = (s7 + s9) % 65536
    
    # 3. Final XOR
    return [s1 ^ s9, s3 ^ s9, s2 ^ s10, s4 ^ s10]


# ---- Main Program ----
# Ask user for plaintext (4 blocks)
p = []
print("Enter 4 plaintext blocks (16-bit integers):")
for i in range(4):
    p.append(int(input(f"p{i+1}: ")))

# Ask user for 6 keys
k = []
print("\nEnter 6 subkeys (16-bit integers):")
for i in range(6):
    k.append(int(input(f"k{i+1}: ")))

# Run IDEA round
result = idea_round_detailed(p, k)
print("\nIDEA Round State:", result)

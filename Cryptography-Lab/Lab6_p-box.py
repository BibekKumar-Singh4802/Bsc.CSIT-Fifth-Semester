"""
Lab 6: P-box (Permutation Box) - Expansion and Compression
"""

EXPANSION_BOX = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

COMPRESSION_BOX = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

def apply_permutation(data, pbox):
    """Apply permutation to binary string"""
    return ''.join(data[pbox[i] - 1] for i in range(len(pbox)))

def expansion_box(data_32bit):
    """Expand 32-bit to 48-bit"""
    return apply_permutation(data_32bit, EXPANSION_BOX)

def compression_box(data_32bit):
    """Apply compression P-box to 32-bit"""
    return apply_permutation(data_32bit, COMPRESSION_BOX)

print("P-box: Expansion and Compression")
choice = input("1:Expansion (32->48) 2:Compression (32->32): ")

if choice == '1':
    data = input("Enter 32-bit binary: ")
    if len(data) == 32 and all(c in '01' for c in data):
        result = expansion_box(data)
        print(f"Output (48 bits): {result}")
    else:
        print("Error: Must be exactly 32 binary digits (0s and 1s)")
elif choice == '2':
    data = input("Enter 32-bit binary: ")
    if len(data) == 32 and all(c in '01' for c in data):
        result = compression_box(data)
        print(f"Output (32 bits): {result}")
    else:
        print("Error: Must be exactly 32 binary digits (0s and 1s)")
else:
    print("Invalid")
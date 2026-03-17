# Lab Topic: MD4 Hash Function
# This program implements the MD4 hashing algorithm to produce fixed-length digests.



import struct

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def F(x, y, z): return (x & y) | (~x & z)

def lab19_md4_verbose(message):
    print(f"--- MD4 VERBOSE EXECUTION ---")
    print(f"[1] Input Message: {message}")
    
    # Padding logic
    msg_bytes = bytearray(message, 'utf-8')
    orig_len_bits = (len(msg_bytes) * 8) & 0xffffffffffffffff
    msg_bytes.append(0x80)
    while len(msg_bytes) % 64 != 56:
        msg_bytes.append(0x00)
    msg_bytes += struct.pack('<Q', orig_len_bits)
    
    print(f"[2] Post-Padding Hex: {msg_bytes.hex()[:64]}...")
    print(f"[3] Message Length: {len(msg_bytes)} bytes ({len(msg_bytes)//64} block(s))")

    # Initialize Buffers
    A, B, C, D = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476
    print(f"[4] Initial Registers: A={hex(A)}, B={hex(B)}, C={hex(C)}, D={hex(D)}")

    # Process first block
    X = struct.unpack('<16I', msg_bytes[0:64])
    print(f"\n[5] Starting Round 1 (F-Function Operations):")
    
    for i in range(16):
        s = [3, 7, 11, 19][i % 4]
        f_val = F(B, C, D)
        A = left_rotate((A + f_val + X[i]) & 0xffffffff, s)
        # Shift registers
        A, B, C, D = D, A, B, C
        if i < 4: # Show first 4 steps of bit-shifting
            print(f"    Step {i+1}: Registers -> A:{hex(A)} B:{hex(B)} C:{hex(C)} D:{hex(D)}")

    print(f"\n[RESULT] Final MD4 Digest Preview: {hex(A)}{hex(B)[2:]}{hex(C)[2:]}{hex(D)[2:]}")

lab19_md4_verbose("Namaste")
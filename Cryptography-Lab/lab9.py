# Simplified S-Box for demonstration (Real AES uses a 256-value lookup table)
SBOX = [i for i in range(256)] # In practice, this is a complex non-linear mapping

def sub_bytes(state):
    return [SBOX[b] for b in state]

def shift_rows(state):
    # state is a 16-byte list representing a 4x4 matrix
    # [s0, s4, s8, s12]
    # [s1, s5, s9, s13] ...
    res = [0] * 16
    res[0], res[4], res[8], res[12] = state[0], state[4], state[8], state[12]   # Row 0
    res[1], res[5], res[9], res[13] = state[5], state[9], state[13], state[1]   # Row 1 shift 1
    res[2], res[6], res[10], res[14] = state[10], state[14], state[2], state[6] # Row 2 shift 2
    res[3], res[7], res[11], res[15] = state[15], state[3], state[7], state[11] # Row 3 shift 3
    return res

def add_round_key(state, key):
    return [s ^ key for s in state]

def aes_encrypt(plaintext, key_val):
    # AES-128 requires 16 bytes (128 bits)
    if len(plaintext) < 16: plaintext = plaintext.ljust(16)
    state = [ord(c) for c in plaintext[:16]]
    
    print(f"Initial State: {state}")
    
    # Initial Round
    state = add_round_key(state, key_val)
    
    # 9 Rounds (SubBytes -> ShiftRows -> MixColumns -> AddRoundKey)
    for r in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        # MixColumns skipped for brevity as it involves GF(2^8) math
        state = add_round_key(state, key_val + r) # Simple key schedule simulation
        print(f"End of Round {r}: {state[:4]}...")

    # Final Round (No MixColumns)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_val + 10)
    
    # Convert to Hex instead of raw text to avoid "out of this world" symbols
    return bytes(state).hex()

msg = "SECRET_MESSAGE12"
print("AES Final Result (Hex):", aes_encrypt(msg, 0x42))
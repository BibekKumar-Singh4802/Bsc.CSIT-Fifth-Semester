"""
 Lab Topic: Message Authentication Code (MAC)
 This program generates and verifies a MAC to ensure message integrity and authenticity.
"""
import hashlib

def manual_hmac(key, message):
    # HMAC uses a specific block size (usually 64 bytes for SHA-256)
    block_size = 64
    
    # Step 1: Prepare the Key
    # If key is longer than block_size, hash it first
    if len(key) > block_size:
        key = hashlib.sha256(key).digest()
    # If key is shorter, pad it with zeros to the right
    if len(key) < block_size:
        key = key.ljust(block_size, b'\x00')
    
    print(f"Key (padded/hashed): {key.hex()[:20]}...")

    # Step 2: Inner Padding (ipad) and Outer Padding (opad)
    # These are constants defined in RFC 2104
    ipad = bytes([b ^ 0x36 for b in key])
    opad = bytes([b ^ 0x5c for b in key])

    print(f"Ipad (first 10 bytes): {ipad.hex()[:20]}")
    print(f"Opad (first 10 bytes): {opad.hex()[:20]}")

    # Step 3: Inner Hash
    # Hash(ipad + message)
    inner_content = ipad + message.encode()
    inner_hash = hashlib.sha256(inner_content).digest()
    print(f"Inner Hash: {inner_hash.hex()[:20]}...")

    # Step 4: Outer Hash
    # Hash(opad + Inner Hash)
    outer_content = opad + inner_hash
    final_mac = hashlib.sha256(outer_content).hexdigest()

    return final_mac

# Testing the implementation
secret_key = b"my_super_secret_key"
msg_text = "This is a secure message."

mac_result = manual_hmac(secret_key, msg_text)

print("-" * 30)
print(f"Message: {msg_text}")
print(f"MAC (HMAC-SHA256): {mac_result}")
print("-" * 30)

# Verification Simulation
def verify_mac(key, message, received_mac):
    calculated_mac = manual_hmac(key, message)
    if calculated_mac == received_mac:
        print("Verification Successful: Message is authentic!")
    else:
        print("Verification Failed: Message or Key has been tampered with!")

verify_mac(secret_key, msg_text, mac_result)
"""
Lab 4: Railfence Cipher Implementation
"""

def railfence_encrypt(plaintext, rails):
    """Encrypt using Railfence Cipher"""
    plaintext = plaintext.upper().replace(" ", "")
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in plaintext:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    
    return ''.join(''.join(f) for f in fence)

def railfence_decrypt(ciphertext, rails):
    """Decrypt using Railfence Cipher"""
    ciphertext = ciphertext.upper().replace(" ", "")
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    # Mark positions
    for _ in range(len(ciphertext)):
        fence[rail].append(None)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    
    # Fill with characters
    idx = 0
    for i in range(rails):
        for j in range(len(fence[i])):
            fence[i][j] = ciphertext[idx]
            idx += 1
    
    # Read in zigzag
    plaintext = ""
    rail = 0
    rail_idx = [0] * rails
    direction = 1
    
    for _ in range(len(ciphertext)):
        plaintext += fence[rail][rail_idx[rail]]
        rail_idx[rail] += 1
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    
    return plaintext

print("Railfence Cipher")
choice = input("1:Encrypt 2:Decrypt: ")
rails = int(input("Enter number of rails: "))

if choice == '1':
    text = input("Enter text: ")
    print("Result:", railfence_encrypt(text, rails))
elif choice == '2':
    text = input("Enter text: ")
    print("Result:", railfence_decrypt(text, rails))
else:
    print("Invalid")
"""
Lab 3: Playfair Cipher Implementation
"""

def create_matrix(key):
    """Create 5x5 Playfair matrix"""
    key = key.upper().replace(" ", "")
    key = ''.join(dict.fromkeys(key))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for c in alphabet:
        if c not in key:
            key += c
    matrix = []
    for i in range(5):
        matrix.append(list(key[i*5:(i+1)*5]))
    return matrix

def find_pos(matrix, char):
    """Find position of character"""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def prepare_text(text):
    """Prepare text for encryption"""
    text = text.upper().replace(" ", "").replace("J", "I")
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                result += 'X'
            else:
                result += text[i + 1]
                i += 1
        i += 1
    
    if len(result) % 2:
        result += 'X'
    return result

def playfair_encrypt(plaintext, key):
    """Encrypt using Playfair Cipher"""
    matrix = create_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        r1, c1 = find_pos(matrix, plaintext[i])
        r2, c2 = find_pos(matrix, plaintext[i+1])
        
        if r1 == r2:
            ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    """Decrypt using Playfair Cipher"""
    matrix = create_matrix(key)
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_pos(matrix, ciphertext[i])
        r2, c2 = find_pos(matrix, ciphertext[i+1])
        
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    
    return plaintext

print("Playfair Cipher")
choice = input("1:Encrypt 2:Decrypt: ")
key = input("Enter key: ")

if choice == '1':
    text = input("Enter text: ")
    result = playfair_encrypt(text, key)
    print(f"Key: {key}")
    print(f"Text: {text}")
    print(f"Result: {result}")
elif choice == '2':
    text = input("Enter text: ")
    result = playfair_decrypt(text, key)
    print(f"Key: {key}")
    print(f"Text: {text}")
    print(f"Result: {result}")
else:
    print("Invalid")

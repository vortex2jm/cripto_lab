def encrypt_vigenere(plaintext, key):
    """
    Encrypts the plaintext using the Vigenere cipher with the given key.
    """
    ciphertext = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    """
    Decrypts the ciphertext encrypted with the Vigenere cipher using the given key.
    """
    plaintext = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

# Example usage:
#plaintext = "This is the unencrypted text!"
#key = "ABC"
#print("Plaintext:", plaintext)
#encrypted_text = encrypt_vigenere(plaintext, key)
#print("Encrypted Text:", encrypted_text)
#decrypted_text = decrypt_vigenere(encrypted_text, key)
#print("Decrypted Text:", decrypted_text)

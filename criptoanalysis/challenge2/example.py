def xor_block(message_block: bytes, key: bytes) -> bytes:
    """XOR operation between a block of message and the key."""
    return bytes([a ^ b for a, b in zip(message_block, key)])

def encrypt(message: bytes, key: bytes) -> bytes:
    """Encrypt the message using XOR block cipher."""
    cipher_text = b''
    for i in range(0, len(message), 16):
        message_block = message[i:i+16]
        cipher_text += xor_block(message_block, key * (len(message_block) // len(key)))
    return cipher_text

def decrypt(cipher_text: bytes, key: bytes) -> bytes:
    """Decrypt the cipher text using XOR block cipher."""
    decrypted_text = b''
    for i in range(0, len(cipher_text), 16):
        cipher_block = cipher_text[i:i+16]
        decrypted_text += xor_block(cipher_block, key * (len(cipher_block) // len(key)))
    return decrypted_text

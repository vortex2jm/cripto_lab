# XOR is a cheap way to encrypt data with a password.
# Any data can be encrypted using XOR as shown in this Python example...
from os import urandom

def genkey(length: int) -> bytes:
    """8-bit key."""
    return str.encode(''.join([chr(ord('A'))*length]))

def xor_strings(s, t) -> bytes:
    """Concate xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode('utf8')
    else:
        # Bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

message = 'This is the unencrypted message!'
print('Message:', message)

key = genkey(len(message))
print('Key:', key)

cipherText = xor_strings(message.encode('utf8'), key)
print('cipherText:', cipherText)
print('decrypted:', xor_strings(cipherText, key).decode('utf8'))

# Verify
if xor_strings(cipherText, key).decode('utf8') == message:
    print('Unit test passed')
else:
    print('Unit test failed')

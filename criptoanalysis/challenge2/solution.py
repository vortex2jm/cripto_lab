CIPHER = b'\x12\'&73#/! b$/a\x01./175#\"#.bsrsvns'

#====================================================#
# Gera uma chave de 16bits
def gen_key_16b(byte1: int, byte2: int) -> bytes:
  return str.encode(''.join([f'{chr(byte1)}{chr(byte2)}']))

#========================================================#
def xor_block(message_block: bytes, key: bytes) -> bytes:
    return bytes([a ^ b for a, b in zip(message_block, key)])

#========================================================#
def decrypt(cipher_text: bytes, key: bytes) -> bytes:
    """Decrypt the cipher text using XOR block cipher."""
    decrypted_text = b''
    for i in range(0, len(cipher_text), 16):
        cipher_block = cipher_text[i:i+16]
        decrypted_text += xor_block(cipher_block, key * (len(cipher_block) // len(key)))
    return decrypted_text

#=======================================================================#
# Verifica se os caracteres da mensagem estão nos limites da tabela ascii
def potential_message(decrypted_msg) -> bool:
   return all(32 <= byte <= 127 for byte in decrypted_msg)

#=============================#
def main():
  # Loop para gerar todas as possíveis chaves de 16 bits
  for x in range(256):
    for y in range(256):
      key = gen_key_16b(x, y)
      text = decrypt(CIPHER, key)
      if potential_message(text):
         print(f'CharKey: {key.decode()}; BinKey: {bin(int(key.hex(), 16))[2:].zfill(16)}; HexKey: {key.hex()}; Text: {text.decode()}')

if __name__ == '__main__':
  main()

# A chave em caracteres é 'AB' e a mensagem é 'Seguranca em Computacao 2024/1'

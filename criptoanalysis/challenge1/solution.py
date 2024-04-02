def genkey(length: int) -> bytes:
    return str.encode(''.join([chr(ord('A'))*length]))

def main():
  cipher = b'rDFTS@OB@\x01DL\x01bNLQTU@B@N\x01\x13\x11\x13\x15\x0e\x10'    
  key = genkey(len(cipher))

  # Método 1=============================#
  print('\nMÉTODO 1\n')
  text = bytes([a ^ b for a, b in zip(cipher, key)])
  # bytes
  print(text)
  # hexadecimal
  print(text.hex())
  # utf-8
  print(text.decode())

  # Método 2=============================#
  r= []
  for x in range(len(cipher)):
    r.append(chr(int(cipher[x]) ^ int(key[x])))
  r = ''.join(r)
  print('\nMÉTODO 2\n')
  print(r)

if __name__ == '__main__':
   main()

# O operador ^ (XOR) só funciona em inteiros.

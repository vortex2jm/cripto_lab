CIPHER = b'rDFTS@OB@\x01DL\x01bNLQTU@B@N\x01\x13\x11\x13\x15\x0e\x10'

# Criando nova função para gerar chaves de 8-bits concatenadas
def new_gen_key(length: int, seed: int) -> bytes:
  return str.encode(''.join([chr(seed)*length]))

def main():
  # Testando todas as possíveis chaves de 8-bits
  for x in range(256):
    key = new_gen_key(len(CIPHER), x)
    text = bytes([a ^ b for a, b in zip(CIPHER, key)])
    xbin = bin(x)[2:].zfill(8)
    print(f'DecKey: {x}; BinKey: {xbin}; HexKey: {hex(x)}; Text: {text}')

if __name__ == '__main__':
   main()

#A mensagem descriptografada é: 'Seguranca em Computacao 2024/1' e a chave de 8 bits é 0x21

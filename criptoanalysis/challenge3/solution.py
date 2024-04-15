from example import decrypt_vigenere
import time

CIPHER1 = 'Coqebkxmk ow Mywzedkmky 2024/1'
CIPHER2 = 'Ciqybexgk oq Gyqzydemey 2024/1'
CIPHER3 = 'Cieevyxgy ik Gmwtsdeaks 2024/1'
CIPHER4 = 'Ciembeluk ce Gmezyrsmem 2024/1'

def verify(d_msg) -> bool:
  return d_msg == 'Seguranca em Computacao 2024/1'

def gen_keys_1():
  keys = []
  for x in range(65, 91):
    keys.append(chr(x))
  return keys

def gen_keys_2():
  keys = []
  for x in range(65, 91):
    for y in range(65, 91):
      keys.append(f'{chr(x)}{chr(y)}')
  return keys

def gen_keys_3():
  keys = []
  for x in range(65, 91):
    for y in range(65, 91):
      for z in range(65, 91):
        keys.append(f'{chr(x)}{chr(y)}{chr(z)}')
  return keys

def gen_keys_4():
  keys = []
  for x in range(65, 91):
    for y in range(65, 91):
      for z in range(65, 91):
        for w in range(65, 91):
          keys.append(f'{chr(x)}{chr(y)}{chr(z)}{chr(w)}')
  return keys

def main():
  start = time.time()
  for key in gen_keys_1():
    if verify(decrypt_vigenere(CIPHER1, key)):
      print(f'Key: {key}')
  end = time.time()
  print(f'Tempo para chave de 1 caracter = {end-start} segundo(s).\n')

  start = time.time()
  for key in gen_keys_2():
    if verify(decrypt_vigenere(CIPHER2, key)):
      print(f'Key: {key}')
  end = time.time()
  print(f'Tempo para chave de 2 caracteres = {end-start} segundo(s).\n')

  start = time.time()
  for key in gen_keys_3():
    if verify(decrypt_vigenere(CIPHER3, key)):
      print(f'Key: {key}')
  end = time.time()
  print(f'Tempo para chave de 3 caracteres = {end-start} segundo(s).\n')

  start = time.time()
  for key in gen_keys_4():
    if verify(decrypt_vigenere(CIPHER4, key)):
      print(f'Key: {key}')
  end = time.time()
  print(f'Tempo para chave de 4 caracteres = {end-start} segundo(s).\n')

if __name__ == '__main__':
  main()

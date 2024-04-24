from urllib.request import urlopen
import crypt

ENTRY = 'trinity:$6$neo2024$r7SohmtacsW79Zbno//eHNka5kbhY9Riw/3MH0qX8viVM7U0bfCS9sZF7gMGQoMJmuFPGsVf.BPomhLGefhfb/:17337:0:99999:7:::'
URL = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt'

hash_type = {
  '1': 'MD5',
  '2a': 'Blowfish',
  '2y': 'Blowfish',
  '5': 'SHA-256',
  '6': 'SHA-512',
  'y': 'yescrypt'
}

def main():
  entry_parts = ENTRY.split(':') 
  
  user = entry_parts[0]
  cred_parts = entry_parts[1].split('$')

  prefix = cred_parts[1]
  salt = cred_parts[2]
  hashed = cred_parts[3]

  # Imprimindo as informaçoes sobre o usuário
  print('    ===USER INFO===')
  print(f''' 
    User: {user}
    Prefix: {prefix} -> {hash_type[prefix]}
    Salt: {salt}
    Hash: {hashed}
  \n''')

  # Tornando o salt legível para a função crypt
  salt = '$'+prefix+'$'+salt+'$'

  LIST_OF_COMMON_PASSWORDS = str(urlopen(URL).read(), 'utf-8')
  
  for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashed_guess = crypt.crypt(guess, salt)
    print(hashed_guess)

    if hashed in hashed_guess:
      print(f'The password is {guess}') 
      break

if __name__ == '__main__':
  main()

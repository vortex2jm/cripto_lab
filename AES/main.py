from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_AES_ECB(key, data):
    # Instancia um objeto de cifra
    cipher = AES.new(key, AES.MODE_ECB)
    # pad garante que os blocos estarão alinhados
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return ciphertext

def decrypt_AES_ECB(key, ciphertext):
    # Instancia um objeto de cifra
    cipher = AES.new(key, AES.MODE_ECB)
    # unpad garante que os blocos estarão alinhados
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data

def main():
    while True:
        print('Digite 1 para chave aleatoria e 2 para digitar uma chave:')
        try:
            option = int(input())
        except:
            print('Type a number!\n')
            continue
        if option == 1:
            key = get_random_bytes(16)
        elif option == 2:
            while True:
                print('Digite uma chave de criptografia de 16 bytes:')
                key = str(input())
                if len(key) != 16:
                    print('A chave digitada não possui 16 bytes')
                    continue
                key = bytes(key, 'utf-8')
                break
        else:
            print('Opção inválida!')
            continue
        break

    print('Digite o texto no qual deseja criptografar:')
    data = bytes(input(), 'utf-8')  # Transforma a entrada num array de bytes
    
    # Criptografar os dados
    ciphertext = encrypt_AES_ECB(key, data)
    print('Texto criptografado:', ciphertext.hex())

    # Descriptografar os dados
    decrypted_data = decrypt_AES_ECB(key, ciphertext)
    print('\nTexto descriptografado:', decrypted_data.decode())

if __name__ == "__main__":
    main()

#O modo ECB tem algumas vulnerabilidades significativas, especialmente quando
#se trata de criptografar blocos de dados idênticos ou semelhantes, pois não
#fornece aleatorização dos blocos criptografados.

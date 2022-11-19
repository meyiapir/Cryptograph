import os

try:
    import pyAesCrypt
except ImportError:
    print("Module [pyAesCrypt] not found\nInstall this package? [y/n]")
    accept_installation = input(">>> ").strip().lower()
    if accept_installation == 'y':
        print("Installing...")
        os.system("pip install pyAesCrypt==6.0.0")
        import pyAesCrypt
    else:
        print("Exit...")
        exit()

def encrypt_aes(file: str, password: str, del_file: str = 'n'):
    try:
        print('Шифрование...\n')
        pyAesCrypt.encryptFile(file, file + ".aes", password)
        if del_file == 'y':
            os.remove(file)
        print('Готово!')
    except Exception as e:
        print(f"Error: {str(e)}")


def decrypt_aes(file: str, password: str, del_file: str = 'n'):
    try:
        print('Дешифрование...\n')
        pyAesCrypt.decryptFile(file, file[:-4], password)
        if del_file == 'y':
            os.remove(file)
        print('Готово!')
    except Exception as e:
        print(f"Error: {str(e)}")

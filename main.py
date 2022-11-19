from cryptograph.aes import encrypt_aes, decrypt_aes


def get_data():
    print('Выберите режим: \n0. Шифрование \n1. Дешифрование \n2. Выход')
    c_mode = input("# ").strip()
    print()
    file_path = input('Введите путь к файлу: ').strip()
    print()
    del_file = input("Удалять исходный файл? (y/n): ").strip().lower()
    print()
    key = input('Введите ключ: ').strip()
    return c_mode, file_path, key, del_file


def hello():
    print('''
 ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░░██████╗░██████╗░░█████╗░██████╗░██╗░░██╗
 ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░██║
 ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║██║░░██╗░██████╔╝███████║██████╔╝███████║
 ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║██║░░╚██╗██╔══██╗██╔══██║██╔═══╝░██╔══██║
 ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░░░░░██║░░██║
 ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝
\n\n''')


def main():
    hello()

    while True:
        try:
            c_mode, file_path, key, del_file = get_data()
            print('-' * 50 + '\n')
            if c_mode == '0':
                encrypt_aes(file_path, key, del_file)
            elif c_mode == '1':
                decrypt_aes(file_path, key, del_file)
            elif c_mode == '2':
                print('Выход...')
                exit()
            else:
                print('Error: Неверный режим')
            print()
            print("=" * 50)
        except ValueError:
            print('Error: Невозможно прочитать файл.')
        except Exception as e:
            print(f'Error: {str(e)}')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
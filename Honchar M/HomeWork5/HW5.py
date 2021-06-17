# Реализуйте шифратор и дешифратор по шифру Цезаря.
# Спросить пользователя, что он хочет сделать - зашифровать или расшифровать
# файл.
# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла,
# который мы получим на выходе(зашифрованного) и ключ(ключем будет уроваень
# сдвига).
# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на
# выходе(расшифрованного) и ключ.
#
import string


# Генератор для розбору файлу порядково
def read_file(namefile):
    with open(namefile, 'r', encoding='UTF-8') as file:
        for line in file:
            yield line


# Функція для шифрування файлів порядково
def encrypt_line(line, key_e):
    # Читаємо рядки у циклі, отримані від генератора
    alphabet = string.ascii_letters * 2
    string_to_encrypt = line
    shift_amount = key_e
    encrypted_string = ""
    for currentCharacter in string_to_encrypt:
        position = alphabet.find(currentCharacter)
        new_position = position + shift_amount
        if currentCharacter in alphabet:
            encrypted_string = encrypted_string + alphabet[new_position]
        else:
            encrypted_string = encrypted_string + currentCharacter
    return encrypted_string


def write_line_to_file(namefile, line):
    with open(namefile, 'a', encoding='UTF-8') as file:
        file.write(line)


#  Запитуємо користувача про намір зашифрувати чи розшифрувати файл
user_request =\
    (input(f"Are you have encrypt or descrypt file?\n"
           f"Please enter 'e' if 'encrypt' or 'd' if 'descrypt' >>>")).lower()
#  Якщо користувач підтвердив намір зашифрувати файл
if user_request == 'e':
    #  Запитуємо його ім'я файлу що шифрується
    filename_e_request =\
        input("Please enter file name was encrypt  >>").lower()
    # Запитуємо користувача ім'я вихідного файлу після шифрування
    filename_oe_request =\
        (input("Please enter output file name after encryption >>")).lower()
    #  Запитуємо ключ шифрування(зміщення)
    key_request = int(input("Please enter encrypt key (only int number) >>"))
    # виконуємо кодування порядково у циклі
    for line in read_file(filename_e_request):
        write_line_to_file(filename_oe_request,
                           encrypt_line(line, key_request))

elif user_request == 'd':
    # Питаємо користувача ім'я файлу для розшифрування
    filename_d_request =\
        (input("Please enter descrypted file name >>")).lower()
    # Питаємо користувача ім'я вихідного файлу після розшифрування
    filename_od_request =\
        (input("Please enter output file name after descryption >>")).lower()
    #  Запитуємо ключ розшифрування(зміщення)
    key_o_request =\
        int(input("Please enter key for descrypt (only int number) >>"))
    # виконуємо розшифрування порядково у циклі
    for line in read_file(filename_d_request):
        write_line_to_file(filename_od_request,
                           encrypt_line(line, -key_o_request))

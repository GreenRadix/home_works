#
# *************************ЗАДАЧА №6******************************
# Есть два файла whitelist.txt и blacklist.txt, наполните их именами и
# фамилиями пользователей.
#
# 1. Попросить пользователя ввести имя и фамилию;
# 2. Если имени нет в черном и белом списках, тогда добавить пользователя в
# whitelist.txt и вывести приветствие;
# 3. Если имя есть в белом списке, вывести приветствие;
# 4. Если имя в черном списке, тогда вывести сообщение, что имя в блоке.
# 5. Результат не должен зависеть от регистра введеных слов (строковые
# литералы).
#
f_name = str(input("Input your surname and name, please! ").title())
with open('whitelist.txt', 'r+', encoding='UTF-8') as file1,\
        open('blacklist.txt', 'r+', encoding='UTF-8') as file2:
    bl_list = str(file2.readlines()).find(f_name)
    wl_list = str(file1.readlines()).find(f_name)
    if -1 < bl_list:
        print(f"Access Denied! Your name {f_name} is blocked!")
    elif -1 < wl_list:
        print(f"Hello! Welcome to Enterprise Web {f_name}!")
    else:
        file1.write(f_name)
        print(f"Hello, {f_name}! Your name added to whitelist our"
              f" database! Access allowed!")

# *************************ЗАДАЧА №7******************************
# 1. Прочитать содержимое файлов whitelist.txt и blacklist.txt;
# 2. Сделать вывод не на экран, а в новый файл
# Вывод должен выглядеть так:
# 	Имя
# ХХХХХХХХХХХХХХХХХХХХ
# 	Имя
# ХХХХХХХХХХХХХХХХХХХХ
# 	...
#     Print Finished
with open('whitelist.txt', 'r+', encoding='UTF-8') as file1, \
        open('blacklist.txt', 'r+', encoding='UTF-8') as file2, \
        open('new_file2.txt', 'w', encoding='UTF-8') as file3:
    merge_list1 = list(file1.readlines())
    merge_list2 = list(file2.readlines())
    merge_list = merge_list1 + merge_list2
    print(*merge_list, sep='XXXXXXXXXXXXXXXXXXXXXX\n',
          end='Print Finished', file=file3)

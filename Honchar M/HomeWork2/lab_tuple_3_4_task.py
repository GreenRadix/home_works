#***************************ЗАДАЧА №3*****************************
# 1. Открыть тот же файл и перезаписать его содержимое на эту же строку в обратном порядке (задом на перед).
#
name = input("Input your name, please! ")
last_name = input("Input your lastname, please! ")
age = input("Input your age, please! ")
with open('new_file.txt', 'w+', encoding='UTF-8') as file:
    file.write(f'{name} {last_name} - {age}')
    file.seek(0)
    new_data = file.read()
    file.seek(0)
    file.write(new_data[::-1])


# *************************ЗАДАЧА №4******************************
# Содержимое файл:
#
# Рудковский К.
# Иванов О.
# Петров И.
# Дмитриев Н.
# Смирнова О.
# Керченских В.
# Котов Д.
# Иванов О.
# Бирюкова Н.
# Данилов П.
# Аранских В.
# Лемонов Ю.
# Олегова К.
# Данилов П.
# Смирнова О.
# Керченских В.
# Петров И.
# Стадкевич О.
# Васюченко А.
# Рудковский К.
# Пацук И.
#
# 1. Считать данные с файла и сохранить только уникальные значения;
with open('list_worker.txt', 'r', encoding= 'UTF-8') as file1, open('list_worker_res.txt', 'w', encoding= 'UTF-8') as file2:
    worker_name = list(file1.readlines())
    file1.seek(0)
    worker_name = list(set(worker_name))
    # 2. Записать их в новый файл в алфавитном порядке (каждый элемент в новой строке).
    worker_name.sort()
    # worker_name = sorted(worker_name) #Ще один варіант сортування
    file2.seek(0)
    file2.writelines(worker_name)
# *************************ЗАДАЧА №1******************************
# Реализовать алгоритм пузырьковой сортировки.
#
import random
from random  import randint

def buble_sort(your_list):
    permutation = 1
    while permutation > 0:
        permutation = 0
        for i in range(0, len(your_list) - 1):
            if your_list[i] > your_list[i + 1]:
                your_list[i], your_list[i + 1] = your_list[i + 1], your_list[i]
                permutation += 1
    return your_list

# generate random list value var.1
list_apl = list(range(16, 82, 3))
apl = random.sample(list_apl, 15)
print("Unsorted value list", apl)

# generate random list value var.2
n = 25
list_apl2 = []
for i in range(n):
    list_apl2.append(randint(0, 500))
print("Unsorted value list:\n", list_apl2)

# bubble sort algo realized through the function:
print("Sorted value list: ", buble_sort(apl))
print("Sorted value list: ", buble_sort(list_apl2))

# *************************ЗАДАЧА №2******************************
# Написать программу которая просит у пользователя ввести его любимое число.
# Если ввод число, тогда поблагодорить пользователя за сотрудничество и завершить программу.
# Если ввод не число, тогда попросить его быть более внимательным и ввести именно число.
# Если неправильный ввод более 3 раз, перейти на более грубое предупреждение.
# Если неправильный ввод более 5 раз, дать пользователю последний шанс.
# Если ввод по прежнему не число, тогда обругать пользователя и завершить программу.
#

def number_request_audit():
    try:
        number = int(input("Enter a number which you like!  "))
        aud = isinstance(number, int)
        print("Thank you for co-working!")
        return aud
    except ValueError:
        print("What you entered is not a number")


i = 3
while i > 0:
    if number_request_audit():
        break
    else:
        print("You have try: ", i-1)
        i -= 1
else:
    print("Are you seriously so boom? I say to you: only a number! Let's try again!")
    j = 5
    while j > 0:
        if number_request_audit():
            break
        else:
            print("You have try: ", j-1)
            j -= 1
    else:
        print("You have the last chance!")
        if number_request_audit():
            print("At last!!")
        else:
            print("You are stupid donkey! Fuck off!")
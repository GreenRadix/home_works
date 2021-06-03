# Создать эмуляцию системы входа и регистрации для пользователей.
# При запуске программы, пользователя должно спросить проходил ли он
# регистрацию на нашем ресурсе, если да, тогда предложить ему ввести логи
# и пароль от его учетной записи.
# Если данные верны вывести сообщение об успешном входе в систему, если нет
# тогда сообщить об этом.
# Если пользователь не регистрировался на ресурсе, тогда спросить не желает
# ли он пройти регистрацию.
# Если желает, взять от него необходимые данные и вывести об успешной
# регистрации, если не желает регистрироватся - пожелать удачи.
# Данные о зарегестрированных пользователях хранить в файле 'users.txt',
# по желанию можете создать файл для логирования событий регистрации
# и входа.

from datetime import datetime
# Робимо усе гарнюньо з датою та часом)
log_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#  відкриваємо файл де зберігаються логіни:паролі користувачів системи
with open('users.txt', 'r', encoding='UTF-8') as file:
    user_dict = {}  # створюємо пустий словник для наповнення його
#  елементами файлу(у якому рядки розміщені у форматі key:value)
    for line in file:  # цикл поки лінії у відкритому файлі не закінчаться
        key, value = line.strip().split(':')  # рядок обрізаємо по краям і
        # розділяємо двокрапкою на частини key:value і розміщуємо елементи
        # в них відповідно до індексу(розпаковуємо рядок)
        user_dict[key] = value  # додаємо елементи до словника в циклі

#  Відкриваємо файл логування подій в режимі append
log_file = open("log.txt", 'a')

#  Запрос до користувача нанаявність обліковки в системі
user_request = (input(f"Are you have registration on our resource?\n"
                f"Please enter 'Y' if 'Yes' or 'N' if 'No' >>>>")).title()
log_file.write(f"{log_date_time} System: Are you have registration on our"
               f" resource? Please enter 'Y' if 'Yes' or 'N' if 'No' >>>>\n")

#  Якщо користувач підтвердив наявність обліковки
if user_request == 'Y':
    log_file.write(f"{log_date_time} User: {user_request}\n")

    login_request = None
    pass_request = None
    #  Запитуємо його логін у циклі доки не посиніє
    while login_request not in user_dict.keys():

        #  Запитуємо його логін
        login_request = input("Please enter your login >>>>")
        log_file.write(f"{log_date_time} System: Please enter your login >>>> \n")
        log_file.write(f"{log_date_time} User: {login_request} \n")

        #  Запитуємо його пароль
        pass_request = input("Please enter your password >>>>")
        log_file.write(f"{log_date_time} System: Please enter "
                       f" your password >>>> \n")
        log_file.write(f"{log_date_time} User: {pass_request} \n")

        # Тут проводимо перевірку чи існує такий логін у системі
        if login_request in user_dict.keys():

            # І якщо існує - перевіряємо відповідність паролю введеному логіну
            if pass_request == user_dict.get(login_request):
                # І якщо усе ОК, весело відкриваємо перед користувачем двері
                # у систему й наливаємо чаю с кальвадосом
                print(f"Success! Access allowed! Welcome on our resource"
                      f" {login_request}!")
                log_file.write(f"{log_date_time} System: Success! Access allowed!"
                               f" Welcome on our resource{login_request}!\n")
            else:
                # Якщо ж пароль не вгадав, зажурливо махаємо хустинкою
                # і йдемо пити чай з кальвадосом самі)
                print(f"Your password is incorrect!")
                log_file.write(f"{log_date_time} System:"
                               f" Your password is incorrect!\n")

        else:  # Ага! Хтось нас хотів нахитати з наскоку,
            # але ми й не таких завертали
            print(f"Your login {login_request} is absent in system!")
            log_file.write(f"{log_date_time} System: Your login {login_request} "
                           f"is absent in system!\n")

# якщо користувач відповів, що ще не зареєстрований у системі
elif user_request == 'N':
    log_file.write(f"{log_date_time} User: {user_request}\n")
    # питаємо, чи не хоче він зареєструватись?
    reg_request = (input("Do you want to register on our resource?"
                         " Enter 'Y' if 'Yes' or 'N' if 'No' >>>>")).title()
    log_file.write(f"{log_date_time} System: Do you want to register on our"
                   f" resource? Enter 'Y' if 'Yes' or 'N' if 'No' >>>>\n")

    # якщо бажання реєструватись ще не відпало і він погоджується, то просимо
    # ввести логін/пароль, які користувач бажає
    if reg_request == 'Y':
        log_file.write(f"{log_date_time} User: {reg_request}\n")
        login_new = input("Please enter login you want >>>>")
        log_file.write(f"{log_date_time} System: Please enter"
                       f" login you want >>>>\n")
        log_file.write(f"{log_date_time} User: {login_new}\n")

        pass_new = input("Please enter password you want >>>>")
        log_file.write(f"{log_date_time} System: Please enter password"
                       f" you want >>>>\n")
        log_file.write(f"{log_date_time} User: {pass_new}\n")

        print(f"You enter login: {login_new}, and password: {pass_new}.")
        log_file.write(
            f"{log_date_time} System: You enter login: {login_new},"
            f" and password: {pass_new}.\n")

        # Тут проводимо перевірку на існування введеного логіну в базі системи
        # Якщо такий логін вже є посилаємо подумати над логіном ще
        # з чаєм і кальвадосом для наснаги
        if login_new in user_dict.keys():
            print("Please choose other login. Such a login already"
                  " exists in the system!")
            log_file.write(f"{log_date_time} System: Please choose other"
                           f" login. Such a login already exists"
                           f" in the system!\n")
        else:
            # Якщо таки користувач вже приложив голову і придумав щось
            # аутентичне - хвалимо, хлопаємо по плечу. І кажемо, щоб заходив
            # якось наступного разу... але вже з дверей.
            print("Your login and password have been successfully stored"
                  " in the system.\nPlease use it to log in next time!")
            log_file.write(f"{log_date_time} System: Your login and password"
                           f" have been successfully stored in the system.\n"
                           f"Please use it to log in next time!\n")

            with open('users.txt', 'a', encoding='UTF-8') as file1:
                file1.write(f'{login_new}:{pass_new}')

    # якщо бажання реєструватись у користувача такі відпало
    elif reg_request == 'N':
        log_file.write(f"{log_date_time} User: {reg_request}\n")
        # бажаємо йому на щастя, на здоров'я і йдемо піднімати тонус
        # з чаєм і кальвадосом
        print("Good luck!")
        log_file.write(f"{log_date_time} System: Good luck!\n")
    else:
        # Бідкаємося, що у користувача ручки ростуть не з плечей, і він
        # невтьопки натиснути декілька клавіш, які саме його просять
        print("Sorry, but you didn't enter 'Y' if 'Yes' or 'N' if 'No'")
else:
    # Так само бідкаємося але вже на глобальному програмному рівні,
    # штибу: ''мая твоя не понімать''. Пересмикни програму, бо я вже від
    # тебе висю зі сміху...
    print("Sorry, but you din't enter anythyng.\n "
          "Or is not clear what you entered:(\n "
          "Please restart program and"
          " retry enter 'Y' if 'Yes' or 'N' if 'No'!")
# от і казочці кінець,
# хто дочитав той молодець!
# Закриваємо файл логування подій.
log_file.close()

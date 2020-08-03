def inf_func(name, surname, year, city, email, phone):
    result = name + ' ' + surname + ' ' + year + ' ' + city + ' ' + email + ' ' + phone
    return result


user_name = input("Введите ваше имя ")
user_surname = input("Введите вашу фамилию ")
user_year = input("Введите ваш год рождния ")
user_city = input("Введите ваш город проживания ")
user_email = input("Введите ваш email ")
user_phone = input("Введите ваш номер телефона ")
print(inf_func(user_name, user_surname, user_year, user_city, user_email, user_phone))

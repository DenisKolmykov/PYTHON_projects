"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.

Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
from datetime import datetime


def user_data(first_name, last_name, birthdate, city, email, tel):
    print(
        f'{first_name} {last_name} {birthdate} года рождения, '
        f'проживает в городе {city}, email: {email}, телефон: {tel}')


try:
    fn = input('Введите свое имя: ')
    ln = input('Введите фамилию: ')
    bd = int(input('Введите год рождения: '))
    c = input('Введите город проживания: ')
    em = input('Введите адрес электронной почты: ')
    t = input('Введите номер телефона: ')

    user_data(first_name=fn, last_name=ln, birthdate=bd, city=c, email=em,
              tel=t)

except ValueError:
    print('Вы попытались ввести некооректный тип данных')

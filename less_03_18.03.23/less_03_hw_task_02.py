"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def divide_nums(num_1, num_2):
    try:
        div = num_1 / num_2
    except ZeroDivisionError:
        print('Вы пытаетесь делить на ноль !!!')
        return
    return div


n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))

res = divide_nums(n, k)
if res is not None:
    print(res)

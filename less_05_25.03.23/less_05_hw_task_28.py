"""
Задача 28:
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

"""


def nums_input(count):
    try:
        num = int(input(f'Введите {count}-е число: '))
    except ValueError:
        print('! Вы ввели не число или не целое число! Повторите ввод.')
        return nums_input(count)
    return num


def sum_a_b(num1, num2, summa=0):
    if num1 > 0:
        return sum_a_b(num1 - 1, num2, summa + 1)
    if num2 > 0:
        return sum_a_b(num1, num2 - 1, summa + 1)
    return summa


a = nums_input(1)
b = nums_input(2)

print(f'Сумма чисел "{a}" и "{b}" -> {sum_a_b(a, b)}')

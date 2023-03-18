"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    sum_maxis = nums[1] + nums[2]
    # print(f'Наибольшие числа: {nums[1]} и {nums[2]}')
    return sum_maxis


def my_func(num1, num2, num3):
    max1, max2 = num1, num2
    if num1 >= num2:
        max1, max2 = num2, num1
    if num2 <= num3:
        max1, max2 = max2, num3
    sum_maxis = max1 + max2
    # print(f'Наибольшие числа: {max1} и {max2}')
    return sum_maxis


n1 = float(input('Введите первое число: '))
n2 = float(input('Введите второе число: '))
n3 = float(input('Введите третье число: '))

# #либо ввоод в одну строку через пробел:
# #тогда можно было бы и перердавать в функцию сразу весь массив
# #(но в задании: "три позиционных аргумента")
# nums = list(input(f'Введите три числа через пробел: ').split(' '))
# n1 = float(nums[0])
# n2 = float(nums[1])
# n3 = float(nums[2])
print()

print('1. С использованием функции sort():')
sum_two_max_num = my_func_sort(n1, n2, n3)
print(f'Сумма наибольших двух чисел равна: {sum_two_max_num}\n')

print('2. Без использования функции sort():')
sum_two_max_num = my_func(n1, n2, n3)
print(f'Сумма наибольших двух чисел равна: {sum_two_max_num}\n')

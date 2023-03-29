"""
Задача 32:
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random

n = 15
fill_array = [random.randint(-100, 100) for i in range(0, n)]
print(fill_array)
min_elem = int(
    input('Введите min значение элемента (в диапазоне от -100 до 100): '))
max_elem = int(
    input('Введите max значение элемента (в диапазоне от -100 до 100) '))

res_list = [i for i in fill_array if min_elem <= i <= max_elem]
res_list_index = [j for j in range(len(fill_array)) if
                  min_elem <= fill_array[j] <= max_elem]
print(res_list)
print(res_list_index)

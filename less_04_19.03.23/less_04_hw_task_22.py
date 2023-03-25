"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.

"""

"""
# вар.1 ввод элементов множества сразу с проверкой на повторы
# --------------------
def fill_set(len):
    print(f'Введите {len} элементов множества:')
    set_len = set()
    i = 0
    while i < len:
        num_input = float(input(f'Введите {i+1}/{len} элемент: '))
        if num_input in set_len:
            print('Такой элемент ранее был уже добавлен. Введите заново..')
        else:
            set_len.add(num_input)
            i += 1
    print()
    return set_len


list_lens = list(input(f'Введите через пробел размеры 2x множеств: ')
                 .split(' '))
set_n = fill_set(int(list_lens[0]))
set_m = fill_set(int(list_lens[1]))

print(f'Вы ввели первое множество: {set_n}')
print(f'Вы ввели второе множество: {set_m}')
print(f'Элементы, которые присутствуют в обоих множествах: {set_n.union(set_m).sort()}')
# --------------------
"""

# вар.2 (вводим элементы списка, в т.ч. повторы)
# --------------------
def fill_list(len):
    print(f'Введите {len} элементов списка:')
    list_len = []
    i = 0
    while i < len:
        num_input = float(input(f'Введите {i+1}/{len} элемент : '))
        # a = [int(x) for x in input().split()] # ввод из эталонного решения
        # k = set(a)
        list_len.append(num_input)
        i += 1
    print()
    return list_len


list_lens = list(input(f'Введите через пробел размеры 2x множеств: ')
                 .split(' '))
list_n = fill_list(int(list_lens[0])) # создаем переменную исключительно для вывода
set_n = set(list_n)
list_m = fill_list(int(list_lens[1]))
set_m = set(list_m)

print(f'Первый список: {list_n}')
print(f'Второй список: {list_m}\n')
print(f'Элементы, которые присутствуют в обоих списках: {set_n.union(set_m).sort()}')

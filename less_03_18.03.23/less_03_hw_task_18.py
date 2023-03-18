"""
Задача 18:
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X.
Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X
"""

n = int(input('Введите количество элементов массива: '))
a_i = list(input(f'Введите {n} значений элементов массива через пробел: ')
           .split(' '))
find_num = input(
    'Введите значение Х для поиска ближайшего к нему по значению элемента в массиве: ')
print()

# вар.1 через словарь "разностей"
# (с возможностью вывода всех ближайших элементов (если расстояние от них до Х одинаковое)
print('вар.1 через словарь "разностей"')
dict_diff = {}
for i in a_i:
    # ключ - разность от элемента исходного массива до Х
    diff = abs(float(i) - float(find_num))
    temp = []
    if diff not in dict_diff.keys():
        temp.append(a_i.index(
            i))  # значение словаря - индекс элемента исходного массива
        dict_diff[diff] = temp
    else:
        temp = list(dict_diff[diff])
        temp.append(a_i.index(i))
        dict_diff[diff] = temp

index_min_diff_x = dict_diff[
    min(dict_diff.keys())]  # минимальное значение ключа - ближайшее растояние до Х
# в этом ключе "лежат" индексы исходного массива, значения по которым наиболее близки к Х
res = list(a_i[i] for i in index_min_diff_x)
print(f"В массиве {a_i} ближайший(ие) элемент(ы) к '{find_num}'")
print("имее(ю)т значение(я): " + ', '.join(
    map(str, res)) + " . С индексом(ами) в исходном массиве: " + ', '.join(
    map(str, index_min_diff_x)))

print()
#----------

# вар.2 бинарный поиск (учитывая что сортируем массив (для бинарного поиска),
# можно, но не стал реализовывать "фиксацию" индексов исходного массива
# и проверку на повторы в массиве
print('вар.2 бинарный поиск')

a_i_copy = a_i.copy()
a_i_copy.sort()

res_index = []
if a_i_copy[-1] <= find_num:
    res_index.append(len(a_i_copy) - 1)
elif a_i_copy[0] >= find_num:
    res_index.append(0)
else:  # если искомое значение "внутри" значений массива - запускаем поиск
    j = 0
    k = len(a_i_copy) - 1
    while j <= k and (j + k // 2) < len(a_i_copy):
# почему то, если искомое значение во второй половине массива
# И одинаковое расстояние "вправо и влево" - то выдает только одно (элемент с большим значением)...
# если изменить сердину на middle = j + (k-1) // 2, то наооборот - в первой половине перестает выдавать второе значение
        middle = j + k // 2  # находим середину массива
        if a_i_copy[middle] == find_num:
            res_index.append(middle)
            j = k + 1
        elif a_i_copy[middle] < find_num:
            j = middle + 1
        elif a_i_copy[middle] > find_num:
            k = middle - 1

    if len(res_index) == 0: # если ближайший элемент не был найден (a_i[middle] == find_num)
        # находим минимальную разницу (ближайший элемент)
        diff_1 = abs(float(a_i_copy[j]) - float(find_num))
        diff_2 = abs(float(a_i_copy[k]) - float(find_num))
        if diff_1 == diff_2:
            res_index.append(j)  # можно сразу значение, но решил через индекс...
            res_index.append(k)
        elif diff_1 > diff_2:
            res_index.append(k)
        else:
            res_index.append(j)

res = list(a_i_copy[i] for i in res_index)
print(f"В массиве {a_i} ближайший(ие) элемент(ы) к '{find_num}'")
print("имее(ю)т значение(я): " + ', '.join(map(str, res)))

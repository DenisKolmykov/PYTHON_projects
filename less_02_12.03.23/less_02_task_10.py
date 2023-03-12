"""
Задача 10:
На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

"""
# вар.1 (через случайную генерацию)
import random

print("вар.1 (через случайную генерацию)")
n = int(input('Введите количество монет: '))
obverse = random.randint(1, n - 1)
reverse = n - obverse
print(f"На столе лежит {n} монет: {obverse} - решкой, {reverse} - гербом")
if obverse > reverse:
    flip = reverse
else:
    flip = obverse
print(f"Необходимо перевернуть: {flip}")
print()

# вар.2 (через ввод каждого вида монет)
print("вар.2 (через ввод каждого вида монет)")
m = int(input('Введите количество монет: '))
obverse_count = 0
reverse_count = 0
for i in range(m):
    temp = int(
        input(f"Укажите какой стороной лежит {i + 1}-я монета (0 или 1): "))
    if temp == 0:
        obverse_count += 1
    else:
        reverse_count += 1
print(f"На столе лежит {m} монет: {obverse_count} - решкой, {reverse_count} - гербом")
if obverse_count > reverse_count:
    turn = reverse_count
else:
    turn = obverse_count
print(f"Необходимо перевернуть: {turn}")

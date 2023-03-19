"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом,собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
"""

n = int(input('Введите количество кустов (N) на грядке: '))
berry = list()
for i in range(n):
    berry.append(int(input(f'Введите количество ягод на {i + 1}/{n} кусте: ')))

count_berry = list()
i = 0
count_berry.append(berry[-1] + berry[-2] + berry[0])
while i < n - 1:
    count_berry.append(berry[i] + berry[i - 1] + berry[i + 1])
    i += 1
res = max(count_berry)
print(f'Наибольшее количество ягод собранных с соседних трех кустов = {res}')

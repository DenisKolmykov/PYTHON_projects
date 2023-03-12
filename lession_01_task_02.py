"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

s = int(input('Введите время в секундах: '))

# вывод как в примере
m = s / 60
h = s / 3600
print(f"Время в формате ч:м:с - {round(h, 1)} : {round(m, 1)} : {s}")

# реальный перевод количества секунд в часы:минуты:секунды
ss = int((s % 3600) % 60)
mm = int(((s - ss) % 3600) / 60)
hh = int((s - mm * 60 - ss) / 3600)
print(f"{s} секунд - это: {hh:02} : {mm:02} : {ss:02}")

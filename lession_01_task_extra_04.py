"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""

# в задаче не уточнено,
# но можно и через s = int(input('Введите общее количество поделок: ')
s = 60

p = c = k = 0
k = 2 * s // 3  # 3*k = 2*s
p = c = s // 6  # p + c = s/3
print(f"Bсего ребята сделали {s} поделок.")
print(f"Петя сделал {p}, Катя сделала {k}, Сережа сделал {c}")


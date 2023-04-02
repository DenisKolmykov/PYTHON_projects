"""
Задание 4.
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, rows_list):
        self.data = rows_list

    def __str__(self):
        for r in range(0, len(self.data)):
            for c in range(0, len(self.data[r])):
                print(self.data[r][c], end=' ')
            print()
        return ''

    def __add__(self, other):
        print('Сумма двух матриц:')
        sum_matrix = []
        for r in range(0, len(self.data)):
            if len(self.data[r]) != len(other.data[r]):
                return 'Сумма матриц не возможна, т.к. матрицы разноразмерные'
            else:
                row_matrix = []
                for c in range(0, len(self.data[r])):
                    row_matrix.append(self.data[r][c] + other.data[r][c])
                sum_matrix.append(row_matrix)
        return Matrix(sum_matrix)


obj_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
obj_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print('Матрица №1:')
print(obj_1)
print('Матрица №2:')
print(obj_2)

res_matrix = obj_1 + obj_2
print(res_matrix)

print('---------------')

obj_3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
obj_4 = Matrix([[1, 1], [1, 1], [1, 1]])
print('Матрица №3:')
print(obj_3)
print('Матрица №4:')
print(obj_4)

res_matrix = obj_3 + obj_4
print(res_matrix)

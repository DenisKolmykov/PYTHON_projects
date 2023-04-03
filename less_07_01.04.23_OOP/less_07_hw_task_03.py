"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

    def __str__(self):
        return f'------\nимя: {self.name}\nфамилия: {self.surname}' \
               f'\nдолжность: {self.position}\nоклад: {self.__income["wage"]}' \
               f'\nпремия: {self.__income["bonus"]}\n------'


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.wage = wage
        self.bonus = bonus
        self.__income = {'wage': self.wage, 'bonus': self.bonus}
        #self.__income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'общий доход = {self.__income["wage"] + self.__income["bonus"]}'


person_1 = Position('Иван', 'Иванов', 'директор', 100, 200)
person_2 = Position('Сергей', 'Сергеев', 'рабочий', 1, 2)

print(f'{person_1.get_full_name()}, '
      f'{person_1.position}: '
      f'{person_1.get_total_income()}')
print(person_1)

print(f'{person_2.name} {person_2.surname}, '
      f'{person_2.position}: '
      f'{person_2.get_total_income()} '
      f'(оклад= {person_2.wage} + премия= {person_2.bonus})')
print(person_2)

"""
реализовать дескрипторы для любых двух классов
"""


class Verification_param:

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("!Вводимое значение должно быть больше нуля!")
        instance.__dict__[self.road_param] = value

    def __set_name__(self, owner, road_param):
        self.road_param = road_param


class Thick_is_in_metr:

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("!Вводимое значение должно быть больше нуля!")
        if value > 0.1:
            raise ValueError("!Вы пытаетесь ввести значение в сантиметрах!")

        instance.__dict__[self.road_param] = value

    def __set_name__(self, owner, thick):
        self.thick = thick


class Road:
    mass_1kwm = 25
    # thick = 0.05
    length = Verification_param()
    width = Verification_param()
    thick = Thick_is_in_metr()

    def __init__(self, length, width, thick):
        self.length = length
        self.width = width
        self.thick = thick

    def mass(self):
        res_mass = self.length * self.width * self.mass_1kwm * self.thick
        return res_mass

    def __str__(self):
        return f'масса асфальта при длине дороги = {self.length}м,' \
               f'шириной {self.width}м = {self.mass()} кг = {self.mass() / 1000}тн' \
               f'\nпри весе 1 м2 асфальта толщиной 1см = {self.mass_1kwm}кг' \
               f'\nи толщине асфальтового покрытия = {self.thick}м'


length = float(input('Введите длину дороги: '))
width = float(input('Введите ширину дороги: '))
thick = float(input('Введите толщину слоя в м (от 0.01 до 0.1): '))

road_1 = Road(length, width, thick)
print('Дорога №1')
print(road_1)

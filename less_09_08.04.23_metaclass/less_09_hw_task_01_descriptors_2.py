import time


class Verification:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("!Вводимое значение должно быть больше нуля!")
        instance.__dict__[self.atribut] = value

    def __set_name__(self, owner, atribut):
        self.atribut = atribut


class TrafficLight:
    _color = {'red': 7, 'yellow': 2, 'green': 5}
    count = Verification()

    def __init__(self, count):
        self.count = count

    def running(self):
        c = 1
        while c <= self.count:
            print(f'начало {c}/{self.count} цикла работы светофора:')
            for key, value in self._color.items():
                # print(key)
                for i in range(value, 0, -1):
                    print(f'\r{key}: {i}', end='')
                    time.sleep(1)
                # time.sleep(value)
            print()
            print(f'{c}-й цикл работы завершен\n')
            c += 1


count = int(input('Введите количество циклов работы светофора: '))
tl = TrafficLight(count)
tl.running()

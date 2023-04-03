"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет)
и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:

    def __init__(self, count):
        self._color = {'red': 7, 'yellow': 2, 'green': 5}
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


count = 2
tl = TrafficLight(count)
tl.running()

"""
реализовать метакласс. позволяющий создавать всегда один и тот же объект класса
"""


class TypeMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.class_obj = None

    def __call__(cls, *args, **kwargs):
        if cls.class_obj is None:
            cls.class_obj = super().__call__(*args, **kwargs)
        return cls.class_obj


class SomeClass(metaclass=TypeMeta):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summa(self):
        return self.a + self.b

    def multy(self):
        return self.a * self.b


n = 5
m = 6
obj_1 = SomeClass(n, m)

k = 8
p = 10
obj_2 = SomeClass(k, p)

print(f'obj_1 is obj_2 : {obj_1 is obj_2}')

print(f'n = {n}, m = {m} --> in obj_1:  n = {obj_1.a}, m = {obj_1.b}')
print(f'k = {k}, p = {p} --> in obj_2:  k = {obj_2.a}, p = {obj_2.b}')

print(f'in obj_1: summ_1 = {obj_1.summa()}, mul_1 = {obj_1.multy()}')
print(f'in obj_2: summ_2 = {obj_2.summa()}, mul_2 = {obj_2.multy()}')

print(f'type of obj_1 --> {type(obj_1)}, '
      f'metaclass of obj_1 --> {obj_1.__class__.__class__}')
print(f'type of obj_2 --> {type(obj_2)}, '
      f'metaclass of obj_2 --> {obj_2.__class__.__class__}')
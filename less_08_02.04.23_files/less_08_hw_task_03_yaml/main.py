"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml
import os

data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
        'items_quantity': 4,
        'items_price': {'computer': '100€-2000€',
                        'keyboard': '1€-10€',
                        'mouse': '2€-5€',
                        'printer': '200€-500€'}}

with open('file_2.yaml', 'w') as file_data:
    yaml.dump(data, file_data,
              default_flow_style=False, allow_unicode=True)

directory = os.getcwd()  # получаем путь текущей директории
for filename in os.listdir(directory):
    if filename.endswith('.yaml'):
        with open(filename) as f:
            r_data = yaml.load(f, Loader=yaml.FullLoader)
            if r_data == data:
                print(f'данные из файла {filename} '
                      f'совпадают с исходными данными')
            else:
                print(f'!!! данные из файла {filename} '
                      f'НЕ СОВПАДАЮТ с исходными данными !!!')
            for k, v in r_data.items():
                print(k, ":", v)
            print('')

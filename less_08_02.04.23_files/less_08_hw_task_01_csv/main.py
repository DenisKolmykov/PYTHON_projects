"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import os
import re
import csv


def get_data():
    os_prod_list = list()
    os_name_list = list()
    os_code_list = list()
    os_type_list = list()
    main_data_list = list()
    count = 0  # для заполнения столбца "№п/п"

    directory = os.getcwd()  # получаем путь текущей директории
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            # файлы находит сначала №3, потом №2, затем №1
            # print(filename) # для проверки
            # file_name_list.insert(0, filename) # если необходимо еще гдето файлы использовать
            # и тогда с ними работать в отдельном цикле: for i in range(0, len(file_name_list)):
            try:
                with open(filename, 'r', encoding='windows-1251') as f:
                    data = f.read()

                    os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*.*')
                    os_prod_list.append(
                        os_prod_reg.findall(data)[0].split(':')[1].lstrip())

                    os_name = re.compile(r'Название ОС:\s*\S*.*')
                    os_name_list.append(
                        os_name.findall(data)[0].split(':')[1].lstrip())

                    os_code = re.compile(r'Код продукта:\s*\S*.*')
                    os_code_list.append(
                        os_code.findall(data)[0].split(':')[1].lstrip())

                    os_type = re.compile(r'Тип системы:\s*\S*.*')
                    os_type_list.append(
                        os_type.findall(data)[0].split(':')[1].lstrip())
                    # не совсем понятно - зачем формировать списки os_prod_list, os_name_list и тд
                    # на мой взгляд, в ситуации выше можно было обойтись соответствующими переменными
                    # которые использовать для добавления в список ниже (main_data_list)
                    # и которые на каждом шаге цикла можно было бы "перезаписывать" новыми значениями...
                    # но... в задании указано - сформировать списки - значит формируем....

                    main_data_list.append(
                        {'№п/п': count + 1,
                         'Изготовитель системы': os_prod_list[count],
                         'Название ОС': os_name_list[count],
                         'Код продукта': os_code_list[count],
                         'Тип системы': os_type_list[count]})
                    count += 1

            except IOError:
                print("Ошибка ввода-вывода")

    # print(os_prod_list) # для проверки
    # print(os_name_list) # для проверки
    # print(os_code_list) # для проверки
    # print(os_type_list) # для проверки
    # print(main_data_list) # для проверки
    # print(file_name_list) # для проверки
    return main_data_list


def write_to_csv():
    with open('result_data.csv', 'w') as result_file:
        data = get_data()
        res_data_write = csv.DictWriter(result_file,
                                        fieldnames=list(data[0].keys()))
        res_data_write.writeheader()
        for i in data:
            res_data_write.writerow(i)
            result_file.write('\n')  # для пустой строки между строками в файле

    print('Файл "result_data.csv" успешно создан\nПроверьте его содержимое')


write_to_csv()
# get_data() # для проверки

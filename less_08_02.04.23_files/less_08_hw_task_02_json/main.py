"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import random
import json


def write_order_to_json(item, quantity, price, buyer, date):
    my_order_dict = {'item': item,
                     'quantity': quantity,
                     'price': price,
                     'buyer': buyer,
                     'date': date}
    orders_list = list()
    all_orders_dict = {}
    key_orders_dict = ''
    with open('orders.json') as orders_file:
        orders_prev = json.load(orders_file)  # выгружаем имеющиеся данные из файла
    for section, command in orders_prev.items():
        key_orders_dict = section  # ключ выгруженного словаря
        orders_list = command  # список ордеров (словарей)

    orders_list.append(my_order_dict)   # добавляем в список ордеров(словарей) - новый ордер
    all_orders_dict[key_orders_dict] = orders_list  # добавляем дополненный список в словарь ордеров
    # print(all_orders_dict)  # для проверки

    with open('orders.json', 'w') as orders_file:  # открываем файл для записи в файл
        json.dump(all_orders_dict, orders_file,  # запись дополненного словаря
                  sort_keys=True, indent=4, ensure_ascii=False)
        # красивый вывод: indent-отступы; ensure_ascii-русский текст

    print('Данные нового ордера успешно добавлены в файл "orders.json"')


#  "база данных" для случайного выбора значений для ордера
item_list = ['wifi_router', 'laptop', 'mouse', 'keyboard', 'mother_board']
quantity_list = ['2', '5', '10', '3', '8', '7', '1', '4', '9']
price_list = ['10000', '30000', '500', '1500', '20000', '16000', '200']
buyer_list = ['Сидоров С.С.', 'Иванов И.И', 'Петров П.П.', 'Федорова С.Ш.']
date_list = ['03.04.2023', '23.12.2000', '01.01.2022', '10.05.2005']

orders_count = 2  # кол-во ордеров для записи в файл
for i in range(0, orders_count):
    item = random.choice(item_list)
    quantity = random.choice(quantity_list)
    price = random.choice(price_list)
    buyer = random.choice(buyer_list)
    date = random.choice(date_list)

    write_order_to_json(item, quantity, price, buyer, date)

    # print(item, quantity, price, buyer, date)  # для проверки сгенерированных данных ордера

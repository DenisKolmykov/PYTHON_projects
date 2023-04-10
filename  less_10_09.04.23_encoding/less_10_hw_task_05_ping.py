"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess


def ping_sites(site_name, c):
    print(f'PING сайта {site_name}')
    args = ['ping', site_name]
    site_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    print(site_ping.stdout)

    i = 0  # счетчик для прерывания
    for row in site_ping.stdout:
        if i == c:
            break
        res = chardet.detect(row)
        print(res)
        print(row.decode(encoding=res['encoding']))
        i += 1
    print(f'------ PING "{site_name}" ЗАВЕРШЕН --------')


site_names = ['yandex.ru', 'youtube.com']
count = 10  # счетчик для прерывания

for s in site_names:
    ping_sites(s, count)

"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

def word_to_byte(word):
    wb = b''
    for char in word:
        bch = ord(char)
        try:
            wb += bch.to_bytes()
        except OverflowError:
            print(f'! Слово "{word}" не возможно записать '
                  f'в байтовом предствалении, т.к. '
                  f'присутствует символ(ы) за пределами ASCII')
            return

    print(f'Слово "{word}" в байтовом предствалении:" {wb} " '
          f'({type(wb)}), length = {len(wb)}')



words = ['attribute', 'класс', 'функция', 'type']

for w in words:
    word_to_byte(w)

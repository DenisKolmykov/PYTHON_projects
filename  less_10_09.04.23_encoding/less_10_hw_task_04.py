"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def word_to_byte(word):
    bw = word.encode()
    print(f'слово "{word}" в байтовом представлении --> {bw}')
    #  bw = w.encode('unicode_escape')
    #  print(bw)
    return bw


def byte_to_word(byte_w):
    word_from_byte = byte_w.decode()
    print(
        f'из байтового представления {byte_w} в слово --> "{word_from_byte}"')
    return word_from_byte


words = ['разработка', 'администрирование', 'protocol', 'standard']

bw = list()
for w in words:
    bw.append(word_to_byte(w))
print(bw, '\n')

words_from_byte = list()
for i in bw:
    words_from_byte.append(byte_to_word(i))
print(words_from_byte)

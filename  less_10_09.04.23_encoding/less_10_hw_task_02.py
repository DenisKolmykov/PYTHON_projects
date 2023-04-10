"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = ['class', 'function', 'method']

print('------- Вар.1 --------')


def char_to_byte(word):
    wb = b''
    for c in word:
        ch_to_byte = ord(c)
        wb += ch_to_byte.to_bytes()

    print(f'Слово "{word}" в байтовом представлении:" {wb} " '
          f'({type(wb)}), length = {len(wb)}')


for i in words:
    char_to_byte(i)
#  -----------------------------

print('------- Вар.2 --------')
for w in words:
    bw = bytes(w, encoding='utf-8')
    print(f'Слово "{w}" в байтовом представлении --> {bw},'
          f' ({type(bw)}), length = {len(bw)}')
#  -----------------------------

print('------- Вар.3 --------')


def word_to_byte(bword):
    print(f' byte_format --> {bword}, ({type(bword)}), length = {len(bword)}')


bw = list()
bw.append(b'class')
bw.append(b'function')
bw.append(b'method')

for i in bw:
    word_to_byte(i)

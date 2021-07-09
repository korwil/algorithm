# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import heapq  # модуль для работы с мин. кучей из стандартной библиотеки Python
from collections import Counter
from collections import namedtuple

# информации о структуре дерева
class Node(namedtuple("node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"

class Leaf(namedtuple("leaf", ["char"])):  # класс для листьев дерева
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"

def get_tree(h, index):
    if len(h) <= 1:
        return  h
    else:
        freq1, _, left = heapq.heappop(h)
        freq2, _, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, index, Node(left, right)))
        return get_tree(h, index + 1)

def huffman_encode(s):  # функция кодирования строки в коды Хаффмана
    h = []  # очередь с приоритетами
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  # очередь будет представлена частотой символа, идентификатор и самим символом
    heapq.heapify(h)  # построим очередь с приоритетами
    print(h)
    get_tree(h, len(h)) # переведем список в дерево
    print(h)
    code = {}  # словарь кодов символов
    if h:  # если строка пустая, то очередь будет пустая и обходить нечего
        (_, _, root) = h[0]  # берем корень дерева
        root.walk(code, "")  # обойдем дерева от корня и заполним словарь для получения кодирования Хаффмана
    return code  # возвращаем словарь символов и соответствующих им кодов

s = 'на траве дрова во дворе трава, не руби дрова на траве двора'
code = huffman_encode(s)
encoded = "".join(code[ch] for ch in s) # кодируем строку

print('символы и код')
for ch in sorted(code):
    print(f'{ch}: {code[ch]}')  # выведем символ и соответствующий ему код
print(f'Закодированная строка: \n{encoded}')

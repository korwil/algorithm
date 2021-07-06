# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

l = [random.randint(0, 50) for _ in range(20)]


def merge(first, second):
    merged = []
    while len(first) or len(second):
        if len(first) and len(second):
            merged.append(first.pop(0) if first[0] < second[0] else second.pop(0))
        else:
            merged.append(first.pop(0) if len(first) else second.pop(0))
    return merged


def sort(ar):
    if len(ar) <= 2:
        return ar if len(ar) == 1 or ar[0] < ar[1] else [ar[1], ar[0]]
    separator = len(ar) // 2
    return merge(sort(ar[:separator]), sort(ar[separator:]))

print(l)
print(sort(l))
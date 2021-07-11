# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random

l = [random.randint(-100, 100) for _ in range(20)]
print(l)


def bubble(a):
    itteration = 0
    for _ in range(len(a)):
        for i in range(len(a)-1):
            itteration +=1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a, itteration

def bubble2(a):
    itteration = 0
    for N in range(len(a)):
        for i in range(len(a)-(N+1)):
            itteration +=1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a, itteration


print(bubble(l))
print(bubble2(l))
# 6. В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import random
N = 15
numbers = [0]*N
for i in range(N):
    numbers[i] = int(random()*100)
print(numbers)

min = max = 0
for i, number in enumerate(numbers):
    if numbers[min] > number:
        min = i
    if numbers[max] < number:
        max = i

def sum(a,b):
    result = 0
    for i in numbers[a+1:b]:
        result += i

    return result


if min < max:
    print(sum(min, max))
else:
    print(sum(max, min))

print(numbers)
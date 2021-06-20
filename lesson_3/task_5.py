# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

numbers = [12, -211, 3, -423, 12, -3, 425, -11, 3, 12, 12]
min = 0
for number in numbers:
    if min > number:
        min = number

if min == 0:
    print('В массиве нет отрицательных элементов')
else:
    print(f'{numbers.index(min)} : {min}')
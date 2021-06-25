# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.
numbers = [12, -211, 3, 423, 12, 3, 425, -11, 3, 12, 12]
print(numbers)
min = max = 0
for i, number in enumerate(numbers):
    if numbers[min] > number:
        min = i
    if numbers[max] < number:
        max = i
numbers[min], numbers[max] = numbers[max], numbers[min]
print(numbers)

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.


# Python 3.8.5
# import platform
# print(platform.architecture()[0])
# 32 bit


numbers = [12, -211, 3, -423, 12, -3, 425, -11, 3, 12, 12]
min_1 = numbers[0]
min_2 = numbers[1]
for n in numbers:
    if min_1 > n:
        min_1 = n
    elif min_2 > n:
        min_2 = n

print(numbers)
print(f'первое минимальное число: {min_1}, второе: {min_2}')
print(f'Для числа numbers памяти затрачено: {numbers.__sizeof__()} bytes. '
      f'Предполагаемо: 20+4*длина = {20 + 4 * len(numbers)}')

numbers = {12, -211, 3, -423, 12, -3, 425, -11, 3, 12, 12}

print(f'Для числа numbers памяти затрачено: {numbers.__sizeof__()} bytes. '
      f'Предполагаемо: 100+8*длина = {100 + 8 * len(numbers)}')
# print(struct.unpack('L'*7+'lL'*8+'lL', ctypes.string_at(id(numbers), 100)))

numbers = (12, -211, 3, -423, 12, -3, 425, -11, 3, 12, 12)
print(f'Для числа numbers памяти затрачено: {numbers.__sizeof__()} bytes. '
      f'Предполагаемо: 12+4*длина = {12 + 4 * len(numbers)}')



# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f',
# то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

v1, v2 = input('Введите границы для целого числа через пробел: ').split()

print(f'Целое число: {random.randint(int(v1), int(v2))}')

v1, v2 = input('Введите границы для вещественного числа через пробел: ').split()

print(f'Вещественное число: {random.uniform(float(v1), float(v2))}')

v1, v2 = input('Введите границы для символа через пробел: ').split()

print(f'Символ: {chr(random.randint(ord(v1), ord(v2)))}')




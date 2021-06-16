# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

value_in = int(input('Введите число: '))
even = 0
uneven = 0
value = value_in
while value > 0:
    m = value % 10
    if m % 2 == 0:
        even += 1
    else:
        uneven += 1

    value = value//10
print(f'В числе {value_in} {even} четных и {uneven} нечетных цифр')

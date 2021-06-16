# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def sum(v):
    result = 0
    while v > 0:
        result += v % 10
        v = v // 10

    return result


l = input('Введите числа через пробел: ').split()
max_c = 0
max_n = None
for i in l:
    s = sum(int(i))
    if s > max_c:
        max_c = s
        max_n = int(i)

print(f'Число {max_n} иммет максимальную сумму цифр: {max_c}')

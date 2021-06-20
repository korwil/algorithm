# 9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

f = float(input('Введите первое число: '))
s = float(input('Введите второе число: '))
t = float(input('Введите третье число: '))

average = None
if s > f > t or s < f < t:
    average = f
elif f > s > t or f < s < t:
    average = s
else:
    average = t

print(f'Среднее число: {average}')
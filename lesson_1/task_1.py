# 1. Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

value = int(input('Введите трехзначное число: '))

first = value // 100
second = value // 10 % 10
third = value % 10

sum = first + second + third
mul = first*second*third
print(f'Ввели число = {value}')
print(f'Сумма цифр = {sum}')
print(f'Произведение цифр = {mul}')
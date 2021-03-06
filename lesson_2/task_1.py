# 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

while True:
    s = input('Введите операцию +, -, *, /, 0(для выхода): ')
    if s == '0':
        break
    elif s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(f'x+y={x+y}')
        elif s == '-':
            print(f'x-y={x-y}')
        elif s == '*':
            print(f'x*y={x*y}')
        elif s == '/':
            if y != 0:
                print(f'x/y={x/y}')
            else:
                print('Деление на ноль!')
    else:
        print('Неверный знак операции!')
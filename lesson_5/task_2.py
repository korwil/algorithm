# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого
# это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

v1 = input('Первое число: ')
v2 = input('Второе число: ')

class Hex:
    def __init__(self, x):
        self.x = [ i.upper() for i in list(x)]
    def __str__(self):
        return f'result: {self.x}'
    def __add__(self, obj):
        value1 = ''.join(self.x)
        value2 = ''.join(obj.x)
        return Hex(hex(int(value1, 16) + int(value2, 16))[2:])
    def __mul__(self, obj):
        value1 = ''.join(self.x)
        value2 = ''.join(obj.x)
        return Hex(hex(int(value1, 16) * int(value2, 16))[2:])


a = Hex(v1)
b = Hex(v2)
print(f'Сумма = {a + b}')
print(f'Произведение = {a * b}')


#===== Альтернатива ========

a = list(v1)
b = list(v2)

def summ(a, b):
    value1 = ''.join(a)
    value2 = ''.join(b)
    return list(hex(int(value1, 16) + int(value2, 16)).upper()[2:])

def mul(a, b):
    value1 = ''.join(a)
    value2 = ''.join(b)
    return list(hex(int(value1, 16) * int(value2, 16)).upper()[2:])

print('===== Альтернатива ========')
print(f'Сумма = {summ(a, b)}')
print(f'Произведение = {mul(a, b)}')
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

v1 = int(input('Номер буквы: '))

print(f'Буква: {chr(v1 + ord("a") - 1)}')
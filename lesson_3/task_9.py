# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

a = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [6, 2, 3, 4, 5],
]
max = a[0][0]
tmp = []
for j in range(len(a[0])):
    min = a[0][j]
    for i in range(len(a)):
        if min > a[i][j]:
            min = a[i][j]
    tmp.append(min)
    if max < min :
        max = min

print('Массив:')
for n in a:
    print(n)
print(f'Минимальные значения столбцов: \n{tmp}')
print(f'Максимальное из минимальных = {max}')

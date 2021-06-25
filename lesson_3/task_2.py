
a = [8, 3, 15, 6, 4, 2]
result = []
for i, val in enumerate(a):
    if val % 2 == 0:
        result.append(i)
print(result)

a = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in range(2, 99):
    for index, value in a.items():
        if i % index == 0:
            print( f'{i} кратно {index}' )
            value += 1
            a[index] = value
print(a)
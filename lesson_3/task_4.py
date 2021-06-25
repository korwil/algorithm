# 4. Определить, какое число в массиве встречается чаще всего.

numbers = [12, 211, 3, 423, 12, 3, 425, -11, 3, 12, 12]
i = 0
dictionary = {}
for i, number in enumerate(numbers):
    if numbers[i] in dictionary:
        dictionary[numbers[i]] += 1
    else:
        dictionary[numbers[i]] = 1
print(max(dictionary, key=dictionary.get))
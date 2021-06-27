# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.
import collections
import numpy as np

count = int(input('Введите количество предприятий'))
companies = {}
for _ in range(count):
    name = input('Введите название компании: ')
    companies[name] = {
        'Прибыль': [int(input(f"Прибыль за {i+1}-ый квартал: ")) for i in range(4)]
    }
    companies[name]['avg'] = np.mean(companies[name]['Прибыль'])


print(companies)
avg = np.mean([v['avg'] for _, v in companies.items()])
print(avg)

avg_less = []
avg_more = []
for name, value in companies.items():
    if avg >= companies[name]['avg']:
        avg_less.append(name)
    else:
        avg_more.append(name)

print(f'Средняя прибыль (за год для всех предприятий) {avg}')
print(f'Предприятия с прибылью ниже среднего {avg_less}')
print(f'Предприятия с прибылью выше среднего {avg_more}')


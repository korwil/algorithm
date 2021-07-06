# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
import random
import timeit
import cProfile

# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.
n = 10000000
numbers = []
for i in range(n):
    numbers.append(random.random())

# Сложность: ~2n
def change_min_max_0(numbers):
    min = max = numbers[0]
    for i, number in enumerate(numbers):
        if numbers[min] > number:
            min = i
        if numbers[max] < number:
            max = i

    numbers[min], numbers[max] = numbers[max], numbers[min]
    return numbers

# Сложность: ~2n
def change_min_max_1(numbers):
    mx = numbers.index(max(numbers))
    mn = numbers.index(min(numbers))
    numbers[mn], numbers[mx] = numbers(mx), numbers(mx)
    return numbers

# Сложность: ~2n
def change_min_max_2(numbers):
    min = max = numbers[0]
    for i, number in enumerate(numbers):
        if numbers[min] > number:
            min = i
    for i, number in enumerate(numbers):
        if numbers[max] < number:
            max = i

    numbers[min], numbers[max] = numbers[max], numbers[min]
    return numbers

# Сложность: n*log(n)
def change_min_max_3(numbers):
    a = numbers.copy()
    a.sort()
    mn = numbers.index(a[0])
    mx = numbers.index(a[-1])
    numbers[mn], numbers[mx] = numbers[mx], numbers[mn]
    return numbers


time1 = timeit.Timer('change_min_max_0', 'from task_1 import change_min_max_0')
cProfile.run('change_min_max_0')
print(f'Time.timeit: {time1.timeit()}')
#    3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#    3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Time.timeit: 0.02427120000000027
# Time.timeit: 0.01501579999999958


time2 = timeit.Timer('change_min_max_1', 'from task_1 import change_min_max_1')
cProfile.run('change_min_max_1')
print(f'Time.timeit: {time2.timeit()}')

#         3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#          3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Time.timeit: 0.03098460000000003
# Time.timeit: 0.01678960000000007


time3 = timeit.Timer('change_min_max_2', 'from task_1 import change_min_max_2')
cProfile.run('change_min_max_2')
print(f'Time.timeit: {time3.timeit()}')

#          3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#          3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Time.timeit: 0.0181792999999999
# Time.timeit: 0.020974999999999966

time4 = timeit.Timer('change_min_max_3', 'from task_1 import change_min_max_3')
cProfile.run('change_min_max_3')
print(f'Time.timeit: {time4.timeit()}')
#          3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#          3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Time.timeit: 0.024245899999999487
# Time.timeit: 0.03194530000000029


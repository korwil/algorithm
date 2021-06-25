# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию:
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
import cProfile
import sys
import timeit

sys.setrecursionlimit(10000)

i = int(input("i = "))

# Перебираем значения с рекурсией
# Сложность  n ** 2
def find_1(i, tmp=2, lst=[]):
    if i <= 0:
        return lst[-1]
    for j in lst:
        if tmp % j == 0:
            break
    else:
        lst.append(tmp)
        i -= 1
    return find_1(i, tmp+1, lst)

print(find_1(i))

time1 = timeit.Timer(f'find_1({i}, 2, [])', 'from task_2 import find_1')
cProfile.run(f'find_1({i})')
print(f'Time.timeit: {time1.timeit()}')

# i = 10
# Time.timeit: 76.6544479
# Time.timeit: 77.30424560000002
# i = 50
# Time.timeit: 889.9020617
# Time.timeit: 811.0043188

# i = 200
#          3106 function calls (366 primitive calls) in 0.020 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#         9    0.000    0.000    0.000    0.000 ntpath.py:124(splitdrive)
#         2    0.000    0.000    0.000    0.000 ntpath.py:180(split)
#         1    0.000    0.000    0.000    0.000 ntpath.py:214(basename)
#         3    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
#         6    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
#         2    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
#         1    0.000    0.000    0.000    0.000 ntpath.py:524(abspath)
#         1    0.000    0.000    0.000    0.000 ntpath.py:537(_readlink_deep)
#         1    0.000    0.000    0.000    0.000 ntpath.py:579(_getfinalpathname_nonstrict)
#         1    0.000    0.000    0.000    0.000 ntpath.py:61(isabs)
#         1    0.000    0.000    0.001    0.001 ntpath.py:625(realpath)
#         2    0.000    0.000    0.000    0.000 ntpath.py:77(join)
#         2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
#         1    0.000    0.000    0.001    0.001 pydevd_file_utils.py:228(_NormPaths)
#         2    0.000    0.000    0.001    0.000 pydevd_file_utils.py:245(_NormPath)
#         1    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
#         1    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
#         1    0.000    0.000    0.001    0.001 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
#    2741/1    0.019    0.000    0.019    0.019 task_2.py:17(find_1)
#         1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#        24    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#        20    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         4    0.000    0.000    0.000    0.000 {built-in method nt._getfinalpathname}
#         1    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
#        22    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
#         1    0.000    0.000    0.000    0.000 {built-in method nt.getcwd}
#         1    0.000    0.000    0.000    0.000 {built-in method nt.readlink}
#         1    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#       200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
#         6    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
#         2    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#         8    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
#        18    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
#         2    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
#         2    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
#         9    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}


# Решето Эратосфена
# Сложность  n * log(log(n))
def eratosthenes(i):
    sieve = list(range(i * i))
    lst = []
    sieve[1] = 0  # без этой строки итоговый список будет содержать единицу

    for n in sieve:
        if len(lst) == i:
            break
        if n > 1:
            for j in range(n + n, len(sieve), n):
                sieve[j] = 0
            else:
                lst.append(n)

    return lst[-1]


print(eratosthenes(i))

time1 = timeit.Timer(f'eratosthenes({i})', 'from task_2 import eratosthenes')
cProfile.run(f'eratosthenes({i})')
print(f'Time.timeit eratosthenes: {time1.timeit()}')

# i = 10
# Time.timeit eratosthenes: 37.2562102
# Time.timeit eratosthenes: 35.4303869
# i = 50
# Time.timeit eratosthenes: 945.2509815
# Time.timeit eratosthenes: 841.6233653
# i = 200
#          1629 function calls in 0.016 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#         1    0.015    0.015    0.016    0.016 task_2.py:43(eratosthenes)
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#      1425    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод:
# По сложности алгоритмов первый более сложный
# По скорости выполнения timeIt говорит что выполенния второго алгоритма больше, хотя по показаниям cProfile наоборот.
# Не смог запустить timeIt на более больших значений, т.к. ловил ошибку нехватки памяти
# Второй алгоритм более избыточен и имеет ограничения по используемой памяти

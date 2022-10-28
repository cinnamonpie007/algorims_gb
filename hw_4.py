# task 1
# from timeit import timeit
#
#
# def func_1(nums):
#     new_arr = []
#     for i in range(len(nums)):
#         if nums[i] % 2 == 0:
#             new_arr.append(i)
#     return new_arr
#
#
# def func_2(nums):
#     return [i for i, e in enumerate(nums) if e % 2 == 0]
#
#
# lst = list(range(100))
#
# print(timeit("func_1(lst)", globals=globals()))
# print(timeit("func_2(lst)", globals=globals()))

# использовал list comprehension вместо цикла, это уменьшило время выполнения

# task 2
#
#
# from timeit import timeit
# from random import randint
#
#
# def recursive_reverse(number):
#     if number == 0:
#         return str(number % 10)
#     return f'{str(number % 10)}{recursive_reverse(number // 10)}'
#
#
# num_100 = randint(10000, 1000000)
# num_1000 = randint(1000000, 10000000)
# num_10000 = randint(100000000, 10000000000000)
#
# print('Не оптимизированная функция recursive_reverse')
# print(
#     timeit(
#         "recursive_reverse(num_100)",
#         setup='from __main__ import recursive_reverse, num_100',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_1000)",
#         setup='from __main__ import recursive_reverse, num_1000',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_10000)",
#         setup='from __main__ import recursive_reverse, num_10000',
#         number=10000))
#
#
# def memoize(f):
#     cache = {}
#
#     def decorate(*args):
#
#         if args in cache:
#             return cache[args]
#         else:
#             cache[args] = f(*args)
#             return cache[args]
#     return decorate
#
#
# @memoize
# def recursive_reverse_mem(number):
#     if number == 0:
#         return ''
#     return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'
#
#
# print('Оптимизированная функция recursive_reverse_mem')
# print(
#     timeit(
#         'recursive_reverse_mem(num_100)',
#         setup='from __main__ import recursive_reverse_mem, num_100',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_1000)',
#         setup='from __main__ import recursive_reverse_mem, num_1000',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_10000)',
#         setup='from __main__ import recursive_reverse_mem, num_10000',
#         number=10000))


# мемоизация здесь не нужна, т.к. в данном случае она не ускоряет саму рекурсию
# время выполнения функции с мемоизацией меньше потому что timeit повторяет вызов функции 1000000 раз (по умол.)
# с одним и тем же переданным аргументом (числом), но рекурсия выполняется только в первый вызов,
# а в последующие вызовы результат берется из кэша

# task 3
#
# from timeit import timeit
#
#
# def revers(enter_num, revers_num=0):
#     if enter_num == 0:
#         return
#     else:
#         num = enter_num % 10
#         revers_num = (revers_num + num / 10) * 10
#         enter_num //= 10
#         revers(enter_num, revers_num)
#
#
# def revers_2(enter_num, revers_num=0):
#     while enter_num != 0:
#         num = enter_num % 10
#         revers_num = (revers_num + num / 10) * 10
#         enter_num //= 10
#     return revers_num
#
#
# def revers_3(enter_num):
#     enter_num = str(enter_num)
#     revers_num = enter_num[::-1]
#     return revers_num
#
#
# def revers_4(enter_num):
#     return ''.join(reversed(str(enter_num)))
#
#
# n = 786129
#
# print(timeit("revers(n)", globals=globals()))
# print(timeit("revers_2(n)", globals=globals()))
# print(timeit("revers_3(n)", globals=globals()))
# print(timeit("revers_4(n)", globals=globals()))


# третья функция эффективнее, т.к. работа со срезами самая быстрая
# в четвертой функции join занимает бОльшую часть времени, без него reversed примерно равна по времени с
# третьей функцией

# task 4

#
# from timeit import timeit
#
#
# array = [1, 3, 1, 3, 4, 5, 1]
#
#
# def func_1():
#     m = 0
#     num = 0
#     for i in array:
#         count = array.count(i)
#         if count > m:
#             m = count
#             num = i
#     return f'Чаще всего встречается число {num}, ' \
#            f'оно появилось в массиве {m} раз(а)'
#
#
# def func_2():
#     new_array = []
#     for el in array:
#         count2 = array.count(el)
#         new_array.append(count2)
#
#     max_2 = max(new_array)
#     elem = array[new_array.index(max_2)]
#     return f'Чаще всего встречается число {elem}, ' \
#            f'оно появилось в массиве {max_2} раз(а)'
#
#
# def func_3():
#     n = max(array, key=array.count)
#     return f'Чаще всего встречается число {n}, ' \
#            f'оно появилось в массиве {array.count(n)} раз(а)'
#
#
# print(func_1())
# print(func_2())
# print(func_3())
#
# print(timeit("func_1()", globals=globals()))
# print(timeit("func_2()", globals=globals()))
# print(timeit("func_3()", globals=globals()))

# 0.8134944339999493
# 1.0522533759994985
# 0.835265456000343

# ускорить не получилось, func_3 выполняется по времени чуть медленнее чем func_1

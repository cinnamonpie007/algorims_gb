# task 1
# from timeit import timeit
# from random import randint
#
#
# def rev_bubble_sort(lst):
#     n = len(lst) - 1
#     while n > 0:
#         for i in reversed(range(len(lst) - n, len(lst))):
#             if lst[i] < lst[i-1]:
#                 lst[i], lst[i-1] = lst[i-1], lst[i]
#         n -= 1
#     return lst
#
#
# def optimized_rev_bubble_sort(lst):
#     n = len(lst) - 1
#     while n > 0:
#         count = 0
#         for i in reversed(range(len(lst) - n, len(lst))):
#             if lst[i] < lst[i-1]:
#                 lst[i], lst[i-1] = lst[i-1], lst[i]
#                 count += 1
#         n -= 1
#         if not count:
#             break
#     return lst
#
#
# new_list = [randint(-100, 100) for i in range(500)]
# ordered_list = [i for i in range(500)]
# almost_ordered_list = [i for i in range(500)]
# almost_ordered_list[50] = 101
#
# print(timeit("rev_bubble_sort(new_list[:])", globals=globals(), number=1000))                       # 21.29 сек
# print(timeit("optimized_rev_bubble_sort(new_list[:])", globals=globals(), number=1000))             # 22.28 сек
# print(timeit("rev_bubble_sort(ordered_list[:])", globals=globals(), number=1000))                   # 11.77 сек
# print(timeit("optimized_rev_bubble_sort(ordered_list[:])", globals=globals(), number=1000))         # 0.04 сек
# print(timeit("rev_bubble_sort(almost_ordered_list[:])", globals=globals(), number=1000))            # 12.05 сек
# print(timeit("optimized_rev_bubble_sort(almost_ordered_list[:])", globals=globals(), number=1000))  # 2.56 сек
#
# # Оптимизация не помогает, а наоборот увеличивает время работы на произвольных
# # несортированных списках. Однако при получении отсортированного списка, не производятся ненужные вычисления, и
# # поэтому время заметно сокращается. На почти полностью отсортированных списках время также существенно меньше у
# # оптимизированного варианта.
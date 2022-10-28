# # task 1
# def calculator():
#      operations = ['+', '-', '/', '*', '0']
#      opr = input('Введите операцию (+, -, *, / или 0 для выхода): ')
#      if opr not in operations:
#          print('введите знак сначала: ')
#          calculator()
#      if opr == '0':
#          print('завершено')
#          return
#      try:
#          x = float(input('Введите первое число: '))
#          y = float(input('Введите второе число: '))
#      except ValueError:
#          print('введите знак: ')
#          calculator()
#      if opr == '+':
#          print(x + y)
#          calculator()
#      elif opr == '-':
#          print(x - y)
#          calculator()
#      elif opr == '*':
#          print(x * y)
#          calculator()
#      elif opr == '/':
#          if y == 0:
#              print('Математику надо было в школе учить')
#              calculator()
#          print(x / y)
#
# calculator()

# task 2

# counter = [0, 0]
#
#
# def even_odd(num):
#     if num < 10:
#         if num % 10 % 2 == 0:
#             counter[0] = counter[0] + 1
#         else:
#             counter[1] = counter[1] + 1
#         print('Четных цифр:', counter[0], 'Нечетных цифр:', counter[1])
#         return
#     if num % 10 % 2 == 0:
#         counter[0] = counter[0] + 1
#         even_odd(num // 10)
#     else:
#         counter[1] = counter[1] + 1
#         even_odd(num // 10)
#
#
# even_odd(734638)

#task 3
#
# numba = []
#
#
# def num(numb):
#     if numb > 10:
#         numba.append(str(numb % 10))
#         num(numb // 10)
#     else:
#         numba.append(str(numb))
#
#         print(''.join(numba))
#
# num(67678)

#task 4

# def sum_of_seq(a, n):
#     if n == 0:
#         return 0
#     return a + sum_of_seq(a / -2, n - 1)
#
#
# print(sum_of_seq(1, 6))

# task 5

# def simvol(n=32):
#     if n > 127:
#         return
#     print(n, ' - ', chr(n), end=' ' if (n + 9) % 10 != 0 else '\n')
#     simvol(n + 1)
#
#
# simvol()

# task 6
#
# from random import randint
#
#
# def numb(num, tr=1):
#     if tr > 10:
#         print('Неудача!')
#         return
#     try:
#         x = int(input(f'{tr}я Попытка. Попробуйте угадать число: '))
#         if x == num:
#             print('Победа!')
#             return
#         print('Загаданное число', 'меньше' if x > num else 'больше')
#         numb(num, tr + 1)
#
#     except ValueError:
#         print('Это не число')
#         numb(num, tr + 1)
#
#
# numb(randint(1, 100))

# task 7
#
# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n - 1)
#
#
# x = int(input('введите число: '))
#
# if sum(x) == x * (x + 1) / 2:
#     print('true')
# else:
#     print('false')
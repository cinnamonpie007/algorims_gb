#
# #task 1
#
# import time
#
#
# def time_measure(func):
#     def wrapper(*args):
#         start_t = time.time()
#         func(*args)
#         end_t = time.time()
#         return end_t - start_t
#
#     return wrapper
#
#
# my_lst = []
# my_dict = dict()
#
#
# # a)
#
# @time_measure
# def list_fill(n):
#     for i in range(n):  # O(n)
#         my_lst.append(i)  # O(1)
#
#
# @time_measure
# def dict_fill(n):
#     for i in range(n):  # O(n)
#         my_dict[i] = i  # O(1)
#
#
# print('Время на заполнение списка -', list_fill(100000000))
# print('Время на заполнение словаря -', dict_fill(100000000))
#
# # b)
#
#
# @time_measure
# def dict_del(n):
#     return my_dict.pop(n)           # O(1)
#
#
# @time_measure
# def lst_del(n):
#     return my_lst.pop(n)            # O(n)
#
#
# @time_measure
# def lst_change():
#     for i in range(len(my_lst)):    # O(n)
#         my_lst[i] = 100             # O(n)
#     return
#
#
# @time_measure
# def dict_change():
#     for i in my_dict.keys():        # O(n)
#         my_dict[i] = 100            # O(1)
#     return
#
#
# print('Время на удаление элемента из списка -', lst_del(9999997))
# print('Время на удаление элемента из словаря -', dict_del(9999997))
# print('Время на изменение элемента из списка -', lst_change())
# print('Время на изменение элемента из словаря -', dict_change())
#
# task 2
# import mysql.connector
# import hashlib
# from binascii import hexlify
#
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='******'
# )
#
# cursor = db.cursor()
# cursor.execute('CREATE DATABASE hash_task3')
# cursor.execute('USE hash_task3')
# cursor.execute('CREATE TABLE hashes (hash VARCHAR(255), salt VARCHAR(255))')
#
# salt = input('Введите логин')
# inp_pswd = input('Введите пароль')
#
# hash_obj = hashlib.pbkdf2_hmac(hash_name='sha256',
#                                password=inp_pswd.encode('utf-8'),
#                                salt=salt.encode('utf-8'),
#                                iterations=100)
#
# result = hexlify(hash_obj)
# print(result)
#
# sql = 'INSERT INTO hashes VALUES (%s, %s)'
# val = (result, salt)
# cursor.execute('USE hash_task3')
# cursor.execute(sql, val)
#
# db.commit()
#
# check_pswd = input('Введите пароль повторно')
# check_hash_obj = hashlib.pbkdf2_hmac(hash_name='sha256',
#                                      password=check_pswd.encode('utf-8'),
#                                      salt=salt.encode('utf-8'),
#                                      iterations=100)
#
# check_result = hexlify(check_hash_obj).decode('utf-8')
#
# sql = 'SELECT hash FROM hashes WHERE salt = %s'
# val = (salt,)
# cursor.execute(sql, val)
# res = cursor.fetchall()
# res = str(res[0][0])
#
# if res == check_result:
#     print('Все верно')
# else:
#     print('Неверно')


# task 3
# import hashlib
#
# my_str = input('Введите строку: ')
# a = set()
# my_lst = list(my_str)
#
# for i in range(len(my_lst)):
#     for j in range(i + 1, len(my_lst) + 1):
#         el = ''.join(my_lst[i:j])
#         el = hashlib.sha1(el.encode('utf-8')).hexdigest()
#         a.add(el)
#
# print(f'Количество уникальных подстрок - {len(a) - 1}')

# task 4
#
# import hashlib
#
# cash = dict()
# salt = 'abcdefg'
#
# while True:
#     url = input('Введите URL (0, чтобы выйти): ')
#     if url == '0':
#         break
#     if url in cash.keys():
#         print('Хеш:', cash[url])
#     else:
#         cash[url] = hashlib.sha512(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
#         print('Записано в кэш')
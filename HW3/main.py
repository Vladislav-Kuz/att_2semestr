# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# 5
# 1 2 3 4 5
# 3-> 1

# from random import randint
#
# n = int(input("Введите количество элементов: "))
#
# # list_rand = [randint(1, 10) for i in range(n)]
#
# print(f'Введите элементы массива: ')
# for i in range(n):
#     list_rand[i] = int(input("A[%d] = " % i))
# print(list_rand)
# count = 0
# list_out = list()
# a = int(input("Введите искомое число: "))
#
# for i in range(0, len(list_rand), 1):
#     if a == list_rand[i]:
#         count += 1
# print(f'{a} -> {count} раз')



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# from random import randint
#
# n = int(input("Введите количество элементов: "))
# list_rand = [randint(1, 100) for i in range(n)]
# print(list_rand)
# a = int(input("Введите число: "))
# min_dif_el = list_rand[0]
# for i in range(0, n):
#     dif_curr = abs(a - list_rand[i])
#     dif_prev = abs(a - min_dif_el)
#     if dif_curr < dif_prev:
#         min_dif_el = list_rand[i]
#         min_pos_el = i
# print(f"Самый близкий по величине к {a} является элемент A[{min_pos_el}] = {min_dif_el}")


# list_1=[1, 2, 3, 4, 5,10]
# k=8
#
# res=[abs(list_1[i]-k) for i in range(len(list_1))]
#
# x=res.index(min(res))
#
# print(list_1)
# print(k)
# print(list_1[x])


# letters_dict = {
#         1 : 'AEIOULNSTRАВЕИНОРСТ',
#         2 : 'DGДКЛМПУ',
#         3 : 'BCMPБГЁЬЯ',
#         4 : 'FHVWYЙЫ',
#         5 : 'KЖЗХЦЧ',
#         8 : 'JXШЭЮ',
#         10 : 'QZФЩЪ'}
#
#
# k = "laptop".upper()
#
# result = [key for letter in k for key, value in letters_dict.items() if letter in value]
# print(sum(result))




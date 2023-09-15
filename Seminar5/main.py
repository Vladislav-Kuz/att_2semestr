# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
#
# Задание необходимо решать через рекурсию
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 177111
# def fib(num):
#     if num == 1 or num == 0:
#         return 1
#     return fib(num - 1) + fib(num - 2)
#
#
# n = 7
# res = fib(n-1)
# print(res)


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# import random
#
# def min_max_search(lst):
#     minNum = lst[0]
#     maxNum = lst[0]
#     for num in lst[1:]:
#         if num < minNum:
#             minNum = num
#         if num > maxNum:
#             maxNum = num
#     return minNum, maxNum
#
# def change(minN, maxN, lst):
#     for i in range (len(lst)):
#         if lst[i] == maxN:
#             lst[i] = minN
#     return lst
#
# n = 5
# list_1 = [random.randint(1,5) for _ in range(n)]
#
# # minNum = min(list_1)
# # maxNum = max(list_1)
# minNum, maxNum = min_max_search(list_1)
# print(list_1)
# print(change(minNum, maxNum, list_1))


# Простые числа

# # Variant1
# def is_number_simple(num: int) -> bool:
#     if num % 2 == 0 and num != 2:
#         return False
#
#     for i in range(3, num, 2):
#         if num % i == 0:
#             return False
#     return True
#
# # Variant2
# n = int(input('Введите число: '))
# if is_number_simple(n):
#     print(f'Число {n} является простым')
# else:
#     print(f'Число {n} простым не является')
#
#
# def is_number_simple(num: int) -> bool:
#     if num % 2 == 0 and num != 2:
#         return False
#
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True
#
#
# n = int(input('Введите число: '))
# if is_number_simple(num=n):
#     print(f'Число {n} является простым')
# else:
#     print(f'Число {n} простым не является')

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
#
# Input:    2 -> 3 4
# Output: 4 3

from random import randint as rnd

# def print_numbers(num : int):
#     if num == 0:
#         return ""
#     str_num = input("Введите число = ")
#     return print_numbers(num - 1) + str_num + " "
#
#
# if __name__ != "__main__":
#     pass
# else:
#     n = int(input("Введите кол-во чисел = "))
#     print(print_numbers(n).strip())


# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
#
def pow_rec( x, y):
    if y == 1:
        return x
    if y != 1:
        return x * pow_rec(x, y - 1)


# n = 2
# m = 8
# print(pow_rec(n, m))
print(pow_rec(a = 9, b = 4))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# def sum_numbers(a, b):
#     if a != 0 and b != 0:
#         return 1 + sum_numbers(a-1, b)
#     return b
#
#
# m = 1023
# n = 700
#
# print(sum_numbers(n, m))

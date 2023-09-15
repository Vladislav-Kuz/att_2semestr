# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# from random import randint
#
# n = int(input("Введите размер 1-го массива: "))
# m = int(input("Введите размер 2-го массива: "))
#
# list_n = [randint(0, 100) for i in range(n)]
# list_m = [randint(0, 100) for i in range(m)]
# print(n, list_n)
# print(m, list_m)
#
# # list_diff = list()
# # for elem_n in list_n:
# #     if elem_n not in list_m:
# #         list_diff.append(elem_n)
#
# list_diff = [elem_n for elem_n in list_n if elem_n not in list_m]
#
# print(list_diff)

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# from random import randint
#
# n = int(input("Введите размер массива: "))
# list_n = [randint(0, 10) for i in range(n)]
# print(list_n)
#
# count_nums = 0
# for i in range(1, n-1):
#     if list_n[i-1] < list_n[i] and list_n[i+1] < list_n[i]:
#         count_nums += 1
# print(count_nums)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.

# from random import randint
#
#
# def get_random_array(array_len: int) -> list[int]:
#     return [randint(0, 9) for _ in range(array_len)]
#
#
# def count_doubles(array: list[int]) -> int:
#     count = 0
#     for i in range(len(array)-1):
#         for j in range(i + 1, len(array)):
#             if array[i] == array[j]:
#                 count += 1
#     return count
#
#
# if __name__ == "__main__":
#     n = int(input("Введите размер массива: "))
#     array = get_random_array(n)
#     print(array)
#     print(count_doubles(array=array))


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300   220 284


def sum_div(num):
    s = 1
    for div in range(2, int(num**0.5 + 1)):
        if num % div == 0:
            s += div + int(num//div)
    return s


k = int(input("Введите число: "))
result = []
# for num1 in range(2, k):
#     for num2 in range(num1 + 1, k):
#         sum1 = sum_div(num1)
#         sum2 = sum_div(num2)
#         if sum1 == sum2:
#             list_k.append((num1, num2))
for num1 in range(2, k):
    num2 = sum_div(num1)
    sum2 = sum_div(num2)
    if sum2 == num1 and num1 != num2:
        temp = (num1, num2)
        temp_res = min(temp), max(temp)
        if temp_res not in result:
            result.append(temp_res)
for tup_i in result:
    print(*tup_i)

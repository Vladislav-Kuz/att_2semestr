# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула дляполучения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
#
#
# n = 5
# a_1 = 7
# step = 2
a_1 = int(input("введите значение первого элемента: a1 = "))
step = int(input("введите шаг последовательности: d = "))
n = int(input("Введите количество элементов последовательности: n = "))
# list_1 = list()
# for i in range(1, n + 1):
#     el = a_1 + (i - 1) * step
#     list_1.append(el)
list_1 = [a_1 + (i - 1) * step for i in range(1, n+1)]
print(f"Члены прогрессии от a1 = {a_1} с шагом d = {step} и длиной n = {n}:  {list_1}")


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
# min_num = 6
# max_num = 13
#list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_el = -10
max_el = 10
max_len_rnd_arr = 10
min_num = int(input("Введите нижнюю границу: "))
max_num = int(input("Введите верхнюю границу: "))
list_1 = [randint(min_el, max_el) for _ in range(randint(1, max_len_rnd_arr))]
print(f"Число элементов образованного массива: {len(list_1)},\nМассив: {list_1}")
res_list = list()
for i in range(len(list_1)):
    if min_num > max_num:
        temp = min_num
        min_num = max_num
        max_num = temp
    if min_num <= list_1[i] <= max_num:
        res_list.append(i)
if len(res_list) == 0:
    print(f"Элементы из диапазона от {min_num} до {max_num} отсутствуют")
elif len(res_list) == 1:
    print(f"Индекс эл-та из диапазона от {min_num} до {max_num}: {res_list[0]}")
else:
    print(f"Индексы эл-тов из диапазона от {min_num} до {max_num}: {res_list}")

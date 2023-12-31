# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

count_r = 0
count_o = 0

print(f"Введите общее число монет: ")
n = int(input())
list_m = [randint(0, 2) for i in range(n)]
# Для удобства отображения сделаем список из символов
list_char = []
for i in range(0, n, 1):
    if list_m[i] == 0:
        list_char.append('Р')
    else:
        list_char.append('О')
print(list_char)

for i in range(n):
    if list_m[i] == 1:
        count_o += 1
for i in range(n):
    if list_m[i] == 0:
        count_r += 1
if count_r > count_o:
    print(f"Нужно перевернуть {count_o} монет, лежащих орлом вверх")
elif count_r < count_o:
    print(f"Нужно перевернуть {count_r} монет, лежащих решкой вверх")
else:
    print(f"Монет одинаковое количество: {count_r}")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# x+y=s x*y=p
# D = s^2 - 4*p
# x = (-s +- sqrt(D))/2
#============================================================

# Для ввода чисел через консоль
# print(f"Введите X + Y = ")
# s = int(input())
# print(f"Введите X * Y = ")
# p = int(input())

#Сделан вывод всех возможных значений x и y в диапазоне до "length"

list_num = []
length = 10 #максимальное значение x и y
s = 1
p = 1
res_1 = 0
res_2 = 0
for s in range(1, 2*length+1): #ограничение на максимальную сумму
    for p in range(1, length*length+1):#ограничение на максимальное произведение
        d = s ** 2 - 4 * p  # Дискриминант
        if d >= 0:
            res_1 = (s + d**0.5) / 2
            res_2 = (s - d**0.5) / 2
            if res_1 <= length and res_2 <= length:
                if (res_1 == res_1 // 1) or (res_2 == res_2 // 1):  # Проверка на целочисленность
                    if res_1 > 0 and res_2 > 0:  # проверка на натуральность
                        t_res = (int(res_1), int(res_2))
                        print(f" X+Y={s} ; X*Y={p} => загаданы: X,Y = {t_res}")
#                     else:
#                         print("Решения - не натуральные числа")
#                 else:
#                     print("Решения - не целые числа")
#             else:
#                 print(f"Решения не могут быть больше {length}")
#         else:
#             print(f"Решений нет, D={d} < 0")

#==========================================================
# Вариант решения перебором
#==========================================================
# for x in range(1, length+1):
#     y = s - x
#     if x <= y and x * y == p:
#         print(x, y)
#==========================================================


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print("Введите максимальное число: ")
n = int(input())
base = 2
res = 0
i = 0
list_1 = list()
while res <= n:
    res = base**i
    if res <= n:
        list_1.append(res)
        i += 1

print(f"Степени двойки -> {list_1}")

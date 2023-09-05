# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list_in = [1, 1, 2, 0, -1, 3, 4, 4]

# list_in = [int(i) if i.isdigit() else i for i in input().split()]
# print(list_in)
# set_out = set(list_in)
# print(set_out)
# list_out = list(set_out)
# print(f'Количество уникальных элементов в {list_in} составляет {len(set_out)}: {list_out}')

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3] //эдесь не согласен - циклически считая сдвиг так не получается

# list_in = [1, 2, 3, 4, 5]
# print(list_in)
# print('Введите сдвиг: ')
# shift = int(input())
# while shift > len(list_in):
#     shift = shift - len(list_in)
# list_out = (list_in[len(list_in)-shift: len(list_in)] + list_in[0:len(list_in) - shift])
#         #print(list_in[len(list_in)-shift: len(list_in)] + list_in[0:len(list_in) - shift])
# print(f'Сдвинутый вправо список {list_in} на {shift} позиций: {list_out}')


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list_in = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
#            {" VIII ": "S007 "}]
# print(list_in)
# q = set()
# dict_elem = dict()
# for i in range(len(list_in)):
#     dict_elem = (list_in[i])
#     for (k, v) in dict_elem.items():
#         q.add(v)
# print(f'Уникальные значения в словаре:  {q}')


# Задача №23. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list_in = [0, -1, 5, 2, 3]
count = 0
list_out = list()
tup_out = tuple()
for i in range(len(list_in)):
    if list_in[i] > list_in[i-1]:
        tup_out = (list_in[i], list_in[i-1])
        list_out.append(tup_out)
        count += 1
print(f'В массиве {list_in}  {count} элемента(ов) больше предыдущего: ')
# print(list_out)
for i in range(len(list_out)):
    a, b = list_out[i]
    print(f'{a} > {b}')



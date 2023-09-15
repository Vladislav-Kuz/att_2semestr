# Задача 45
# Есть код:
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# if values == transformed_values:
#          print(‘ok’)
# else:
#          print(‘fail’)
#
# - В переменную transformation нужно прописать такую функцию, что бы в переменной transormed_values получилась копия списка values


# transformation = lambda x: x*x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#          print('ok')
# else:
#          print('fail')
#
# print(transformation)
# print(transformed_values)
#
#
# 2) - Дан список размеров(длина, ширина) эллипсов
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.


# def find_farthest_orbit(list_of_orbits):
#     pi = 3.14
#     # list_of_orbits = [pair for pair in list_of_orbits if pair[0] != pair[1]]
#     list_of_orbits = list(filter(lambda pair: pair[0] != pair[1], list_of_orbits))
#     areas_list = [pair[0] * pair[1] * pi for pair in list_of_orbits]
#     max_area = max(areas_list)
#     max_area_index = areas_list.index(max_area)
#     return list_of_orbits[max_area_index]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))



# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод:							            Вывод:
# values = [0, 2, 10, 6]		                same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)


# #  просто функция
# def same_by(characteristic, objects):
#     res_list = list()
#     for num in objects:
#         if characteristic(num):
#             res_list.append(num)
#     if objects == res_list or res_list == []:
#         return True
#     return False

# # функция высшего порядка
#
# def same_by(characteristic, objects):
#     res_list = list(map(characteristic, objects))
#     print(res_list)
#     if len(objects) == sum(res_list) or sum(res_list) == 0:
#         return True
#     return False


# Теперь FILTER


def same_by(characteristic, objects):
    res_list = list(filter(characteristic, objects))
    print(res_list)
    if objects == res_list or res_list == []:
        return True
    return False


values = [0, 2, 10, 6]
# values = [1, 3, 5, 7]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


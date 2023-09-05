#Задача 9 Факториал
# n = int(input())
# f=1
# while n>1:
#     f*=n
#     n-=1
# print(f)

# Задача No11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6
#
def fibonacci(num):
    a = 0
    b = 1
    i = 1
    while a <= num:
        if num == a:
            return 1
            break
        a = b
        b = a+b
        i += 1
    else:
        return -1


num = int(input('Input number: '))
print(fibonacci(num))

#
# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.#
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0

str = 'ОРРОРОРООРРРО'
n=0
print("РРР" in str)
while 'Р'*n in str:
    n+=1
print(n-1)

# Напишите
# программу, которая
# будет
# преобразовывать
# десятичное
# число
# в
# двоичное.
#
# *Пример: *
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10




# 1
# Задайте
# список
# из
# нескольких
# чисел.Напишите
# программу,
# # которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.
#
#
# *Пример: *
#
# - [2, 3, 5, 9, 3] -> на
# нечётных
# позициях
# элементы
# 3
# и
# 9, ответ: 12
#
# list=[2,5,3,6]
# for i in list:
#     if i%2!=0:
#
#
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
#
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton"
# (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
#
# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 5
# 5 до
# 100
# 100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
#
# Формат входных данных
# В первой строке подаётся число n
# n – количество холодильников. В последующих n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
#
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8
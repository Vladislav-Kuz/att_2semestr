# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
# **Вывод:** Парам пам-пам


# def count_syllables(list_phrase, ref_str): # первый вариант
#     count = 0
#     for letter in list_phrase:
#         if letter in ref_str:
#             count += 1
#     return count

def count_syllables(text, ref_str):
    res_sum = list()
    list_phrase = list(map(str, text.split()))
    for item in list_phrase:
        count = 0
        for letter in item:
            if letter in ref_str:
                count += 1
        res_sum.append(count)
    return res_sum


def is_rhythm(array_count):
    for i in range(len(array_count)):
        if array_count[0] != array_count[i]:
            return "Пам парам"
    return "Парам пам-пам"


if __name__ == '__main__':
    chant = 'пара-ра-рам рам-пам-папам па-па-ра-па-да'
    vowel_letters = 'ауеёыяиюоэ'

    lst_phrase = list(map(str, chant.split()))
    syllables_sum = count_syllables(chant, vowel_letters)
    # syllables_sum = list(count_syllables(item, vowel_letters) for item in lst_phrase) # первый вариант
    print(f'В кричалке "{chant}" всё {is_rhythm(syllables_sum)}')




# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
#
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            res = operation(i, j)
            print(res, end=' ')
        print()


print_operation_table(lambda x, y: x*y)
print()


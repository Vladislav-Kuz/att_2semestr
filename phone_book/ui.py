from logger import *
from data_remove import *
from data_modify import *


def interface():
    cmd = 0
    while cmd != '6':
        print('Выберете действие: \n'
              '1. Добавить контакт\n'
              '2. Вывести все контакты\n'
              '3. Поиск контакта\n'
              '4. Удаление контакта\n'
              '5. Изменение контакта\n'
              '6. Выход')
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print("Некорректный ввод")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                delete_data()
            case '5':
                modify_data()
            case '6':
                print("Всего доброго!")

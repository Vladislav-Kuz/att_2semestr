# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def enter_first_name():
    return input("Введите имя: ").capitalize()


def enter_sec_name():
    return input("Введите фамилию: ").capitalize()


def enter_phone():
    return input("Введите номер: ")


def enter_address():
    return input("Введите адрес: ").title()


def enter_data():
    name = enter_first_name()
    surname = enter_sec_name()
    phone = enter_phone()
    addr = enter_address()
    with open("book.txt", 'a', encoding='utf8') as file:
        file.write(f"{name} {surname} \n{phone} \n{addr}\n\n")


def print_data():
    with open("book.txt", 'r', encoding='utf8') as file:
        print(file.read())


def search_line():
    print('Выберете вариант поиска: \n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Телефон\n'
          '4. Адрес')
    index = int(input("Введите вариант: ")) - 1
    searched = input("Введите данные для поиска: ").title()
    with open("book.txt", 'r', encoding='utf8') as file:
        # print(file)
        # print([file.read()])    # отображает форматирование
        # # каретка переехала в конец
        # file.seek(0)  # перевод каретки в позицию 0
        # print(file.readlines()) # пустой список, разбивает на список
        # file.seek(0)  # перевод каретки в позицию 0
        # print(file.read().split('\n\n'))
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
            #     print(item)
            #     print()
                print(item, end='\n\n')



def interface():
    cmd = 0
    while cmd != '4':
        print('Выберете действие: \n'
            '1. Добавить контакт\n'
            '2. Вывести все контакты\n'
            '3. Поиск контакта\n'
            '4. Выход')
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4'):
            print("Некорректный ввод")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                print("Всего доброго!")


if __name__ == '__main__':
    interface()





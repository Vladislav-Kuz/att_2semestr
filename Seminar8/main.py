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
        file.write(f"\n{name} {surname} \n{phone} \n{addr}\n")


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
        print(data)
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                #     print(item)
                #     print()
                print(item, end='\n\n')


def delete_data():
    doubled_data = list()
    data_to_preview = list()
    new_data = list()
    searched = input("Введите данные контакта, подлежащего удалению: ").title()
    with open("book.txt", 'r', encoding='utf8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()  # Это список из элементов контакта
            if searched in new_item:
                doubled_data.append(new_item)  # список повторяющихся
                data_to_preview.append(item)
        if len(doubled_data) > 1:
            for index in range(len(doubled_data)):
                print(f"{index + 1} : {data_to_preview[index]}")
            print('Выберете вариант для удаления из списка: \n')
            index_variant = int(input(" ")) - 1  # Это уже индекс элемента на удаление
            deleted = doubled_data.pop(index_variant)  # Если deleted есть в data, то удалить
        for item in data:
            new_item = item.replace('\n', ' ').split()  # Это список из элементов контакта
            if new_item != deleted:
                new_data.append(item)
    with open("book.txt", 'w', encoding='utf8') as file:
        file.write('\n\n'.join(new_data))


def modify_data():
    doubled_data = list()
    data_to_preview = list()
    new_data = list()
    searched = input("Введите данные контакта, подлежащего изменению : ").title()
    with open("book.txt", 'r', encoding='utf8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()  # Это список из элементов контакта
            if searched in new_item:
                doubled_data.append(new_item)  # список повторяющихся
                data_to_preview.append(item)
        if len(doubled_data) > 1:
            for index in range(len(doubled_data)):
                print(f"{index + 1} : {data_to_preview[index]}")
            print('Выберете контакт для изменения из списка: \n')
            index_variant = int(input(" ")) - 1  # Это уже индекс элемента на удаление
            to_modify = doubled_data.pop(index_variant)  # Если deleted есть в data, то удалить
        for item in data:
            new_item = item.replace('\n', ' ').split()  # Это список из элементов контакта
            if new_item != to_modify:
                new_data.append(item)
            else:
                print('Выберете строку для изменения: \n'
                      '1. Имя\n'
                      '2. Фамилия\n'
                      '3. Телефон\n'
                      '4. Адрес')
                index = int(input("Введите вариант: ")) - 1
                to_modify = input("Введите новые данные: ").title()
                for i in range(len(new_item)):
                    if i == index:
                        new_item[i] = to_modify
                        new_data.append(new_item[0] + " " + new_item[1] + "\n" + new_item[2] + "\n" + new_item[3])
                        print(f"Добавлены новые данные в контакт: \n{new_item[0]}  {new_item[1]}\n{new_item[2]}\n"
                              f"{new_item[3]}")
    with open("book.txt", 'w', encoding='utf8') as file:
        file.write('\n\n'.join(new_data))


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


if __name__ == '__main__':
    interface()

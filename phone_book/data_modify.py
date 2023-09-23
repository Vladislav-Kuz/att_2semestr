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
            index_variant = int(input(" ")) - 1
            to_modify = doubled_data.pop(index_variant)  # получили измененное поле (строку)
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
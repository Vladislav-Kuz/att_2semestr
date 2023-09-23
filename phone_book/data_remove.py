
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

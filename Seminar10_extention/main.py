import copy

# Особенности работы со списками

# Это нужно смотреть по визуализатору

my_list = [1234,3456,5678,456, [345,567,345,23,
{'один': 1, 'два': 2, 'три': 3}]]

num = 34
num_1 = num

my_list_1 = my_list
my_list_1[3] = 0

print(my_list)
print(my_list_1)

my_list_2 = my_list.copy()

my_list_2[2] = '***'
my_list_2[-1][2] = 999
my_list_2[-1][4]['два'] = 222

print()
print(my_list)
print(my_list_2)

my_list_3 = copy.deepcopy(my_list)

my_tuple = (123,2345,456,2345,567, [1111,2222,333])

my_tuple[-1][1]=0



my_tuple = my_tuple = ([1,2,3,4,5],[111,222,333,444,555],[234,234,456,568,3456])

a, b, *c = my_tuple

for q,*w,e in my_tuple:
    print(q)
    print(w)
    print(e)


def create_contact():
    surname = surname_person()
    name = name_person()
    patronymic = patronymic_person()
    num_phone = num_phone_person()
    addres = region_addres_person()
    new_contact_str = f'{surname} {name} {patronymic}\n+7{num_phone}\nГород: {addres}'
    return new_contact_str


def enter_data():
    new_contact = create_contact()
    with open('book.txt', 'a', encoding='utf_8') as file:
        file.write(new_contact + "\n\n")


def change_line():
    search = input('Введите имя, фамилию, отчество, номер телефона или адрес: ').title()
    with open('book.txt', 'r', encoding='utf_8') as file:
        list_contacts = file.read().strip().split('\n\n')
        new_list_contacts = []
        for contact_str in list_contacts:
            if search not in contact_str:
                new_list_contacts.append(contact_str)
            else:
                print(f'Контакт найден:\n{contact_str}')
                check = input('Изменить контакт?\n' \
                              '1 - Да\n' \
                              '2 - Нет\n')
                if check == '1':
                    print('Введите новые данные:')
                    new_contact = create_contact()
                    new_list_contacts.append(new_contact)
                else:
                    new_list_contacts.append(contact_str)

    with open('book.txt', 'w', encoding='utf_8') as file:
        new_str_contacts = "\n\n".join(new_list_contacts)
        file.write(new_str_contacts)


def delete_line():
    search = input('Введите имя, фамилию, отчество, номер телефона или адрес: ').title()
    with open('book.txt', 'r', encoding='utf_8') as file:
        list_contacts = file.read().strip().split('\n\n')
        new_list_contacts = []
        for contact_str in list_contacts:
            if search not in contact_str:
                new_list_contacts.append(contact_str)
    with open('book.txt', 'w', encoding='utf_8') as file:
        new_str_contacts = "\n\n".join(new_list_contacts) + "\n\n"
        file.write(new_str_contacts)
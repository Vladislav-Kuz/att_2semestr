from datetime import datetime
from tabulate import tabulate
from os import path
import csv
import ui as ui

db_file = 'database.csv'
notebook = []
last_id = 0
headers = ['ID', 'Дата сохранения', 'Название', 'Текст']


def read_file():
    global notebook, db_file, last_id, headers
    while True:
        if path.exists(db_file):
            with open(db_file, mode='r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                notebook = [line for line in reader]
                if notebook[-1][0].isnumeric():
                    last_id = int(notebook[-1][0])
                else:
                    last_id = 0
            return notebook
        else:
            ui.show_error_file_message()
            ask_user = input('Создать новый файл? (y/n): ')
            if ask_user.lower() == 'y':
                with open(db_file, mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(headers)
                creator(0)
                print('Первая заметка создана')
                break
            elif ask_user.lower() == 'n':
                ui.show_exit_message()
                exit()
            else:
                ui.show_error_input_msg()


def write_file(new_db):
    with open(db_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for line in new_db:
            writer.writerow(line)


def add_data(new_data):
    with open(db_file, mode='a', encoding='utf-8', newline='\n') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(new_data)


def create_note():
    read_file()
    creator(0)
    print('Заметка создана')
    input(ui.waiting_msg)


def creator(flag):
    if flag == 0:
        id_num = last_id + 1
    else:
        id_num = flag
    note_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    note_title = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    if flag == 0:
        new_note = [str(id_num), note_date, note_title, note_text]
        add_data(new_note)
    else:
        notebook[flag] = [str(id_num), note_date, note_title, note_text]
        write_file(notebook)


def find_note(num_id):
    read_file()
    index_id = 0
    for i in range(1, len(notebook)):
        if notebook[i][0] == num_id:
            index_id = i
    return index_id


def show_all():
    show_notes_only()
    input(ui.waiting_msg)


def show_notes_only():
    read_file()
    result = [[line[i] for i in range(3)] for line in notebook]
    print(tabulate(result, tablefmt="simple_grid", stralign='center'))


def search_by_id():
    read_file()
    search = input('Введите ID записи: ')
    if search == '':
        ui.show_error_input_msg()
    else:
        result = searching(id_note=search)
        if len(result) == 0:
            print('Запись с таким ID не найдена.')
        else:
            print(tabulate(result, headers=headers, maxcolwidths=[None, None, None, 100], tablefmt="simple_grid"))
    input(ui.waiting_msg)


def search_by_date():
    read_file()
    search = input('Введите дату последнего сохранения \n'
                   '(в формате гггг-мм-дд): ')
    search_result = searching(date_note=search)
    if len(search_result) == 0:
        print('Запись с такой датой не найдена.')
    else:
        result = [[line[i] for i in range(4)] for line in search_result]
        print(tabulate(result, headers=headers, maxcolwidths=[None, None, None, 100], tablefmt="simple_grid"))
    input(ui.waiting_msg)


def searching(id_note='', date_note=''):
    result = []
    for row in notebook:
        if id_note != '' and row[0] != id_note:
            continue
        if date_note != '' and row[1].find(date_note):
            continue
        result.append(row)
    return result


def change_note():
    id_num = input('Введите ID редактируемой записи: ')
    ch_id_ind = find_note(id_num)
    if ch_id_ind == 0:
        print('Запись не найдена.')
    else:
        print('Запись найдена.')
        print(*notebook[ch_id_ind], sep='\t')
        ask_user = input("Подтвердите для доступа к изменению (y/n): ")
        if ask_user.lower() == 'y':
            creator(ch_id_ind)
            print(f'Запись с ID {id_num} изменена!')
            input(ui.waiting_msg)
        elif ask_user.lower() == 'n':
            print(f'Изменения записи с ID {id_num} отменены!')
            input(ui.waiting_msg)
        else:
            ui.show_error_input_msg()


def del_note():
    id_num = input('Введите ID удаляемой записи: ')
    del_id_index = find_note(id_num)
    if del_id_index == 0:
        print('Такой записи не найдено.')
    else:
        print(*notebook[del_id_index], sep='\t')
        ask_user = input("Удалить? (y/n): ")
        if ask_user.lower() == 'y':
            note_date = datetime.now().strftime("%Y-%m-%d %H:%M")
            notebook[del_id_index] = [str(id_num), '', f'<deleted {note_date}>', '']
            write_file(notebook)
            print(f'Заметка с ID {id_num} удалена!')
            input(ui.waiting_msg)
        elif ask_user.lower() == 'n':
            print(f'Удаление заметки с ID {id_num} отменено!')
            input(ui.waiting_msg)
        else:
            ui.show_error_input_msg()

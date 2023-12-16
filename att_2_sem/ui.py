from tabulate import tabulate


def show_menu():
    print("\nПрограмма для работы с заметками\n")
    print(tabulate([
                    [1, "Вывести все заметки"],
                    [2, "Поиск заметки по ID"],
                    [3, "Поиск заметки по дате"],
                    [4, "Создать новую заметку"],
                    [5, "Изменить существующую заметку"],
                    [6, "Удалить заметку"],
                    [0, "Выход из программы"]],
                   ["Выберите номер действия: "], "simple_grid"))

def show_exit_message():
    print(tabulate([["***** До новых встреч *****"]], tablefmt="simple_grid"))


def show_error_input_msg():
    print('Некорректный ввод.')


def show_error_file_message():
    print('Ошибка обращения к файлу ')


select_msg = 'Введите номер действия: '

waiting_msg = 'Для продолжения нажмите Enter'

import ui as ui
import commands as db


def operations():

    while True:
        ui.show_menu()
        user_command = input(ui.select_msg)
        if user_command == '0':
            ui.show_exit_message()
            exit()
        elif user_command == '1':
            db.show_all()
        elif user_command == '2':
            db.show_notes_only()
            db.search_by_id()
        elif user_command == '3':
            db.show_notes_only()
            db.search_by_date()
        elif user_command == '4':
            db.create_note()
        elif user_command == '5':
            db.show_notes_only()
            db.change_note()
        elif user_command == '6':
            db.show_notes_only()
            db.del_note()
        elif user_command not in ['0', '1', '2', '3', '4', '5', '6']:
            ui.show_error_input_msg()
            continue
        else:
            break

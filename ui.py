from commands import *
from os.path import exists

def interface():
    print('Заметки:')

    commands = ['r', 'f', 'o', 'c','e', 'd', 'q']
    filename = 'notes.csv'
    
    while True:

        if not exists(filename):
            create_file(filename)
        print('(команды: "r" - прочитать все, "f" - поиск по дате, "o" - открыть, "c" - создать, "e" - редактировать, "d" - удалить, "q" - выход)')
        command = input('Введите команду:')
        print()
        if command in commands:
            if command == 'q':
                print('Программа завершена.')
                break
            elif command == 'r':
                read_notes(filename)
            elif command == 'f':
                read_notesByDate(filename)    
            elif command == 'o':
                open_note(filename)
            elif command == 'c':
                create_note(filename)
            elif command == 'e':
                edit_note(filename)
            elif command == 'd':
                delete_note(filename)

        else:
            print('Неправильный ввод команды...')
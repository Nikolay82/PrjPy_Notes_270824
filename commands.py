from csv import DictWriter, DictReader
import datetime

def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Id', 'Heading', 'Body', 'Timestamp'])
        f_w.writeheader()


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

def standard_write(filename, lst_data):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Id', 'Heading', 'Body', 'Timestamp'])
        f_w.writeheader()
        f_w.writerows(lst_data)

def read_notes(filename):
    #Чтение всех заметок
    list_notes = read_file(filename)
    if len(list_notes) > 0:
        lenField_Id = 5
        lenField_Heading = 30
        print(f"Id{' ' * (lenField_Id - 2)}Заголовок{' ' * (lenField_Heading - 9)}Дата-время")
        for note in list_notes:
            print(f"{note['Id'] + ' ' * (lenField_Id - len(note['Id'])) + note['Heading'] + ' ' * (lenField_Heading - len(note['Heading'])) + note['Timestamp']}")
    else:
        print('Заметок нет!')
    print()

def read_notesByDate(filename):
    #Чтение всех заметок за дату
    list_notes = read_file(filename)
    if len(list_notes) > 0:
        print('Поиск заметок по дате:')
        strDateSearch = input('Введите дату в формате <ГГГГ-ММ-ДД>:')
        print()
        print('Заметки за ', strDateSearch)

        lenField_Id = 5
        lenField_Heading = 30
        print(f"Id{' ' * (lenField_Id - 2)}Заголовок{' ' * (lenField_Heading - 9)}Дата-время")
        for note in list_notes:
            if (strDateSearch in note['Timestamp']):
                print(f"{note['Id'] + ' ' * (lenField_Id - len(note['Id'])) + note['Heading'] + ' ' * (lenField_Heading - len(note['Heading'])) + note['Timestamp']}")
    else:
        print('Заметок нет!')
    print()

def open_note(filename):
    #Открытие выбранной заметки
    list_notes = read_file(filename)
    if len(list_notes) > 0:
        noteToOpen = None
        check_id = False
        while not check_id:
            idNoteToOpen = input(f'Введите Id заметки, которую хотите открыть:')
            if idNoteToOpen.isdigit():
                idNoteToOpen = int(idNoteToOpen)
                for note in list_notes:
                    if int(note['Id']) == idNoteToOpen:
                        noteToOpen = note
                        check_id = True
                        break
            if not check_id:
                print('Неправильный ввод Id...')
        print()
        print('Выбранная заметка:')
        print('Id:', noteToOpen['Id'])
        print('Заголовок:', noteToOpen['Heading'])
        print('Дата-время:', noteToOpen['Timestamp'])
        print('Текст заметки:', noteToOpen['Body'])
    else:
        print('Заметок нет!')
    print()


def create_note(filename):
    #Создание новой заметки
    print('Добавление новой заметки:')
    strHeadingNote = input('Введите заголовок:')
    strBodyNote = input('Введите текст заметки:')
    check_command = False
    
    print()
    while not check_command:
        print('Вы ввели следующие данные:')
        print('Заголовок:', strHeadingNote)
        print('Текст заметки:', strBodyNote)
        print()
        print('Подтверждаете?')

        command = input('"y" - да, "n" - нет:')
        if command in ['y', 'n']:
            check_command = True
        if not check_command:
            print('Неправильный ввод команды...')

    if command == 'y':
        today = datetime.datetime.today()
        strTimestampNote = today.strftime("%Y-%m-%d %H:%M:%S")
        
        list_notes = read_file(filename)
        if len(list_notes) > 0:
            newIdNote = int(list_notes[-1]['Id']) + 1
        else:
            newIdNote = 1

        objNote = {'Id': newIdNote, 'Heading': strHeadingNote, 'Body': strBodyNote, 'Timestamp': strTimestampNote}
        list_notes.append(objNote)
        standard_write(filename, list_notes)
        print('Новая заметка добавлена')
    else:
        print('Добавление новой заметки отменено...')
    print()

def edit_note(filename):
    #Редактирование выбранной заметки
    list_notes = read_file(filename)
    if len(list_notes) > 0:
        noteToEdit = None
        check_id = False
        while not check_id:
            idNoteToEdit = input(f'Введите Id заметки, которую хотите редактировать:')
            if idNoteToEdit.isdigit():
                idNoteToEdit = int(idNoteToEdit)
                for note in list_notes:
                    if int(note['Id']) == idNoteToEdit:
                        noteToEdit = note
                        check_id = True
                        break
            if not check_id:
                print('Неправильный ввод Id...')
        print()
        print('Выбранная заметка на редактирование:')
        print('Id:', noteToEdit['Id'])
        print('Заголовок:', noteToEdit['Heading'])
        print('Дата-время:', noteToEdit['Timestamp'])
        print('Текст заметки:', noteToEdit['Body'])
        print()

        strHeadingNote = input('Введите новый заголовок:')
        strBodyNote = input('Введите новый текст заметки:')
        print()
        check_command = False
        while not check_command:
            print('Вы ввели следующие данные:')
            print('Заголовок:', strHeadingNote)
            print('Текст заметки:', strBodyNote)
            print()
            print('Подтверждаете?')

            command = input('"y" - да, "n" - нет:')
            if command in ['y', 'n']:
                check_command = True
            if not check_command:
                print('Неправильный ввод команды...')

        if command == 'y':
            today = datetime.datetime.today()
            strTimestampNote = today.strftime("%Y-%m-%d %H:%M:%S")
            
            list_notes[list_notes.index(noteToEdit)]['Heading'] = strHeadingNote
            list_notes[list_notes.index(noteToEdit)]['Body'] = strBodyNote
            list_notes[list_notes.index(noteToEdit)]['Timestamp'] = strTimestampNote
            standard_write(filename, list_notes)
            print('Выбранная заметка изменена')
        else:
            print('Редактирование выбранной заметки отменено...')
    else:
        print('Редактировать нечего!')
    print()

def delete_note(filename):
    #Удаление выбранной заметки
    list_notes = read_file(filename)
    if len(list_notes) > 0:
        noteToDel = None
        check_id = False
        while not check_id:
            idNoteToDel = input(f'Введите Id заметки, которую хотите удалить:')
            if idNoteToDel.isdigit():
                idNoteToDel = int(idNoteToDel)
                for note in list_notes:
                    if int(note['Id']) == idNoteToDel:
                        noteToDel = note
                        check_id = True
                        break
            
            if not check_id:
                print('Неправильный ввод Id...')
        print()
        check_command = False
        while not check_command:
            print('Выбранная заметка на удаление:')
            print('Id:', noteToDel['Id'])
            print('Заголовок:', noteToDel['Heading'])
            print('Дата-время:', noteToDel['Timestamp'])
            print('Текст заметки:', noteToDel['Body'])
            print()
            print('Подтверждаете удаление?')

            command = input('"y" - да, "n" - нет:')
            if command in ['y', 'n']:
                check_command = True
            if not check_command:
                print('Неправильный ввод команды...')

        if command == 'y':
            list_notes.remove(noteToDel)

            standard_write(filename, list_notes)
            print('Выбранная заметка удалена')
        else:
            print('Удаление выбранной заметки отменено...')
    else:
        print('Удалять нечего!')
    print()
'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
'''

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while (choice != 7):
        if choice == 1:
            print_the_handbook(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            change_number(phone_book, last_name, new_number)
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            delete_record(phone_book, last_name)
        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите новые данные в формате [Фамилия] [Имя] [Номер] [Описание] через пробел: ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        choice=show_menu()

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            line = line.strip()
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def print_the_handbook(phone_book):
    for record in phone_book:
        print(', '.join(record.values()))

def find_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            return record
    return 'Запись не найдена'

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return 'Номер успешно изменен'
    return 'Запись не найдена'

def delete_record(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            return 'Запись успешно удалена'
    return 'Запись не найдена'

def find_by_number(phone_book, number):  
    for record in phone_book:
        if record['Телефон'] == number:
            return record
    return 'Запись не найдена'

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    return 'Пользователь успешно добавлен'

def write_txt(filename , phone_book):
    with open('phonebook.txt', 'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')        

def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep = '\n')
    choice = int(input())
    return choice

work_with_phonebook()
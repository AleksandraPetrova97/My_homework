# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def phone_book(): #введение нового человека
    last_name = input('фамилия: ')
    first_name = input('имя: ')
    patronymic = input('отчество: ')
    telephon = input('телефон: ')
    data = open('phonebook.txt', 'a', encoding='utf-8')
    data.writelines(f" {last_name} {first_name} {patronymic} {telephon}\n")
    data.close()

# phone_book()

def search(): #поиск человека
    look_people = input('Кого хотите найти: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if look_people in line:
                print(line)

# search()

def print_phonebook(): #печать всего справочника
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)

# print_phonebook()            

def load_book():
    new_phonebook = input('Введите ссылку: ')
    with open(new_phonebook, 'r', encoding='utf-8') as data:
        with open('phonebook.txt', 'a+', encoding='utf-8') as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            # data_1.write('\n')

# load_book()

def delete_person():
    name = int(input('Какую строку хотите удалить(нумерация с нуля): '))
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    del lines[name]    
    with open('phonebook.txt', "w", encoding='utf-8') as data:
        data.writelines(lines)    

# delete_person()

def delite_two():
    name = input('Кого хотите удалить? ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    with open('phonebook.txt', "w", encoding='utf-8') as data:
            for line in lines:
                if name not in line + "\n":
                    data.write(line)
 
# delite_two()

def changing_data():
    name = input(' Кого хотите изменить? ')
    new_name = input('Как изменяете: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines() 
    with open('phonebook.txt', "w", encoding='utf-8') as data:
            for line in lines:
                data.write(line.replace(name, new_name))

# changing_data()                    

print("""1 - Добавить нового человека в телефонный справочник,
2 - Найти человека в телефонном справочнике,
3 - Показать весь телефонный справочник,
4 - Импортировать информацию из другого телефонного справочника,
5 - Удалить информацию из справочника по номеру строки,
6 - Удалить информацию по данным человека,
7 - Изменить данные в справочнике:
 """)

what_do = int(input())

if what_do == 1:
    phone_book()
elif what_do == 2:
    search()
elif what_do == 3:
    print_phonebook()
elif what_do == 4:
    load_book()
elif what_do == 5:
    delete_person()
elif what_do == 6:
    delite_two()
elif what_do == 7:
    changing_data()
else: 
    "Такой команды нет"        
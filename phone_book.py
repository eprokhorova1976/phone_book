import re, string

#Создать контакт
def add_contact():
    book = open('phones.txt', 'r+', encoding = 'utf-8')
    name = input('Введите имя: ')
    number = input('Введите номер: ')
    number = re.sub (r'[-]', '', number)
    comment = input('Введите комментарий: ')
    id = len(book.readlines())+2
    book.write(f'\n{id}; {name}; {number}; {comment}')
    book.close()
    print (f'Контакт {name}, {number}, {comment} добавлен')
    menu()

#Открыть справочник, cкопировать контакты
def take_contacts():
    with open ('phones.txt', 'r+', encoding='utf-8') as book:
        return book.readlines()
      

#Показать все контакты
def show_contacts():
    book = open('phones.txt', 'r', encoding='utf-8')
    for line in book:
        print(line)
    menu()

#Найти контакт
def find_contact():
    book = take_contacts()
    what = input ('Введите номер параметра для поиска: 1-имя, 2-номер телефона, 3-комментарий: ')
    if what == '1':
        name = input ('Введите имя: ').lower()
        count = 0
        for contact in book:
            if name in contact.lower().split()[1]:
                print (contact)
                count +=1
        if count == 0:
            make_contact = input ('Такого имени в списке нет. Хотите добавить контакт? 1-да, 2-нет: ')
            if make_contact == '1':
                add_contact()
    elif what == '2':
        number = input ('Введите номер телефона: ')
        number = re.sub (r'[-]', '', number)
        count = 0
        for contact in book:
            if number in contact.split()[2]:
                print (contact)
                count +=1
        if count == 0:
            make_contact = input ('Такого номера телефона в списке нет. Хотите добавить контакт? 1-да, 2-нет: ')
            if make_contact == '1':
                add_contact()
    elif what == '3':
        comment = input ('Введите комментарий: ').lower()
        count = 0
        for contact in book:
            if comment in contact:
                print (contact)
                count +=1
        if count == 0:
            make_contact = input ('Такого комментария в списке нет. Хотите добавить контакт? 1-да, 2-нет: ')
            if make_contact == '1':
                add_contact()
            else:
                different_search = input ('Попробовать найти по другим параметрам? 1-да, 2-нет: ')   
                if different_search == '1':
                    find_contact() 
    else:
        print ('Вы выбрали несуществующий вариант. Попробуйте снова')
        find_contact()
    menu()
            
#Изменить контакт
        
#Удалить контакт
def delete_contact():
    book = take_contacts()
    what = input ('Какой контакт нужно удалить? Введите параметры для поиска: ').lower()
    count = 0
    for contact in book:
        if what in contact.lower().split()[1] or what in contact.split()[2] or what in contact.lower().split():
            print (contact)
            count +=1
    if count != 0:
        choose_contact = int(input ('Введите номер id удаляемого контакта: '))
        if choose_contact == contact [0]:
            book.pop (choose_contact)
            print (contact)
    if count == 0:
        different_search = input ('Такого контакта не нашлось. Попробовать найти по другим параметрам? 1-да, 2-нет: ')   
        if different_search == '1':
            delete_contact() 
    menu()


#Сохранить справочник
#Выход

#Меню
def menu():
    menu_book = input ('\nЭто телефонный справочник.\nВыберите подходящий пункт меню:\n1- Показать все контакты;\n2- Создать контакт;\n3- Найти контакт;\n4- Редактировать контакт;\n5- Удалить контакт;\n6- Выход\nВведите ваш вариант: ')
    if menu_book == '1':
        show_contacts()
    elif menu_book == '2':
        add_contact()
    elif menu_book =='3':
        find_contact()
    elif menu_book == '4':
        edit_contact()
    elif menu_book =='5':
        delete_contact()
    elif menu_book =='6':
        exit()

menu()

file = 'phonebook.txt'


def show_data() -> None:
    """Вывод инфо из телефонного справочника"""
    with open(file, 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    """Добавление инфо в телефонный справочник"""
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Запись добавлена')


# def find_data() -> None:
#     """Поиск инфо в телефонном справочнике"""
#     data = input('Введите данные для поиска: ')
#     with open(file, 'r', encoding='utf-8') as f:
#         tel_book = f.read()
#     print('Результаты поиска: ')
#     print(search(tel_book, data))


# def search(book: str, info: str):
#     book = book.split('\n')
#     return '\n'.join([post for post in book if info in post])


def find_data() -> None:
    """Поиск инфо в телефонном справочнике"""
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    contact_to_find = input('Введите данные для поиска: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def edit_data() -> None:
    """Изменение записи в телефонном справочнике"""
    with open(file, 'r', encoding='utf-8') as f:
        tel_book = f.read()
    tel_book = tel_book.split('\n')
    num = int(input('Введите номер записи, которую хотите изменить: '))
    tel_book[num] = edited(tel_book[num])
    tel_book = '\n'.join(tel_book)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(tel_book)
    print(tel_book)


def edited(text: str):
    fio = input('Введите ФИО: ')
    number = input('Введите номер телефона: ')
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(number) == 0:
        number = text.split(' | ')[1]
    return f'{fio} | {number}'


def del_data() -> None:
    """Удаление записи из телефонного справочника"""
    with open(file, 'r', encoding='utf-8') as f:
        tel_book = f.read()
    tel_book = tel_book.split('\n')
    num = int(input('Введите номер записи, которую хотите удалить: '))
    tel_book.pop(num)
    tel_book = '\n'.join(tel_book)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(tel_book)
    print(tel_book)

welcome = 'Hi!  Привет!'
select_a_language = 'Select a language/Привет, выбери язык: 0 = English, 1 = Русский: '

class RusText:

    main_menu = ['Главное меню',
                'Открыть файл',
                'Сохранить файл',
                'Показать контакты',
                'Создать контакт',
                'Найти контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Выход']


    main_menu_choice = 'Выберите пункт меню: '

    load_successful = 'Телефонная книга успешно загружена !'

    safe_successful = 'Телефонная книга успешно сохранена !'

    empty_phone_book = 'Телефонная книга пуста или не открыта'

    new_contact = ['Введите имя: ', 'Введите номер телефона: ', 'Введите комментарий: ']

    def new_contact_added_successful(self, name):
        return f'Контакт {name} успешно добавлен !'

    input_search_word = 'Введите слово для поиска: '

    def contacts_not_found(self, word):
        return f'Контакты содержащие {word} не найдены!'

    input_id_change_contact = 'Введите ID контакта, который хотите изменить: '

    change_contact = ['Введите новое имя или ENTER, если оставить без изменений: ',
                    'Введите новый телефон или ENTER, если оставить без изменений: ',
                    'Введите новый комментарий или ENTER, если оставить без изменений: ']

    def contact_changed_successful(self, name):
        return f'Контакт {name} успешно изменён!'

    input_id_delete_contact = 'Введите ID контакта, который хотите удалить: '

    def not_available_id(self, digit: int):
        return f'Вы ввели не существующий ID, введите число не более {digit} :'

    def contact_deleted_successful(self, name):
        return f'Контакт {name} успешно удален!'

    good_bay = 'До новых встреч!'
    
class EngText:

    main_menu = ['Main Menu',
                'Open a file',
                'Save the file',
                'Show contacts',
                'Create a contact',
                'Find a contact',
                'Change a contact',
                'Delete a contact',
                'Exit']


    main_menu_choice = 'Select a menu item: '

    load_successful = 'The phone book has been uploaded successfully!'

    safe_successful = 'The phone book has been saved successfully!'

    empty_phone_book = 'The phone book is empty or not open'

    new_contact = ['Enter a name: ', 'Enter the phone number: ', 'Enter a comment:']

    def new_contact_added_successful(self, name):
        return f'Contact {name} successfully added!'

    input_search_word = 'Enter the search word: '

    def contacts_not_found(self, word):
        return f'Contacts containing {word} not found!'

    input_id_change_contact = 'Enter the ID of the contact you want to change: '

    change_contact = ['Enter a new name or ENTER if you leave it unchanged: ',
                    'Enter a new phone or ENTER if you leave it unchanged: ',
                    'Enter a new comment or ENTER if you leave it unchanged: ']

    def contact_changed_successful(self, name):
        return f'Contact {name} successfully changed!'

    input_id_delete_contact = 'Enter the ID of the contact you want to delete: '

    def not_available_id(self, digit: int):
        return f'You have entered a non-existing ID, enter a number no more {digit} :'

    def contact_deleted_successful(self, name):
        return f'Contact {name} successfully deleted!'

    good_bay = 'See you!'    
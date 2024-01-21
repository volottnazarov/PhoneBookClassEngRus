
import text

def main_menu(dig: int):
    if dig == 1:
        lang = text.RusText
    else:
        lang = text.EngText    
    for n, item in enumerate(lang.main_menu):
        if n == 0:
            print(item)
        else:
            print(f'\t {n}. {item}')
    while True:
        choice = input(lang.main_menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(lang.main_menu):
            return int(choice)
        print(f'Enter the menu item from 1 to/Введите пункт меню от 1 до {len(lang.main_menu) - 1}')  
        
def show_contact(p_book: dict[int, list[str]], error_message: str):
    max_size = list(map(lambda x: len(max(x, key=len)), list(zip(*p_book.values()))))
    if p_book:
        print('\n' + '=' * (sum(max_size) + 7))
        for n, contact in p_book.items():
            print(f'{n:>3}. {contact[0]:<{max_size[0]}} {contact[1]:<{max_size[1]}} {contact[2]:<{max_size[2]}}')
        print('=' * (sum(max_size) + 7) + '\n')     
    else:
        print_message(error_message)
                
def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')   
                 
def add_contact(message: list[str], contact: list[str] = None):
    contact = contact if contact else ['', '', '']
    for n, mes in enumerate(message):
        field = input(mes)
        contact[n] = field if field else contact[n]
    return contact   

def input_data(message: str):
    return input(message)
      
            
                   
    
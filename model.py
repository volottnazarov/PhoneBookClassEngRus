﻿# Наша бизнес логика. Как хранятся данные, как обрабатываются, как они работают.

phone_book = {}
path = 'phone_book.txt'
SEPARATOR = ';'  # CapsLock'ом пишеи константы, кот. не изменяются

def open_file():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = {i: item for i, item in 
                      enumerate(list(map(lambda x: x.strip().split(SEPARATOR), file.readlines())), 1)}  
        # map применяет функцию strip(она убирает значки \n)для каждого элемента списка file
    

def safe_file():
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(SEPARATOR.join(contact))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def next_id():
    global phone_book
    return (max(phone_book) + 1) if phone_book else 1

def new_contaсt(contact: list[str]):
    global phone_book
    phone_book[next_id()] = contact
    
def find_contact(word: str):
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if word.lower() in str(contact).lower(): 
            result[u_id] = contact
    return result   

def change_contact(c_id: int, c_contact: list[str]):
    global phone_book
    phone_book[c_id] = c_contact
          
def delete_contact(c_id: int):
    global phone_book
    return phone_book.pop(c_id)
    
              
    
       
        
        
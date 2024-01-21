﻿        
class PhoneBook:
    def __init__(self, path: str = 'phone_book.txt', separator: str = ';'):
        self.phonebook = {}
        self.path = path
        self.separator = separator
                        

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            self.phonebook = {i: item for i, item in 
                      enumerate(list(map(lambda x: x.strip().split(self.separator), file.readlines())), 1)} 
            
    def total_id(self):
        total = 0
        with open(self.path, 'r', encoding='UTF-8') as file:
            for line in file:
                total += 1
        return total            
                
    def safe_file(self):
        data = []
        for contact in self.phonebook.values():
            data.append(self.separator.join(contact))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def next_id(self):
        return (max(self.phonebook) + 1) if self.phonebook else 1

    def new_contaсt(self,contact: list[str]):
        self.phonebook[self.next_id()] = contact
        
    def find_contact(self, word: str):
        result = {}
        for u_id, contact in self.phonebook.items():
            if word.lower() in str(contact).lower(): 
                result[u_id] = contact
        return result

    def change_contact(self, c_id: int, c_contact: list[str]):
        self.phonebook[c_id] = c_contact
            
    def delete_contact(self, c_id: int):
        return self.phonebook.pop(c_id)
    
        
              
    
       
        
        
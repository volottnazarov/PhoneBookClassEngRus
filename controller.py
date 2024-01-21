import text
import view
import model

view.print_message(text.welcome)
lang_dig = int(view.input_data(text.select_a_language))
if lang_dig == 0:
    lang = text.EngText()
else:
    lang = text.RusText()   
def find_contact(phones: model.PhoneBook):
    word = view.input_data(lang.input_search_word)
    result = phones.find_contact(word)
    view.show_contact(result, lang.contacts_not_found(word))
    
def start_app():        
    pb = model.PhoneBook() 
    total = 0  
    while True:
        choice = view.main_menu(lang_dig)
        match choice:
            case 1:
                pb.open_file()
                view.print_message(lang.load_successful)
                total = int(pb.total_id())
            case 2:
                pb.safe_file()
                view.print_message(lang.safe_successful)
            case 3:
                view.show_contact(pb.phonebook, lang.empty_phone_book)
            case 4:
                contact = view.add_contact(lang.new_contact)
                pb.new_contaсt(contact)
                view.print_message(lang.new_contact_added_successful(contact[0]))
            case 5:
                find_contact(pb)
            case 6:
                find_contact(pb)
                while True:
                    c_id = int(view.input_data(lang.input_id_change_contact))
                    if c_id <= total:
                        c_contact = view.add_contact(lang.change_contact, pb.phonebook[c_id])
                        pb.change_contact(c_id, c_contact)
                        view.print_message(lang.contact_changed_successful(c_contact[0]))
                        break
                    else:
                        view.print_message(lang.not_available_id(total))    
            case 7:
                find_contact(pb)
                while True:
                    c_id = int(view.input_data(lang.input_id_delete_contact))
                    if c_id <= total:
                        name = pb.delete_contact(c_id)[0]
                        view.print_message(lang.contact_deleted_successful(name))
                        break
                    else:
                        view.print_message(lang.not_available_id(total))             
            case 8:
                view.print_message(lang.good_bay)
                break
        
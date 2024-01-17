# Связующая часть между model и view
import text
import view
import model

def find_contact():
    word = view.input_data(text.input_search_word)
    result = model.find_contact(word)
    view.show_contact(result, text.contacts_not_found(word))
    
def start_app():    
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.load_successful)
            case 2:
                model.safe_file()
                view.print_message(text.safe_successful)
            case 3:
                pb = model.phone_book
                view.show_contact(pb, text.empty_phone_book)
            case 4:
                contact = view.add_contact(text.new_contact)
                model.new_contaсt(contact)
                view.print_message(text.new_contact_added_successful(contact[0]))
            case 5:
                find_contact()
            case 6:
                find_contact()
                pb = model.phone_book
                c_id = int(view.input_data(text.input_id_change_contact))
                c_contact = view.add_contact(text.change_contact, pb[c_id])
                model.change_contact(c_id, c_contact)
                view.print_message(text.contact_changed_successful(c_contact[0]))
            case 7:
                find_contact()
                c_id = int(view.input_data(text.input_id_delete_contact))
                name = model.delete_contact(c_id)[0]
                view.print_message(text.contact_deleted_successful(name))
            case 8:
                view.print_message(text.good_bay)
                break
        
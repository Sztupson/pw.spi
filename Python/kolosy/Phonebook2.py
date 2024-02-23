import logging

# Konfiguracja logowania
logging.basicConfig(filename='book.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

filename = "book.txt"

phone_number = input("Enter phone number: ")


def read_phonebook():
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(' ; ') for line in file.readlines()] 
    except FileNotFoundError:
        return "File not found."

def save_phonebook(phonebook):
    with open(filename, 'r') as file:
        file.write(f'{phonebook}\n')
    return [f"Phonebook saved to file {filename}"]

def display_phonebook():
    for list in read_phonebook():
        return list

def validate_phone_number(phone_number:str):
    if phone_number.isdigit() and len(phone_number) == 9:
        return "Phone number is correct."
    else:
        return False
    
def add_entry(name, phone_number:str):
    if validate_phone_number(phone_number) == False:
        return "Enter valid phone number."
    add_new = f"{name};{phone_number}"
    save_phonebook(add_new)
    return "New user added."

def remove_entry(phone_number):
    for entry in read_phonebook():
        if phone_number not in entry:
                logging.warning("Attempted to remove a phone number that does not exist.")
                return False

def modify_entry(old_phone_number, new_name, new_phone_number):
    if not validate_phone_number(new_phone_number):
        print("Attempted to add invalid phone number.")
        return False
    lista = read_phonebook()
    for key,row in enumerate(lista):
        if old_phone_number in row:
            lista[key] = f"{new_name}; {new_phone_number}"
            save_phonebook(lista)
            print("Saved new user.")
            return True    
    return

read_phonebook()
add_entry("Krzysztof", "123456789")
display_phonebook()
modify_entry("123456789","Natalia", "000000000")
remove_entry("123456789")
display_phonebook()
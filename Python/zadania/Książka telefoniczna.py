FILENAME = "book.txt"


def read_phonebook():
    with open(FILENAME,'r') as file:
        for line in file.readlines():
            return line.strip().split(';')
    except FileNotFoundError:
    return []

# Czyta dane z pliku i zwraca je w postaci listy.

def save_phonebook(phonebook):
    with open(FILENAME, 'w') as file:
        for entry in phonebook:
            file.write(f"{phonebook}\n")
        print("Save file.")

# Zapisuje dane książki telefonicznej do pliku.

def display_phonebook():
    for list in read_phonebook():
        return [list]

# Wyświetla aktualną zawartość książki telefonicznej.

def validate_number(phone_number:str):
    return len(phone_number) == 9 and phone_number.isdigit()

def add_entry(name, phone_number:str):
    if not phone_number.isdigit() or len(phone_number) != 9:
        print("Invalid phone number.")
        return
    add_new = f"{name} ; {phone_number}"
    save_phonebook(add_new)
    print("Added phone number.")

# Dodaje nowy wpis do książki telefonicznej z podaną nazwą i numerem telefonu.
# Sprawdza format numeru oraz czy numer już istnieje.

def remove_entry(phone_number):
    nowa_lista = []
    for entry in read_phonebook():
        if phone_number not in entry:
            nowa_lista.append(entry)
    save_phonebook(nowa_lista)
    # save_phonebook([entry for entry in read_phonebook() if phone_number not in entry])
    # ^ to samo tylko w jednej linijce

# Usuwa wpis na podstawie numeru telefonu.

def modify_entry(old_phone_number, new_name, new_phone_number):
    if not validate_number(new_phone_number):
        print("Invalid phone number.")
        return False
    lista = read_phonebook()

    for key, row in enumerate(lista):
        if old_phone_number in row:
            lista[key] = f"{new_name} ; {new_phone_number}"
            save_phonebook(lista)
            print("Save")
            return True
    return
# Modyfikuje istniejący wpis, pozwalając na zmiane nazwy i numeru telefonu.

read_phonebook
display_phonebook()
add_entry("Krzysztof", "123456789")
display_phonebook()


while True
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exit")
        break
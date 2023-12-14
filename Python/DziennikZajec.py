# Zadanie : Prosty Dziennik Zajęć
# Cel: Napisz program służący jako dziennik zajęć. Użytkownik powinien móc dodawać, edytować i us uwać zaplanowanezadania oraz zapisywać je w pliku.
# Funkcje:

#     Dodawanie nowego zadania.
#     Edytowanie istniejącego zadania.
#     Usuwanie zadania.
#     Zapisywanie zadań do pliku.
#     Odczytywanie zadań z pliku.

# class StudentRegister:
import datetime
import os
filename = "tasks.txt"

def add_tasks():
    pass

def edit_tasks():
    pass

def del_tasks():
    pass

def save_tasks_to_file():
    pass

def read_tasks_from_file(filename):
    try:
        if os.path.exists(filename):
            return True
    except FileNotFoundError:
        print("File does not exist.")
        return
    
    with open(filename, 'r') as f:
        f = f.readlines
        return []
    

# task_deadline = datetime.datetime
print(read_tasks_from_file(filename))
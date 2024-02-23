import os
filename = "tasks.txt"

def read_tasks_from_file():
    tasks = {}
    try:
        if os.path.exists(filename):
            pass
        with open(filename, 'r') as f:
            for line in f:
                task_name, task_description = line.strip().split(":")
                tasks[task_name] = task_description
    except FileNotFoundError:
        return "File does not exist."
    return tasks

def add_tasks(task_name, task_description):
    tasks = read_tasks_from_file()
    if task_name in tasks.keys():
        print("Enter another name for your task. This one is already in use.")
        return
    else:
        tasks[task_name] = task_description
        save_tasks_to_file(tasks)
        return "Task added."

def save_tasks_to_file(task:dict):
    with open(filename, 'w') as f:
        for task_name, task_description in task.items():
            f.write(f"{task_name}: {task_description}\n")
    return "Task saved successfully"

def del_tasks(task_name):
    tasks = read_tasks_from_file()
    if task_name in tasks:
        del tasks[task_name]
        save_tasks_to_file(tasks)
        print("Task removed.")
    else:
        print("Task not found.")

def display_tasks():
    tasks = read_tasks_from_file()
    for task_name, task_description in tasks.items():
        print(f"{task_name}: {task_description}")
    return "____________"

def edit_tasks(old_task, new_task, new_description):
    tasks = read_tasks_from_file()
    if old_task in tasks:
        del_tasks(old_task)
        add_tasks(new_task, new_description)
    else:
        print("Task does not exist.")
        return
    
# SPRAWDZENIE DZIAŁANIA
add_tasks("Zadanie 1", "Napisz")
print(display_tasks())
add_tasks("Zadanie 1", "taki sam numer zadania jak w porzednim")
print(display_tasks())

edit_tasks("Zadanie 1", "Kolokwium", "Napisz prosta ksiazke telefoniczna")
print(display_tasks())

del_tasks("Kolokwium")
print(display_tasks())
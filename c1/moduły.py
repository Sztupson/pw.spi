import math

print(math.sqrt(10))

import random

# Generowanie losowej liczby całkowitej z zakresu 1-100:
print(random.randint(1, 100))

# Wybór losowego elementu z listy:
fruits = ["apple", "banana", "orange"]
print(random.choice(fruits))

# Mieszanie listy
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Zwrócenie bieżącego czasu w sekundach:
import time
print(time.time())



# Napisz kod, który wypisze listę wszystkich plików w bieżącym katalogu.
# import os

# for file in os.listdir():
#     print(file)
# # os.mknod("nowy_plik.txt")
# file_path = "request.py"
# if os.path.exists(file_path):
#     print("File already exists.")

# print(os.path.isfile(file_path))

# print(os.listdir(file_path))

# os.rename(file_path, file_path+"nowy_plik.txt")

# os.mkdir("nowy_katalog")
# os.rmdir("nowy_katalog")

# with open("nowy_plik.txt", "w") as f:
#       f.write(("To jest nowy plik."))
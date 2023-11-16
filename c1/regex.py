# python -m ensurepip --upgrade
# pip install regex

import re

txt = "Dopasowuje pozycję, która nie jest granicą słowa."

x = re.search("^Dopasowuje.*słowa.$", txt)

print(x)

# findall - Zwraca listę zawierającą wszystkie wystąpienia.
# search - Zwraca obiekt match, jeśli w dowolnym miejscu znajdzie dopasowanie.
# split - Zwraca listę, w której ciągu znaków został podzielony przy każdym dopasowaniu.
# sub - Zastępuje jedno lub więcej wystąpień.

# [] - Dopasowuje każdy pojedynczy znak w nawiasach.
# [a-z] - Zwraca dopasowania pasujące do wzoru od a-z, małe litery
# [a-k]
# [a-zA-Z]
# [0-9]
# [678]
# [^michal] -> c
# 00-62
# [0-6][0-9] -> 56 / 72(nie pasuje)
# [+]


txt = "Dopnieas nie asdwnieas wasnie nie kupnielem"
x = re.findall("nie",txt)
print(x)
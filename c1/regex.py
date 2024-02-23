# python -m ensurepip --upgrade
# pip install regex

# import re

# txt = "Dopasowuje pozycję, która nie jest granicą słowa."

# x = re.search("^Dopasowuje.*słowa.$", txt)

# print(x)

# # # findall - Zwraca listę zawierającą wszystkie wystąpienia.
# # # search - Zwraca obiekt match, jeśli w dowolnym miejscu znajdzie dopasowanie.
# # # split - Zwraca listę, w której ciągu znaków został podzielony przy każdym dopasowaniu.
# # # sub - Zastępuje jedno lub więcej wystąpień.

# # # [] - Dopasowuje każdy pojedynczy znak w nawiasach.
# # # [a-z] - Zwraca dopasowania pasujące do wzoru od a-z, małe litery
# # # [a-k]
# # # [a-zA-Z]
# # # [0-9]
# # # [678]
# # # [^michal] -> c
# # # 00-62
# # # [0-6][0-9] -> 56 / 72(nie pasuje)
# # # [+]


# txt = "Dopnieas nie asdwnieas wasnie nie kupnielem."
# x = re.findall("nie",txt)
# print(x)

# x=re.split("\s",txt,1)
# print(x)

# x = re.sub("nie","WOW", txt)
# print(x)

# x=re.findall(r"\bnie\b", txt)
# print(x)

# x=re.findall(r"[\w\.]+", txt)
# print(x)

# mail = "wiktor.sztupecki@pw.edu.pl"
# x = re.split("@", mail)
# x = re.match("^[\w\.]+@[\w\.]+", mail)
# print(bool(x))

# txt1 = "rok 2023 bedzie lepszy"
# x = re.sub("\d", "X",txt1)
# print(x)

# x = re.findall(r"\b[n]\w+", txt)
# print(x)

# kot = "Nasz kot ma 60 lat i waży 4 kg."
# x = re.findall(r"\d+", kot)
# print(x)

# x = re.search(r"^nasz", kot, re.IGNORECASE)
# print(x)


# text = "Mój numer to 605-456-7890"
# x = re.search(r"\d{3}-\d{3}-\d{4}", text)
# print(x)

# x = re.search(r"\b[4-8][0-9]{2}-\d{3}-\d{4}", text)
# print(x)

# link = "Odwiedź https://www.example.com i http://www.anotherdomain.org."
# domain_names = re.findall(r"https?://www\.(\w+)", link)
# print(domain_names)

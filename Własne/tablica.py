
# def wypisz_nieparzyste_parzyste_1_2(tab, rows, cols):
#     for r in range(rows):
#         start=0
#         for c in range(start, cols, 2):
#             tab[r][c] = 2
#     for r in range(rows):
#         start = 1
#         for c in range(start,cols,2):
#             tab[r][c] = 1
#     print(tab)
# tab = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# print(wypisz_nieparzyste_parzyste_1_2(tab, 3, 5))



def zeros(r,c):
    tab = []
    for i in range(r):
        tab.append([0 for i in range(c)])
    return tab

def wypisz(tab):
    for i in range(len(tab)):
        print(tab[i])

def polacz(t1, t2, d1, d2):
    t = zeros(d1+d2, d1+d2)
    for r in range(d1):
        for c in range(d1):
            t[r][c] = t1[r][c]
    for r in range(d2):
        for c in range(d2):
            t[r+d1][c+d1] = t2[r][c]
    return t


t1 = [
[1, 2, 3],
[1, 2, 3],
[1, 2, 3]
]
t2 = [
[1, 2, 3, 4],
[1, 2, 3, 4],
[1, 2, 3, 4],
[1, 2, 3, 4]
]
t = zeros(7, 7)
wypisz(t)
print("-------------------------------------------")
t = polacz(t1, t2, 3, 4)
wypisz(t)
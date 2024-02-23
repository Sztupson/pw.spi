# Napisz fukncje w pythonie, ktora przyjmje liczbe calkowita jako argument i zwraca liste wszystkich jej dzielnikow 

# wejscie - 1 liczba calkowita
# wyjscie lista/tablica



def find_div(number):
    div = []
    for i in range(1, number+1):
        if number % i == 0:
            div.append(i)
    print(div)
find_div(1000)
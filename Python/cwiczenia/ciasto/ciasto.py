import json




def read_from_file(nazwa_pliku, nazwa):
    try:
        with open(nazwa_pliku, 'r', encoding = 'utf8') as file:
            dane = json.load(file)
            if nazwa == dane["nazwa"]:
                return dane
    except FileNotFoundError:
        return False

def pokaz_przepis(przepis):
    print(f"Przepis na ciasto{przepis["nazwa"]}")
    for skladniki, dane in przepis["skladniki"].items():
        print(f"-{skladniki}:{dane["ilosc"]} {dane["jednostka"]}")

def dodaj_ciasto(ciasto):
    przepis["nazwa"] = ciasto
    return przepis


def dodaj_skladnik(skladnik, ilosc, jednostka):
    przepis["skladniki"][skladnik] = {
        "ilosc": ilosc,
        "jednostka": jednostka
    }

def save_to_file(nazwa_pliku, przepis):
    with open(nazwa_pliku, "w") as file:
        return json.dump(przepis, file, indent=4)

# przepis = read_from_file("ciasto.json", "Jabłecznik")
# pokaz_przepis(przepis)

ciasto = {}
dodaj_ciasto("Czekoladowe")
dodaj_skladnik(ciasto, )

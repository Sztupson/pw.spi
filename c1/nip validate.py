




def validate_nip(nip:str):
    wagi = [6,5,7,2,3,4,5,6,7]
    suma = 0

    # spawdzamy czy mamy 10
    # sprawdzamy czy wszystkie sa cyframi

    if len(nip) != 10:
        return False
    if nip.isdigit():
        return False
    suma = 0
    for i in range(9):
        suma += int(nip[i]) * wagi[i]
    if suma%11 == 10 and suma%11 != nip[9]:
        return False
    return True

if validate_nip('7742704378'):
    print('NIP prawidłowy.')
else:
    print('NIP nieprawidłowy.')
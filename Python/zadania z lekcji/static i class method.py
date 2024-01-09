class Matematyka:

    szerokosc = 0
    dlugosc = 0
    
    def __init__(self, szerokosc, dlugosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def mydecorator(self, func):
        def wrapper(self):
            print(f"Początek funkcji.")
            print (func(self))
            print(f"Koniec funkcji.")
        return wrapper

    @classmethod
    def kwadrat(cls, bok):
        return cls(bok, bok)
    
    @mydecorator
    def pole(self):
        return self.szerokosc * self.dlugosc

m = Matematyka(4,5)
m.pole()
import threading
import time
from collections import deque

class Magazyn:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.produkty = deque()
        self.producenci = []
        self.konsumenci = []

    def dodaj_obserwatora_producenta(self, producent):
        self.producenci.append(producent)

    def dodaj_obserwatora_konsumenta(self, konsument):
        self.konsumenci.append(konsument)

    def jest_miejsce(self):
        return len(self.produkty) < self.pojemnosc

    def sa_produkty(self):
        return len(self.produkty) > 0

    def dodaj_produkt(self, produkt):
        if self.jest_miejsce():
            self.produkty.append(produkt)

    def usun_produkt(self):
        if self.sa_produkty():
            return self.produkty.popleft()
        return None

    def powiadom_producentow(self):
        for producent in self.producenci:
            producent.produkuj(self)

    def powiadom_konsumentow(self):
        for konsument in self.konsumenci:
            konsument.konsumuj(self)

class Producent:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.counter = 0

    def produkuj(self, magazyn):
        if magazyn.jest_miejsce():
            self.counter += 1
            produkt = f"{self.nazwa}-{self.counter}"
            magazyn.dodaj_produkt(produkt)
            print(f"{self.nazwa} wyprodukowal: {produkt}")

class Konsument:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def konsumuj(self, magazyn):
        if magazyn.sa_produkty():
            produkt = magazyn.usun_produkt()
            print(f"{self.nazwa} skonsumowal: {produkt}")

def main():
    pojemnosc_magazynu = 5
    liczba_producentow = 2
    liczba_konsumentow = 2

    magazyn = Magazyn(pojemnosc_magazynu)

    producenci = [Producent(f"P{i + 1}") for i in range(liczba_producentow)]
    konsumenci = [Konsument(f"K{i + 1}") for i in range(liczba_konsumentow)]

    for producent in producenci:
        magazyn.dodaj_obserwatora_producenta(producent)

    for konsument in konsumenci:
        magazyn.dodaj_obserwatora_konsumenta(konsument)

    def run_magazyn():
        while True:
            if magazyn.jest_miejsce():
                magazyn.powiadom_producentow()
            if magazyn.sa_produkty():
                magazyn.powiadom_konsumentow()
            time.sleep(2)

    watek_magazyn = threading.Thread(target=run_magazyn)
    watek_magazyn.start()

if __name__ == "__main__":
    main()

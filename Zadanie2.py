from abc import ABC, abstractmethod

class Komponent(ABC):
    @abstractmethod
    def wyslij(self, wiadomosc):
        pass

class Uzytkownik(Komponent):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def wyslij(self, wiadomosc):
        print(f"Wiadomość do {self.nazwa}: {wiadomosc}")

class Grupa(Komponent):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.komponenty = []

    def dodaj(self, komponent):
        self.komponenty.append(komponent)

    def usun(self, komponent):
        self.komponenty.remove(komponent)

    def wyslij(self, wiadomosc):
        print(f"Grupa {self.nazwa} rozsyła wiadomość: {wiadomosc}")
        for komponent in self.komponenty:
            komponent.wyslij(wiadomosc)

if __name__ == "__main__":
    grupa_glowna = Grupa("Grupa_Glowna")
    uzytkownicy = [Uzytkownik(f"Uzytkownik{i + 1}") for i in range(3)]
    for uzytkownik in uzytkownicy:
        grupa_glowna.dodaj(uzytkownik)

    print("\nTest 1: Struktura plaska")
    grupa_glowna.wyslij("Witajcie w grupie plaskiej!")

    podgrupa1 = Grupa("Podgrupa1")
    podgrupa2 = Grupa("Podgrupa2")

    for i in range(2):
        podgrupa1.dodaj(Uzytkownik(f"Podgrupa1_Uzytkownik{i + 1}"))
    for i in range(3):
        podgrupa2.dodaj(Uzytkownik(f"Podgrupa2_Uzytkownik{i + 1}"))

    zagniezdzona_grupa = Grupa("GrupaZagniezdzona")
    zagniezdzona_grupa.dodaj(Uzytkownik("Zagniezdzony_Uzytkownik1"))
    podgrupa2.dodaj(zagniezdzona_grupa)

    grupa_glowna.dodaj(podgrupa1)
    grupa_glowna.dodaj(podgrupa2)

    print("\nTest 2: Struktura hierarchiczna")
    grupa_glowna.wyslij("Witajcie w grupie hierarchicznej!")

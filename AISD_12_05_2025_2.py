import re
from collections import defaultdict
import random

slowa = [
    "pies", "kot", "samochod", "rower", "komputer", "telefon", "programowanie", "sztuczna",
    "inteligencja", "szkola", "nauka", "ksiazka", "biurko", "okno", "drzwi", "zegar", "kawa",
    "herbata", "matematyka", "fizyka", "chemia", "historia", "geografia", "muzyka", "sport",
    "pilka", "bieganie", "czytanie", "pisanie", "rysowanie", "malowanie", "gotowanie",
    "jedzenie", "spanie", "podroze", "wakacje", "praca", "dom", "mieszkanie", "rodzina"
]

# Tworzymy losowy tekst z tych slow, majacy 650 slow
tekst = " ".join(random.choices(slowa, k=650))

# Funkcja do zliczania slow zaczynajacych sie na dana litere
def zlicz_pierwsze_litery(tekst: str):
    # Usuwamy interpunkcje i zmieniamy wszystko na male litery
    czysty_tekst = re.sub(r'[^\w\s]', '', tekst).lower()
    slowa_lista = czysty_tekst.split()

    # Mapa haszujaca do zliczania liczby wystapien pierwszych liter slow
    mapa = defaultdict(int)
    for slowo in slowa_lista:
        if slowo:  # ignorujemy puste ciagi
            pierwsza_litera = slowo[0]
            mapa[pierwsza_litera] += 1

    # Sortuje slownik 'mapa' wedlug wartosci (liczby wystapien) w porzadku malejacym
    posortowane = dict(sorted(mapa.items(), key=lambda x: x[1], reverse=True))
    return posortowane

# Uruchamiamy funkcje
rozkład = zlicz_pierwsze_litery(tekst)

# Wypisujemy wynik
print(rozkład)

# python "C:\Users\lechowski_sz\Desktop\AISD_12_05_2025_2.py"
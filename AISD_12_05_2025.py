from collections import Counter

ROZMIAR_TABLICY = 16 #rozmiar tablicy haszujacej


def prosta_funkcja_haszujaca(klucz: str, rozmiar=ROZMIAR_TABLICY) -> int:     #sumuje kody ASCII znakow i zwraca reszte z dzielenia przez rozmiar tablicy
    return sum(ord(znak) for znak in klucz) % rozmiar

def funkcja_hornera(klucz: str, rozmiar=ROZMIAR_TABLICY, podstawa=31) -> int: #traktuje tekst jak liczbe w systemie o ustalonej podstawie by lepiej rozproszyc dane
    wartosc = 0                                                              
    for znak in klucz:
        wartosc = (wartosc * podstawa + ord(znak)) % rozmiar
    return wartosc

def funkcja_djb2(klucz: str, rozmiar=ROZMIAR_TABLICY) -> int: #zaczyna od 5381 i dla kazdego znaku mnozy wynik przez 33, po czym dodaje kod znaku
    wartosc = 5381
    for znak in klucz:
        wartosc = ((wartosc << 5) + wartosc) + ord(znak) # wartosc * 33 + kod znaku
    return wartosc % rozmiar

klucze = [f"klucz{i}" for i in range(1, 31)] #tworzy liste 30 napisow klucz1, klucz2 itd itd


def wypisz_rozklad(funkcja_haszujaca, nazwa): #wypisuje rozklad hashy
    print(f"\nRozklad hashy dla: {nazwa}")
    hashe = [funkcja_haszujaca(klucz) for klucz in klucze] #tworzy liste hashy dla kazdego klucza
    licznik = Counter(hashe) #zlicza ile razy kazdy hash (indeks) wystapil

    print(f"{'Indeks':<8} | {'Liczba kolizji':<15}")
    print("-" * 26)
    for i in range(ROZMIAR_TABLICY):
        print(f"{i:<8} | {licznik.get(i, 0):<15}") #wypisuje liczbe kolizji (czyli ile kluczy trafilo w dany indeks)

# testujemy rozklad dla kazdej z 3 funkcji
wypisz_rozklad(prosta_funkcja_haszujaca, "Prosta funkcja")
wypisz_rozklad(funkcja_hornera, "Funkcja Hornera")
wypisz_rozklad(funkcja_djb2, "Funkcja DJB2")

###########################################

class ProstaMapaHaszujaca: #implementacja mapy haszujacej (HashMap) wykorzystujaca funkcje haszujaca
    def __init__(self, rozmiar=ROZMIAR_TABLICY):
        self.tablica = [[] for _ in range(rozmiar)] #tworzy pusta tablice z listami, obsluga kolizji przez lancuchowanie

    def dodaj(self, klucz, wartosc): #dodaje pare klucz-wartosc do mapy
        indeks = prosta_funkcja_haszujaca(klucz, len(self.tablica)) #wylicza indeks na podstawie klucza
        for i, (k, _) in enumerate(self.tablica[indeks]): #sprawdza czy klucz juz istnieje
            if k == klucz:
                self.tablica[indeks][i] = (klucz, wartosc) #nadpisuje wartosc jesli klucz juz byl
                return
        self.tablica[indeks].append((klucz, wartosc)) #dodaje nowy element

    def pobierz(self, klucz): #zwraca wartosc dla danego klucza
        indeks = prosta_funkcja_haszujaca(klucz, len(self.tablica))
        for k, v in self.tablica[indeks]: #przeszukuje liste w danym indeksie
            if k == klucz:
                return v
        return None #jesli nie znaleziono

# Test dzialania mapy
print("\nTest mapy haszujacej:")
mapa = ProstaMapaHaszujaca()
mapa.dodaj("jablko", 100)
mapa.dodaj("banan", 200)
print("jablko ->", mapa.pobierz("jablko")) #powinno zwrocic 100
print("banan ->", mapa.pobierz("banan"))   #powinno zwrocic 200


# python "C:\Users\lechowski_sz\Desktop\AISD_12_05_2025.py"
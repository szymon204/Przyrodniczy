#ZWRACA WSZYSTKIE PERMUTACJE CIAGU ZNAKOW:
def permutacja(ciag):
    if len(ciag) <= 1:
        return [ciag]
    
    wynik = []
    for i, znak in enumerate(ciag):
        reszta = ciag[:i] + ciag[i+1:]
        for perm in permutacja(reszta):
            wynik.append(znak + perm)
        return wynik
print("Permutacja:")
print(permutacja("abc"))


#PRZYJMUJE LICZBE CALKOWITA N I WYPISUJE JEJ ZAPIS BINARNY:
def wypiszBinarnie(liczba):
    if liczba < 2:
        print(liczba, end="")
    else:
        wypiszBinarnie(liczba // 2)
        print(liczba % 2, end="")

print("Zamiana liczby binarnej (13) daje:")
wypiszBinarnie(13) #test uzycia
print()


#ZNAJDYWANIE SCIEZKI W LABIRYNCIE:
def znajdz_sciezke(labirynt, start, koniec, sciezka=None, odwiedzone=None):
    if sciezka is None:
        sciezka = []
    if odwiedzone is None:
        odwiedzone = set()

    x, y = start
    if start == koniec:
        return sciezka + [koniec]

    if (
        x < 0 or y < 0 or x >= len(labirynt) or y >= len(labirynt[0]) or
        labirynt[x][y] == 1 or (x, y) in odwiedzone
    ):
        return None

    odwiedzone.add((x, y))
    kierunki = [(0,1), (1,0), (0,-1), (-1,0)]  # prawo, dol, lewo, gora

    for dx, dy in kierunki:
        nastepny = (x + dx, y + dy)
        wynik = znajdz_sciezke(labirynt, nastepny, koniec, sciezka + [start], odwiedzone)
        if wynik:
            return wynik

    return None

# Przyklad uzycia:
labirynt = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]
start = (0, 0)
koniec = (3, 3)

sciezka = znajdz_sciezke(labirynt, start, koniec)
print("Sciezka:", sciezka)


# python "C:\Users\lechowski_sz\Desktop\AISD_26_05_2025.py"
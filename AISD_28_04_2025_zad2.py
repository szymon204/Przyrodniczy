class WezelBPlus:
    def __init__(self, czy_lisc=False):
        self.klucze = []        # lista kluczy (wyników punktowych)
        self.wartosci = []      # lista list nicków
        self.dzieci = []        # lista dzieci
        self.czy_lisc = czy_lisc
        self.nastepny = None    # wskaźnik na kolejny liść (lista powiązana)

class BPlusTree:
    def __init__(self, stopien=3):
        self.korzen = WezelBPlus(czy_lisc=True)
        self.stopien = stopien
        self.liczba_porownan = 0

    def znajdz_wezel(self, klucz):
        wezel = self.korzen
        while not wezel.czy_lisc:
            i = 0
            while i < len(wezel.klucze):
                self.liczba_porownan += 1
                if klucz < wezel.klucze[i]:
                    break
                i += 1
            wezel = wezel.dzieci[i]
        return wezel

    def dodaj_gracza(self, nick, wynik):
        wezel = self.znajdz_wezel(wynik)
        i = 0
        while i < len(wezel.klucze):
            self.liczba_porownan += 1
            if wynik == wezel.klucze[i]:
                wezel.wartosci[i].append(nick)
                return
            if wynik < wezel.klucze[i]:
                break
            i += 1
        wezel.klucze.insert(i, wynik)
        wezel.wartosci.insert(i, [nick])
        if len(wezel.klucze) > self.stopien:
            self.podziel_wezel(wezel)

    def podziel_wezel(self, wezel):
        polowa = len(wezel.klucze) // 2
        nowy_wezel = WezelBPlus(czy_lisc=wezel.czy_lisc)
        nowy_wezel.klucze = wezel.klucze[polowa:]
        nowy_wezel.wartosci = wezel.wartosci[polowa:]

        if not wezel.czy_lisc:
            nowy_wezel.dzieci = wezel.dzieci[polowa+1:]
            wezel.dzieci = wezel.dzieci[:polowa+1]

        wezel.klucze = wezel.klucze[:polowa]
        wezel.wartosci = wezel.wartosci[:polowa]

        if wezel.czy_lisc:
            nowy_wezel.nastepny = wezel.nastepny
            wezel.nastepny = nowy_wezel

        if wezel == self.korzen:
            nowy_korzen = WezelBPlus()
            nowy_korzen.klucze = [nowy_wezel.klucze[0]]
            nowy_korzen.dzieci = [wezel, nowy_wezel]
            self.korzen = nowy_korzen
        else:
            rodzic = self.znajdz_rodzica(self.korzen, wezel)
            i = 0
            while i < len(rodzic.klucze):
                self.liczba_porownan += 1
                if nowy_wezel.klucze[0] < rodzic.klucze[i]:
                    break
                i += 1
            rodzic.klucze.insert(i, nowy_wezel.klucze[0])
            rodzic.dzieci.insert(i + 1, nowy_wezel)
            if len(rodzic.klucze) > self.stopien:
                self.podziel_wezel(rodzic)

    def znajdz_rodzica(self, aktualny, dziecko):
        if aktualny.czy_lisc or aktualny.dzieci[0].czy_lisc:
            return None
        for dziecko_wezel in aktualny.dzieci:
            if dziecko_wezel == dziecko:
                return aktualny
            rodzic = self.znajdz_rodzica(dziecko_wezel, dziecko)
            if rodzic:
                return rodzic
        return None

    def aktualizuj_wynik(self, nick, stary_wynik, nowy_wynik):
        self.usun_gracza(nick, stary_wynik)
        self.dodaj_gracza(nick, nowy_wynik)

    def znajdz_graczy_w_przedziale(self, dol, gora):
        wynik = []
        wezel = self.korzen
        while not wezel.czy_lisc:
            wezel = wezel.dzieci[0]

        while wezel:
            for i in range(len(wezel.klucze)):
                self.liczba_porownan += 1
                if dol <= wezel.klucze[i] <= gora:
                    wynik.extend(wezel.wartosci[i])
            wezel = wezel.nastepny
        return wynik

    def najlepszy_gracz(self):
        wezel = self.korzen
        while not wezel.czy_lisc:
            wezel = wezel.dzieci[-1]
        return wezel.wartosci[-1], wezel.klucze[-1]

    def najgorszy_gracz(self):
        wezel = self.korzen
        while not wezel.czy_lisc:
            wezel = wezel.dzieci[0]
        return wezel.wartosci[0], wezel.klucze[0]

    def sprawdz_wynik_gracza(self, nick):
        wezel = self.korzen
        while not wezel.czy_lisc:
            wezel = wezel.dzieci[0]
        while wezel:
            for i in range(len(wezel.klucze)):
                self.liczba_porownan += 1
                if nick in wezel.wartosci[i]:
                    return wezel.klucze[i]
            wezel = wezel.nastepny
        return None

    def usun_gracza(self, nick, wynik):
        wezel = self.znajdz_wezel(wynik)
        for i in range(len(wezel.klucze)):
            self.liczba_porownan += 1
            if wezel.klucze[i] == wynik:
                if nick in wezel.wartosci[i]:
                    wezel.wartosci[i].remove(nick)
                    if len(wezel.wartosci[i]) == 0:
                        wezel.klucze.pop(i)
                        wezel.wartosci.pop(i)
                    return

# ------------------ PRZYKŁAD UŻYCIA ------------------

drzewo = BPlusTree(stopien=3)

# Dodawanie graczy
drzewo.dodaj_gracza("Anna", 1500)
drzewo.dodaj_gracza("Bartek", 1800)
drzewo.dodaj_gracza("Celina", 1700)
drzewo.dodaj_gracza("Daniel", 1500)
drzewo.dodaj_gracza("Ewa", 2000)

# Aktualizacja wyniku
drzewo.aktualizuj_wynik("Anna", 1500, 1900)

# Znajdowanie w przedziale
print("Gracze w przedziale 1600-2000:", drzewo.znajdz_graczy_w_przedziale(1600, 2000))

# Najlepszy i najgorszy gracz
print("Najlepszy gracz:", drzewo.najlepszy_gracz())
print("Najgorszy gracz:", drzewo.najgorszy_gracz())

# Sprawdzanie wyniku konkretnego gracza
print("Wynik gracza Daniel:", drzewo.sprawdz_wynik_gracza("Daniel"))

# Usuwanie gracza
drzewo.usun_gracza("Ewa", 2000)
print("Po usunięciu Ewy:", drzewo.znajdz_graczy_w_przedziale(1400, 2100))

print("Liczba porównań:", drzewo.liczba_porownan)

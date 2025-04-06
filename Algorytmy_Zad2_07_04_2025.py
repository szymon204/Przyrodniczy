listaSlow = [
    "kot", "andrzejko", "komputer", "kwiat", "krzesło", "klucz",
    "kosmos", "karma", "kajak", "kawiarnia", "kabura", "karabin",
    "kolej", "korek", "kowadło", "kawa", "kakao", "kapelusz", "korektor",
    "kalendarz", "kamień", "krawat", "kolor", "kwiat", "koc", "karta",
    "kotek", "klasor", "komoda", "królik", "krzesło", "klimatyzator", "klub",
    "kalosze", "krem", "koza", "kran", "klops", "kapusta", "karmel",
    "kurek", "kowal", "kościół", "królewna", "kwadrat", "kruk", "kapsuła",
    "kaczka", "królik", "kometa", "kocur", "kurczak", "korpus", "kałasznikow",
    "kocyk", "kładka", "kocioł", "krata", "koralik", "kamizelka", "królewicz",
    "kurwa", "kurier", "katar", "kieliszek", "kociak", "komik", "kocur",
    "kanapa", "kancelaria", "koncert", "krowa", "kultura", "klinika",
    "kuchnia", "kamienica", "klucze", "kufel", "kwiaciarnia", "kurtka",
    "kalkulator", "koc", "kajak", "klucznik", "kryształ", "kawiarnia", "kosz",
    "krab", "kaloryfer", "konsola", "kierownica", "kamień", "kajak", "karoseria",
    "kaftan", "kamper", "klapki", "krzesło", "kołdra", "katalog"
]

#Znajdywanie prefixu w liście słow
def znajdzPrefix(slowa, prefix):
    krok = 0
    wynik = []

    for s in slowa:
        krok += 1
        if s.startswith(prefix):
            wynik.append(s)
    return wynik, krok

wynik, krok = znajdzPrefix(listaSlow, "ko")
print("Metoda tablicy:")
print("Znalezione słowa:", wynik)
print("Liczba kroków:", krok)


##ZADANIE DRZEWO:
class WezelDrzewo:
    def __init__(self):
        self.dzieci = {}
        self.koniec_slowa = False

class Drzewo:
    def __init__(self):
        self.korzen = WezelDrzewo() #Korzeń drzewa

    def dodajSlowo(self, slowo):
        wezel = self.korzen
        for s in slowo:
            if s not in wezel.dzieci: #tworzymy nowy węzęł jak litera nie istnieje
                wezel.dzieci[s] = WezelDrzewo()
            wezel = wezel.dzieci[s] #Przechodzimy do kolejnego drzewa
        wezel.koniec_slowa = True

    def wyszukajPrefix(self, prefiks):
        wezel = self.korzen
        wynik = []
        liczba_krokow = 0

        #Przechodzimy przez litery prefiksu
        for s in prefiks:
            liczba_krokow += 1
            if s not in wezel.dzieci:
                return [], liczba_krokow
            wezel = wezel.dzieci[s]

        self.zbierzSlowa(wezel, prefiks, wynik)
        return wynik, liczba_krokow
        
    def zbierzSlowa(self, wezel, aktualne_slowo, wynik):
        if wezel.koniec_slowa:
            wynik.append(aktualne_slowo) #Jeśli to koniec słowa to dodajemy je:

        for litera, nastepnyWezel in wezel.dzieci.items():
            self.zbierzSlowa(nastepnyWezel, aktualne_slowo + litera, wynik)

drzewo = Drzewo()
for s in listaSlow:
    drzewo.dodajSlowo(s)

wynik, krok = drzewo.wyszukajPrefix("ko")
print("Metoda trie:")
print("znalezione slowa:",wynik)
print("liczba krokow: ", krok)
from collections import deque
from datetime import datetime

class Powiadomienie:
    def __init__(self, tresc, typ, priorytet):
        self.tresc = tresc
        self.typ = typ
        self.priorytet = priorytet  # 1 – pilne   0 - standardowe
        self.znacznik_czasu = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Każde powiadomienie jest obiektem który ma 3 części: tresc, typ, priorytet, znacznik czasu
        
    def __str__(self):
        return f"[{self.znacznik_czasu}] ({self.typ}, priorytet: {self.priorytet}) {self.tresc}" #Definiowanie sposobu w jaki powiadomienie jest reprezentowano jako string

class SystemPowiadomien:
    def __init__(self, limit_najnizszych=5):
        self.kolejka = deque() #struktura danych typu FIFO która umożliwia szybsze dodawanie i usuwanie elementów z obu końców
        self.limit_najnizszych = limit_najnizszych #limit liczby powiadomien o najnizszym priorytecie (0), które mogą się znajdować w kolejce. Jeśli liczba przekroczy to najstarsze powiadomienie jest usuwane

    def dodaj_powiadomienie(self, powiadomienie):
        if powiadomienie.priorytet == 1: #Jak powiadomienie ma priorytet 1 to jest dodawane na początek kolejki
            indeks = 0 #szukamy miejsca po ostatnim pilnym powiadomieniu
            for powiad in self.kolejka: 
                if powiad.priorytet == 1: #jak też jest pilne to przesuwamy index dalej
                    indeks += 1
                else:
                    break #jak trafiamy na zwykłe to kończymy
            self.kolejka.insert(indeks, powiadomienie) #wstawiamy pilne powiuadomienie w odpowiednim miejscu
        else: #jeśli powiadomienie nie pilne
            self.kolejka.append(powiadomienie) #dodajemy na koniec kolejki
            self.usun_nadmiar_najnizszych() #sprawdzamy czy nie ma za dużo powiadomień o niskim priorytecie

        print("Dodano powiadomienie:")
        print(powiadomienie) 
        print(f"Liczba oczekujących powiadomień: {self.liczba_oczekujacych()}")

    def usun_nadmiar_najnizszych(self): #usuwa nadmiar zwykłych powiadomień jeśti przekroczono limit
        powiadomienia_niskiego = [p for p in self.kolejka if p.priorytet == 0]
        while len(powiadomienia_niskiego) > self.limit_najnizszych: #dopóki jest ich za dużo
            for p in self.kolejka:
                if p.priorytet == 0: 
                    self.kolejka.remove(p) #usuwamy zwykłe powiadomienie
                    print("Usunięto powiadomienie (limit niskich priorytetów przekroczony):")
                    print(p) #informacja jakie powiadomienie zostało usunięte
                    break
            powiadomienia_niskiego = [p for p in self.kolejka if p.priorytet == 0] #aktuaizacja listy zwykłych

    def pobierz_powiadomienie(self): #pobieranie najstarszego powiadomineia
        if self.kolejka: #jeśli są jakieś powiadomienia
            powiadomienie = self.kolejka.popleft() #pobieramy i usuwamy najstarsze z przodu kolejki
            print("Wyświetlono powiadomienie:")
            print(powiadomienie)
            return powiadomienie #zwracamy powiadomienie
        else:
            print("Brak powiadomień do wyświetlenia.")
            return None

    def liczba_oczekujacych(self): #zwraca liczbe powiadomień w kolejce
        return len(self.kolejka)

#TEST
if __name__ == "__main__":
    system = SystemPowiadomien(limit_najnizszych=3)  # limit powiadomień o priorytecie 0 ustawiony na 3

    # Dodanie kilku powiadomień
    system.dodaj_powiadomienie(Powiadomienie("Masz nowe zadanie!", "info", 0)) #zwykłe
    system.dodaj_powiadomienie(Powiadomienie("Uwaga: Wykryto problem!", "warning", 1)) #pilne
    system.dodaj_powiadomienie(Powiadomienie("Informacja: System zaktualizowany.", "info", 0)) #zwykłe
    system.dodaj_powiadomienie(Powiadomienie("Error: Wystąpił błąd krytyczny.", "error", 1)) #pilne
    system.dodaj_powiadomienie(Powiadomienie("Przypomnienie: Spotkanie o 15:00.", "info", 0)) #zwykłe
    system.dodaj_powiadomienie(Powiadomienie("Notatka: Zakończ projekt.", "info", 0))  #zwykłe, usuwa najstasze zwykłe

    print("\n--- Wyświetlanie powiadomień ---")
    while system.liczba_oczekujacych() > 0: #dopóki jest coś w kolejce pobieramy kolejne powiadomienie i je wyświetlamy
        system.pobierz_powiadomienie()

# python "C:\Users\lechowski_sz\Desktop\AISD_14_04_2025_v2.py"
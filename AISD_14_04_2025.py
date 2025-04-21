class MenedzerHistorii:
    def __init__(self):
        self.stos_wykonanych = [] #stos wykonanych poleceń
        self.stos_cofnietych = [] #stos cofniętych poleceń

    def wykonaj_polecenie(self, polecenie):
        print(f"Wykonuje: {polecenie}")
        self.stos_wykonanych.append(polecenie) #Dodanie nowego polecenia do stos_wykonanych
        self.stos_cofnietych.clear() #Wyczyszczenie stosu cofniętych, ponieważ po tym działaniu nie można już ponowić poprzednio cofniętego

    def cofnij(self):
        if not self.stos_wykonanych:
            print("Brak poleceń do ponowienia") #Sprawdza czy są jakiekolwiek wykonane poelecenia, jeśli nie - nie da się cofnąć
            return
        polecenie = self.stos_wykonanych.pop() #pop zabiera ostatnie polecenie ze stos_wykonanych i zwraca je (czyli to co właśnie cofamy)
        print(f"Cofam: {polecenie}")
        self.stos_cofnietych.append(polecenie) #Wyświetla cofnięcie i dodaje cofnięte polecenie do stos_cofnietych, aby można było je ponowić.

    def usun(self):
        if not self.stos_wykonanych:
            print("Brak poleceń do usunięcia")
            return
        polecenie = self.stos_wykonanych.pop() #zdejmuje ostatnie polecenie ze stosu wykonanych i nie przenosi go nigdzie, nie można go ani cofnąć ani ponowić
        print(f"Usuwam polecenie: {polecenie}")

    def wypisz_historie(self):
        print("Historia wykonanych poleceń:")
        for numer, polecenie in enumerate(self.stos_wykonanych, start = 1): #enumerate tworzy pary (numer, poelcenie) - nr. porządkowy i tekst polecenia, numeracja ustawiona od 1
            print(f"{numer}, {polecenie}") 

    def ponow(self):
        if not self.stos_cofnietych:
            print("Brak poleceń do ponowienia")
            return
        polecenie = self.stos_cofnietych.pop()  #Zdejmowanie ostatniego cofniętego polecenia ze stosu stos_cofnietych, zeby je ponowic
        print(f"Ponawiam: {polecenie}")
        self.stos_wykonanych.append(polecenie)

#TEST:
if __name__ == "__main__":
    historia = MenedzerHistorii()

    while True:
        print("\nWybierz operację:")
        print("1. Wykonaj polecenie")
        print("2. Cofnij ostatnie polecenie (UNDO)")
        print("3. Ponów ostatnie cofnięte polecenie (REDO)")
        print("4. Usuń ostatnie polecenie (DELETE)")
        print("5. Wyświetl historię")
        print("6. Zakończ")

        wybor = input("Podaj numer operacji: ")

        if wybor == "1":
            polecenie = input("Podaj treść polecenia: ")
            historia.wykonaj_polecenie(polecenie)
        elif wybor == "2":
            historia.cofnij()
        elif wybor == "3":
            historia.ponow()
        elif wybor == "4":
            historia.usun()
        elif wybor == "5":
            historia.wypisz_historie()
        elif wybor == "6":
            print("Koniec programu.")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

# python "C:\Users\lechowski_sz\Desktop\AISD_14_04_2025.py"
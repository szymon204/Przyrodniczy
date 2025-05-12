import datetime
import random

# Uzytkownik wybiera date prezentacji
data_prezentacji = input("Podaj date prezentacji (YYYY-MM-DD): ")

try:
    bazowa_data = datetime.datetime.strptime(data_prezentacji, "%Y-%m-%d")
except ValueError:
    print("Niepoprawny format daty! Uzyj YYYY-MM-DD.")
    exit()

# Tworzymy slownik (hashmape) przechowujacy odwiedziny uzytkownika
odwiedziny = {}

def zapisz_odwiedziny(odwiedziny, wspolrzedne, czas=None):
    """Zapisuje czas odwiedzin dla danej lokalizacji"""
    if czas is None:
        czas = datetime.datetime.now()  # Jesli brak czasu, ustawiamy teraz
    
    odwiedziny[wspolrzedne] = czas  # Przypisujemy czas do lokalizacji

# Lista przykladowych wspolrzednych lokalizacji
lista_lokalizacji = [
    (52.23, 21.01), (50.06, 19.94), (51.11, 17.03), (53.13, 23.16),
    (54.35, 18.64), (50.26, 19.02), (51.76, 19.45), (49.79, 19.05),
    (53.01, 18.60), (52.40, 16.92)
]

# Dodajemy odwiedziny dla losowych lokalizacji, zmieniajac czas co kilka iteracji
for _ in range(30):
    wspolrzedne = random.choice(lista_lokalizacji)
    
    # Dodajemy wpisy dla roznych dni wokol wybranej daty
    przesuniecie_dni = random.choice([-2, -1, 0, 1, 2])  # Losowe przesuniecie daty
    przesuniecie_godzin = random.choice([0, 4, 8, 12])  # Rozne godziny w ciagu dnia
    czas_odwiedzin = bazowa_data + datetime.timedelta(days=przesuniecie_dni, hours=przesuniecie_godzin)
    
    zapisz_odwiedziny(odwiedziny, wspolrzedne, czas_odwiedzin)

# Wyszukiwanie lokalizacji odwiedzonych w danym dniu
def wyszukaj_lokalizacje_dnia(odwiedziny, data):
    """Zwraca liste lokalizacji odwiedzonych danego dnia"""
    return [lok for lok, czas in odwiedziny.items() if czas.date() == data]

# Debugowanie wyswietlenie wszystkich zapisanych lokalizacji i dat:
print("\nWszystkie zapisane lokalizacje:")
for lok, czas in odwiedziny.items():
    print(f"Lokalizacja: {lok}, Data: {czas.date()}")

# Sprawdzamy lokalizacje odwiedzone dokladnie w wybranym dniu prezentacji
lokalizacje_dnia = wyszukaj_lokalizacje_dnia(odwiedziny, bazowa_data.date())

print(f"\nLokalizacje odwiedzone {bazowa_data.date()}: {lokalizacje_dnia}")

# python "C:\Users\lechowski_sz\Desktop\AISD_12_05_2025_3.py"
import random

def insertion_sort(tablica, lewy, prawy, liczba_porownan):
    for i in range(lewy + 1, prawy + 1): 
        klucz = tablica[i] 
        j = i - 1 
        while j >= lewy:
            liczba_porownan[0] += 1
            if tablica[j] > klucz:
                tablica[j + 1] = tablica[j]
                j -= 1
            else:
                break
        tablica[j + 1] = klucz

def scalanie(tablica, lewy, srodek, prawy, liczba_porownan):
    lewa_czesc = tablica[lewy:srodek+1]
    prawa_czesc = tablica[srodek+1:prawy+1]
    i = j = 0
    k = lewy

    while i < len(lewa_czesc) and j < len(prawa_czesc):
        liczba_porownan[0] += 1
        if lewa_czesc[i] <= prawa_czesc[j]:
            tablica[k] = lewa_czesc[i]
            i += 1
        else:
            tablica[k] = prawa_czesc[j]
            j += 1
        k += 1

    while i < len(lewa_czesc):
        tablica[k] = lewa_czesc[i]
        i += 1
        k += 1

    while j < len(prawa_czesc):
        tablica[k] = prawa_czesc[j]
        j += 1
        k += 1

def uproszczony_tim_sort(tablica, wielkosc_runa):
    n = len(tablica)
    liczba_porownan = [0]

    # Sortowanie małych bloków
    for poczatek in range(0, n, wielkosc_runa):
        koniec = min(poczatek + wielkosc_runa - 1, n - 1)
        insertion_sort(tablica, poczatek, koniec, liczba_porownan)

    # Łączenie posortowanych bloków
    rozmiar = wielkosc_runa
    while rozmiar < n:
        for lewy in range(0, n, 2 * rozmiar):
            srodek = min(lewy + rozmiar - 1, n - 1)
            prawy = min(lewy + 2 * rozmiar - 1, n - 1)
            if srodek < prawy:
                scalanie(tablica, lewy, srodek, prawy, liczba_porownan)
        rozmiar *= 2

    return liczba_porownan[0]

def wykonaj_test(tablica, wielkosc_runa, opis):
    tablica_kopia = tablica.copy()
    liczba_porownan = uproszczony_tim_sort(tablica_kopia, wielkosc_runa)
    print(f"{opis}")
    print(f"Tablica po sortowaniu: {tablica_kopia}")
    print(f"Liczba porównań: {liczba_porownan}\n")

# Testy
tablica_posortowana = [1, 2, 3, 4, 5]
wykonaj_test(tablica_posortowana, 2, "Test 1: Tablica już posortowana")

tablica_odwrotna = [5, 4, 3, 2, 1]
wykonaj_test(tablica_odwrotna, 2, "Test 2: Tablica odwrotnie posortowana")

tablica_losowa = [3, 1, 4, 5, 2]
wykonaj_test(tablica_losowa, 2, "Test 3: Tablica losowa")

tablica_czesciowo = [1, 2, 6, 5, 4]
wykonaj_test(tablica_czesciowo, 2, "Test 4: Tablica częściowo posortowana")

tablica_wieksza = random.sample(range(1, 21), 20)
wykonaj_test(tablica_wieksza, 4, "Test 5: Większa tablica losowa")

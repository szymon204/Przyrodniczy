import copy

# 1. ZWYKLY BLUR – srednia otoczenia (3x3)
def blur_zwykly(obraz):
    wysokosc = len(obraz)
    szerokosc = len(obraz[0])
    nowy_obraz = copy.deepcopy(obraz)

    for y in range(1, wysokosc - 1):
        for x in range(1, szerokosc - 1):
            suma = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    suma += obraz[y + dy][x + dx]
            nowy_obraz[y][x] = suma // 9  # srednia arytmetyczna

    return nowy_obraz

# 2. BLUR GAUSSA – wagi z macierzy Gaussa
def blur_gaussa(obraz):
    wysokosc = len(obraz)
    szerokosc = len(obraz[0])
    nowy_obraz = copy.deepcopy(obraz)

    wagi = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]
    suma_wag = 16

    for y in range(1, wysokosc - 1):
        for x in range(1, szerokosc - 1):
            suma = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    waga = wagi[dy + 1][dx + 1]
                    suma += obraz[y + dy][x + dx] * waga
            nowy_obraz[y][x] = suma // suma_wag

    return nowy_obraz

# 3. PRZEKSZTALCENIE DO CZARNO-BIALEGO (binary thresholding)
def binaryzacja(obraz, prog):
    wysokosc = len(obraz)
    szerokosc = len(obraz[0])
    nowy_obraz = []

    for y in range(wysokosc):
        wiersz = []
        for x in range(szerokosc):
            if obraz[y][x] >= prog:
                wiersz.append(1)  # czarny
            else:
                wiersz.append(0)  # bialy
        nowy_obraz.append(wiersz)

    return nowy_obraz


# Przykladowy obraz 5x5 w skali szarosci
obraz = [
    [10, 20, 30, 40, 50],
    [20, 30, 40, 50, 60],
    [30, 40, 50, 60, 70],
    [40, 50, 60, 70, 80],
    [50, 60, 70, 80, 90]
]

print("Zwykly blur:")
for w in blur_zwykly(obraz):
    print(w)

print("\nBlur Gaussa:")
for w in blur_gaussa(obraz):
    print(w)

print("\nBinaryzacja (prog 45):")
for w in binaryzacja(obraz, 45):
    print(w)


# python "C:\Users\lechowski_sz\Desktop\AISD_26_05_2025_3.py"
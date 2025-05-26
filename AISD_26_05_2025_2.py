from collections import deque

# 1. Flood Fill – rekurencyjne przeszukiwanie w glab (DFS)
def flood_fill_dfs(obraz, x, y, nowy_kolor):
    wysokosc = len(obraz)
    szerokosc = len(obraz[0])
    kolor_startowy = obraz[x][y]

    if kolor_startowy == nowy_kolor:
        return

    def dfs(i, j):
        # Sprawdz granice obrazu
        if i < 0 or j < 0 or i >= wysokosc or j >= szerokosc:
            return
        if obraz[i][j] != kolor_startowy:
            return

        obraz[i][j] = nowy_kolor

        # 4 kierunki: dol, gora, prawo, lewo
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    dfs(x, y)

# 2. Flood Fill – iteracyjne przeszukiwanie wszerz (BFS)
def flood_fill_bfs(obraz, x, y, nowy_kolor):
    wysokosc = len(obraz)
    szerokosc = len(obraz[0])
    kolor_startowy = obraz[x][y]

    if kolor_startowy == nowy_kolor:
        return

    kolejka = deque()
    kolejka.append((x, y))

    while kolejka:
        i, j = kolejka.popleft()

        if i < 0 or j < 0 or i >= wysokosc or j >= szerokosc:
            continue
        if obraz[i][j] != kolor_startowy:
            continue

        obraz[i][j] = nowy_kolor

        # 4 kierunki: dol, gora, prawo, lewo
        kolejka.append((i + 1, j))
        kolejka.append((i - 1, j))
        kolejka.append((i, j + 1))
        kolejka.append((i, j - 1))

# Przykładowy obraz (2D tablica kolorow)
obraz = [
    [1, 1, 1, 2],
    [1, 1, 0, 2],
    [1, 0, 0, 2],
    [3, 3, 2, 2]
]

# Parametry: punkt startowy (1, 1), nowy kolor = 9
print("Oryginalny obraz:")
for wiersz in obraz:
    print(wiersz)

flood_fill_dfs(obraz, 1, 1, 9)  # <- DFS (rekurencyjny)
flood_fill_bfs(obraz, 1, 1, 9)    # <- BFS (iteracyjny)

print("\nPo zastosowaniu Flood Fill:")
for wiersz in obraz:
    print(wiersz)


# python "C:\Users\lechowski_sz\Desktop\AISD_26_05_2025_2.py"
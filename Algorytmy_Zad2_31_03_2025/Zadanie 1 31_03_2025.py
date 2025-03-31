#Algorytm z jedna operacja:
def O1(n):
    krok = 0
    krok += 1
    return krok
    
# Testowanie
n_values = [100,1000,100000]
for n in n_values:
    print(f"O(1) dla n={n}: {O1(n)} krokow")

#PRZYKLAD DRUGI
#Ten kod zlicza i wypisuje liczbe krokow (iteracji) wykonanych w petli dla roznych wartosci n, co odpowiada zlozonosci czasowej O(n).
def On(n):
    krok = 0
    for x in range(n):
        krok += 1 
    return krok

n_values = [100, 1000, 100000]
# Testowanie
for x in n_values:
    print(f"O(n) dla n={x}: {On(x)} krokow")

#PRZYKLAD TRZECI
#Ten kod zlicza i wypisuje liczbe krokow (iteracji) wykonanych w dwoch zagniezdzonych petlach, co odpowiada zlozonosci czasowej O(n2).
def On2(n):
    krok = 0
    for i in range(n):
        for j in range(n):
            krok += 1
    return krok

n_values = [100, 1000, 10000]
# Testowanie
for x in n_values:
    print(f"O(n^2) dla n={x}: {On2(x)} krokow")

#PRZYKLAD CZWARTY
def Oan(n):
    krok = 0
    for i in range(2**n):  # Petla wykona sie 2^n razy
        krok += 1
    return krok

# Testowanie
n_values = [5, 6, 7]
for x in n_values:
    print(f"O(2^n) dla n={x}: {Oan(x)} krokow")
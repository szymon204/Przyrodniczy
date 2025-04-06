#1.1 Tablica posortowana:
def min_max_sort(arr):
    steps = 0
    min_value = arr[0] #Dostęp do pierwszego elementu
    steps += 1
    max_value = arr[-1] #Dostęp do ostatniego elementu
    steps +=1

    return min_value, max_value, steps
#Przykład użycia:
sorted_table = [1,3,5,7,9]
min_value, max_value, steps = min_max_sort(sorted_table)
print("Tablica posortowana:")
print("Największy element =", max_value)
print("Najmniejszy element =", min_value)
print("Liczba kroków =", steps)


#1.2 Tablica nieposortowana:
def min_max_unsorted(arr):
    steps = 0
    min_value = arr[0]
    max_value = arr[0] #Uznajemy pierwszy element za najmniejszy i największy
    steps += 2 #Inicjalizacja min i max value

    #Przechodzimy przez elementy tablicy:
    for x in range(1, len(arr)):
        steps += 1
        if arr[x] < min_value:
            min_value = arr[x]
            steps += 1
        if arr[x] > max_value:
            max_value = arr[x]
            steps += 1
    return min_value, max_value, steps
#Przykład użycia:
unosrted_table = [7,1,9,3,5]
min_value, max_value, steps = min_max_unsorted(unosrted_table)
print("Tablica nieposortowana:")
print("Największy element to:", max_value)
print("Najmniejszy element to:", min_value)
print("Liczba kroków to:", steps)


#1.3 Drzewo BST:
class Node: #Klasa prezentująca węzęł drzewa BST. Każdy węzeł posiada wartość oraz wskaźniki na lewego i prawego syna.

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value): #Funckja wstawia wartośc do drzewa BST
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def min_bst(root): #Funkcja znajduje najmniejszy element w BST:
    steps = 0
    current = root
    #Przechodzimy do najbardziej lewego węzła
    while current.left is not None:
        current = current.left
        steps += 1
    steps += 1 #Liczymy ostatni krok gdy już nie ma lewego dziecka
    return current.value, steps

def max_bst(root): #Funkcja znajduje największy element w BST:
    steps = 0
    current = root
    #Przechodzimy do najbardziej prawego węzła:
    while current.right is not None:
        current = current.right
        steps += 1
    steps += 1 #Liczymy ostatni krok
    return current.value, steps

#Przykładowe użycie funkcji:
values = [7,1,9,3,5]
bst_root = None
for val in values:
    bst_root = insert(bst_root, val)
min_bst_val, steps_bst_min = min_bst(bst_root)
max_bst_val, steps_bst_max = max_bst(bst_root)
print("BST:")
print("Najmniejszy element =",min_bst_val, ", Liczba kroków przy szukaniu:", steps_bst_min)
print("Największy element =", max_bst_val, ", Liczba kroków przy szukaniu max =", steps_bst_max)
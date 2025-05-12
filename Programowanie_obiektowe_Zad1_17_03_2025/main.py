import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap, QFont
import webbrowser

def on_label_click():
    label.setText("Zostałeś przeniesiony na Google")  # Przenoszenie na Google
    webbrowser.open("https://www.google.com")

@Slot()
def say_hello():
    print("Przycisk Kliknięty, cześć") # Powiadomienie w konsoli

@Slot()
def clear_input():
    input1.clear()  # Czyści tekst w polu input1
    input2.clear()  # Czyści tekst w polu input2

def add_numbers():
    try:
        num1 = float(input1.text())
        num2 = float(input2.text())
        result_label.setText(f"Wynik: {num1 + num2}")
    except ValueError:
        result_label.setText("Błąd: Proszę wprowadzić liczby")

def subtract_numbers():
    try:
        num1 = float(input1.text())
        num2 = float(input2.text())
        result_label.setText(f"Wynik: {num1 - num2}")
    except ValueError:
        result_label.setText("Błąd: Proszę wprowadzić liczby")

def multiply_numbers():
    try:
        num1 = float(input1.text())
        num2 = float(input2.text())
        result_label.setText(f"Wynik: {num1 * num2}")
    except ValueError:
        result_label.setText("Błąd: Proszę wprowadzić liczby")

def divide_numbers():
    try:
        num1 = float(input1.text())
        num2 = float(input2.text())
        if num2 == 0:
            result_label.setText("Błąd: Nie można dzielić przez zero")
        else:
            result_label.setText(f"Wynik: {num1 / num2}")
    except ValueError:
        result_label.setText("Błąd: Proszę wprowadzić liczby")

app = QApplication(sys.argv)

# Tworzenie głównego okna
window = QWidget()

# Tworzenie etykiety:
label = QLabel()
label.setAlignment(Qt.AlignCenter)

# Ustawienie obrazu:
pixmap = QPixmap(r"C:\temp\SAMOLOT.jpg")  # Wczytaj obrazek:


# Ustawienie czcionki
font = QFont("Arial", 20)
label.setFont(font)

# Ustawienie koloru tła
window.setStyleSheet("background-color: orange;")  # Kolor tła okna na pomarańczowy s

# Dodanie linku do etykiety
label.setText('<a href="https://www.google.com" style="color: blue;">Kliknij aby otworzyć Google</a>')
label.linkActivated.connect(on_label_click)

# Tworzenie pola input
input1 = QLineEdit()
input1.setPlaceholderText("Wprowadź pierwszą liczbę...")

input2 = QLineEdit()
input2.setPlaceholderText("Wprowadź drugą liczbę...")

# Tworzenie etykiety do wyświetlania wyniku
result_label = QLabel("Wynik: 0")
result_label.setAlignment(Qt.AlignCenter)
result_label.setFont(QFont("Arial", 16))

# Tworzenie przycisków dla działań matematycznych
add_button = QPushButton("+")
subtract_button = QPushButton("-")
multiply_button = QPushButton("*")
divide_button = QPushButton("/")

# Przypisanie funkcji do przycisków
add_button.clicked.connect(add_numbers)
subtract_button.clicked.connect(subtract_numbers)
multiply_button.clicked.connect(multiply_numbers)
divide_button.clicked.connect(divide_numbers)

# Tworzenie przycisku, który czyści pole input
clear_button = QPushButton("Wyczyść pola input")
clear_button.clicked.connect(clear_input)

#Przycisk Hello konsola
hello_button = QPushButton("Kliknij aby zobaczyć w konsoli tekst")
hello_button.clicked.connect(say_hello)

# Układ pionowy
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(input1)
layout.addWidget(input2)
layout.addWidget(add_button)
layout.addWidget(subtract_button)
layout.addWidget(multiply_button)
layout.addWidget(divide_button)
layout.addWidget(result_label)
layout.addWidget(clear_button)
layout.addWidget(hello_button)

window.setLayout(layout)
window.show()

app.exec()

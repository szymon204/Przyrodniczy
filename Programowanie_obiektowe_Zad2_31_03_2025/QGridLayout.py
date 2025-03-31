from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QLineEdit, QCheckBox, QRadioButton, QButtonGroup, QPushButton, QMessageBox, QScrollArea
from PySide6.QtCore import Qt

class QuizGrid(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marvel Quiz - QGridLayout")

        scroll_area = QScrollArea()
        centralny_widget = QWidget()
        scroll_area.setWidget(centralny_widget)
        scroll_area.setWidgetResizable(True)
        self.setCentralWidget(scroll_area)
        self.resize(400, 300)

        # Tworzymy layout
        layout = QGridLayout()

        # Dodanie tytułu quizu (tytuł rozciąga się na 3 kolumny)
        self.tytul = QLabel("MARVEL QUIZ - PYTANIA Z MCU")
        self.tytul.setAlignment(Qt.AlignCenter)
        self.tytul.setStyleSheet("font-weight: bold")
        layout.addWidget(self.tytul, 0, 0, 1, 3)  # Umieszczamy tytuł w wierszu 0, rozciągamy na 3 kolumny

        # Pytanie nr 1:
        self.pytanie1 = QLabel("1. Kto jest Iron Manem:")
        self.input1 = QLineEdit(self)
        layout.addWidget(self.pytanie1, 1, 0)  # Pytanie 1 w wierszu 1, kolumna 0
        layout.addWidget(self.input1, 1, 1, 1, 2)  # Pole tekstowe w wierszu 1, kolumna 1-2 (rozciąga się na 2 kolumny)

        # Pytanie nr 2:
        self.pytanie2 = QLabel("2. Kto z poniższych jest członkiem Avengers:")
        self.checkbox2_1 = QCheckBox("Thor")
        self.checkbox2_2 = QCheckBox("Loki")
        self.checkbox2_3 = QCheckBox("Hawkeye")

        # Pytanie 2 i checkboxy w wierszu 2
        layout.addWidget(self.pytanie2, 2, 0, 1, 3)  # Pytanie 2 w wierszu 2, rozciągamy na 3 kolumny
        layout.addWidget(self.checkbox2_1, 3, 0)  # Checkbox Thor w wierszu 3, kolumna 0
        layout.addWidget(self.checkbox2_2, 3, 1)  # Checkbox Loki w wierszu 3, kolumna 1
        layout.addWidget(self.checkbox2_3, 3, 2)  # Checkbox Hawkeye w wierszu 3, kolumna 2

        # Pytanie nr 3:
        self.pytanie3 = QLabel("3. Kto gra rolę Thora w filmach Marvela?")
        self.radio_group3 = QButtonGroup(self)
        self.radio_button3_1 = QRadioButton("Chris Hemsworth")
        self.radio_button3_2 = QRadioButton("Chris Evans")
        self.radio_button3_3 = QRadioButton("Chris Pratt")

        # Pytanie 3 i radio buttons w wierszu 4
        layout.addWidget(self.pytanie3, 4, 0, 1, 3)  # Pytanie 3 w wierszu 4, rozciągamy na 3 kolumny
        layout.addWidget(self.radio_button3_1, 5, 0)  # Chris Hemsworth w wierszu 5, kolumna 0
        layout.addWidget(self.radio_button3_2, 5, 1)  # Chris Evans w wierszu 5, kolumna 1
        layout.addWidget(self.radio_button3_3, 5, 2)  # Chris Pratt w wierszu 5, kolumna 2

        # Pytanie nr 4:
        self.pytanie4 = QLabel("4. Kto jest siostrą Gamory:")
        self.radio_group4 = QButtonGroup(self)
        self.radio_button4_1 = QRadioButton("Nebula")
        self.radio_button4_2 = QRadioButton("Valkyrie")
        self.radio_button4_3 = QRadioButton("Shuri")

        # Pytanie 4 i radio buttons w wierszu 6
        layout.addWidget(self.pytanie4, 6, 0, 1, 3)  # Pytanie 4 w wierszu 6, rozciągamy na 3 kolumny
        layout.addWidget(self.radio_button4_1, 7, 0)  # Nebula w wierszu 7, kolumna 0
        layout.addWidget(self.radio_button4_2, 7, 1)  # Valkyrie w wierszu 7, kolumna 1
        layout.addWidget(self.radio_button4_3, 7, 2)  # Shuri w wierszu 7, kolumna 2

        # Pytanie nr 5:
        self.pytanie5 = QLabel("Które z poniższych postaci występuje w filmie 'Guardians of the Galaxy':")
        self.checkbox5_1 = QCheckBox("Rocket Racoon")
        self.checkbox5_2 = QCheckBox("Black Widow")
        self.checkbox5_3 = QCheckBox("Drax the Destroyer")

        # Pytanie 5 i checkboxy w wierszu 8
        layout.addWidget(self.pytanie5, 8, 0, 1, 3)  # Pytanie 5 w wierszu 8, rozciągamy na 3 kolumny
        layout.addWidget(self.checkbox5_1, 9, 0)  # Checkbox Rocket w wierszu 9, kolumna 0
        layout.addWidget(self.checkbox5_2, 9, 1)  # Checkbox Black Widow w wierszu 9, kolumna 1
        layout.addWidget(self.checkbox5_3, 9, 2)  # Checkbox Drax w wierszu 9, kolumna 2

        # Przycisk sprawdzający:
        self.check_button = QPushButton("Sprawdź")
        self.check_button.clicked.connect(self.sprawdzenie_odp)
        layout.addWidget(self.check_button, 10, 0, 1, 3)  # Przycisk w wierszu 10, rozciągamy na 3 kolumny

        # Ustawiamy layout
        centralny_widget.setLayout(layout)

    def sprawdzenie_odp(self):
        punkty = 0

        # Funkcja sprawdzająca odpowiedzi:
        def sprawdz_poprawnosc_odpowiedzi(odpowiedz_uzytkownika, poprawna_odpowiedz):
            return odpowiedz_uzytkownika.strip().lower() == poprawna_odpowiedz.lower()

        # Sprawdzanie odpowiedzi i ustawienie tła na zielono lub czerwono
        if sprawdz_poprawnosc_odpowiedzi(self.input1.text(), "Tony Stark"):
            punkty += 1
        self.input1.setStyleSheet("background-color: green;" if sprawdz_poprawnosc_odpowiedzi(self.input1.text(), "Tony Stark") else "background-color: red;")

        if self.checkbox2_1.isChecked() and not self.checkbox2_2.isChecked() and self.checkbox2_3.isChecked():
            punkty += 1
        self.checkbox2_1.setStyleSheet("background-color: green;")
        self.checkbox2_2.setStyleSheet("background-color: red;")
        self.checkbox2_3.setStyleSheet("background-color: green;")

        if self.radio_button3_1.isChecked():
            punkty += 1
        self.radio_button3_1.setStyleSheet("background-color: green;")
        self.radio_button3_2.setStyleSheet("background-color: red;")
        self.radio_button3_3.setStyleSheet("background-color: red;")

        if self.radio_button4_1.isChecked():
            punkty += 1
        self.radio_button4_1.setStyleSheet("background-color: green;")
        self.radio_button4_2.setStyleSheet("background-color: red;")
        self.radio_button4_3.setStyleSheet("background-color: red;")

        if self.checkbox5_1.isChecked() and not self.checkbox5_2.isChecked() and self.checkbox5_3.isChecked():
            punkty += 1
        self.checkbox5_1.setStyleSheet("background-color: green;")
        self.checkbox5_2.setStyleSheet("background-color: red;")
        self.checkbox5_3.setStyleSheet("background-color: green;")

        # Wyświetlanie wyniku:
        QMessageBox.information(self, "Wynik", f"Zdobyłeś {punkty} na 5 punktów!")

# Uruchomienie aplikacji
app = QApplication([])
quiz_grid = QuizGrid()
quiz_grid.show()
app.exec()
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QFormLayout, QLineEdit, QCheckBox, QRadioButton, QButtonGroup, QPushButton, QMessageBox, QScrollArea
from PySide6.QtCore import Qt

class QuizForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marvel Quiz - QFormLayout")

        scroll_area = QScrollArea()
        centralny_widget = QWidget()
        scroll_area.setWidget(centralny_widget)
        scroll_area.setWidgetResizable(True)
        self.setCentralWidget(scroll_area)
        self.resize(400, 300)

        layout = QFormLayout() #ZMIANA LAYOUTU

        # Dodanie tytułu quizu
        self.tytul = QLabel("MARVEL QUIZ - PYTANIA Z MCU")
        self.tytul.setAlignment(Qt.AlignCenter)
        self.tytul.setStyleSheet("font-weight: bold")
        layout.addRow(self.tytul)  #Tytul do formularza

        # Pytanie nr 1:
        self.pytanie1 = QLabel("1. Kto jest Iron Manem:")
        self.input1 = QLineEdit(self)
        layout.addRow(self.pytanie1, self.input1)

        # Pytanie nr 2:
        self.pytanie2 = QLabel("2. Kto z poniższych jest członkiem Avengers:")
        self.checkbox2_1 = QCheckBox("Thor")
        self.checkbox2_2 = QCheckBox("Loki")
        self.checkbox2_3 = QCheckBox("Hawkeye")
        layout.addRow(self.pytanie2)  # Dodanie pytania
        layout.addRow(self.checkbox2_1, self.checkbox2_2)  # Pierwsza linia z checkboxami
        layout.addRow(self.checkbox2_3)  # Druga linia z jednym checkboxem

        # Pytanie nr 3:
        self.pytanie3 = QLabel("3. Kto gra rolę Thora w filmach Marvela?")
        self.radio_group3 = QButtonGroup(self)
        self.radio_button3_1 = QRadioButton("Chris Hemsworth")
        self.radio_button3_2 = QRadioButton("Chris Evans")
        self.radio_button3_3 = QRadioButton("Chris Pratt")

        layout.addRow(self.pytanie3)  # Dodanie pytania
        layout.addRow(self.radio_button3_1, self.radio_button3_2)  # Pierwsza linia z radio buttons
        layout.addRow(self.radio_button3_3)  # Druga linia z jednym radio buttonem

        # Pytanie nr 4:
        self.pytanie4 = QLabel("4. Kto jest siostrą Gamory:")
        self.radio_group4 = QButtonGroup(self)
        self.radio_button4_1 = QRadioButton("Nebula")
        self.radio_button4_2 = QRadioButton("Valkyrie")
        self.radio_button4_3 = QRadioButton("Shuri")

        layout.addRow(self.pytanie4)  # Dodanie pytania
        layout.addRow(self.radio_button4_1, self.radio_button4_2)  # Pierwsza linia z radio buttons
        layout.addRow(self.radio_button4_3)  # Druga linia z jednym radio buttonem

        # Pytanie nr 5:
        self.pytanie5 = QLabel("Które z poniższych postaci występuje w filmie 'Guardians of the Galaxy':")
        self.checkbox5_1 = QCheckBox("Rocket Racoon")
        self.checkbox5_2 = QCheckBox("Black Widow")
        self.checkbox5_3 = QCheckBox("Drax the Destroyer")

        layout.addRow(self.pytanie5)  # Dodanie pytania
        layout.addRow(self.checkbox5_1, self.checkbox5_2)  # Pierwsza linia z checkboxami
        layout.addRow(self.checkbox5_3)  # Druga linia z jednym checkboxem

        # Przycisk sprawdzający:
        self.check_button = QPushButton("Sprawdź")
        self.check_button.clicked.connect(self.sprawdzenie_odp)
        layout.addRow(self.check_button)  # Dodajemy przycisk na końcu formularza

        # Ustawiamy layout
        centralny_widget.setLayout(layout)

    def sprawdzenie_odp(self):
        punkty = 0

        def sprawdz_poprawnosc_odpowiedzi(odpowiedz_uzytkownika, poprawna_odpowiedz):
            return odpowiedz_uzytkownika.strip().lower() == poprawna_odpowiedz.lower()

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
quiz_form = QuizForm()
quiz_form.show()
app.exec()
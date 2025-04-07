import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QMenu, QToolBar, QDialog, QVBoxLayout, QPushButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #wywołanie konstruktora

        self.setWindowTitle("07_04_2025")
        self.setGeometry(100,100,400,200)

        self.statusBar() #Włącza pasek statusu na dole
        self.create_menu() #tworzenie menu aplikacji
        self.create_toolbar() #Tworzenie toolbaru ZADANIE 2

    def create_menu(self):
        menu_bar = self.menuBar() #tworzenie paska menu

        file_menu = menu_bar.addMenu("Plik") #dodanie kategorii PLIK

        #Akcja otwórz:
        open_action = QAction(QIcon("C:/Users/lechowski_sz/Desktop/STUDIA UP/SEMESTR 4/PROGRAMOWANIE OBIEKTOWE II/otworz.png"), "Otwórz", self) #dodanie akcji otwórz
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Otwórz plik")  #podpowiedz w pasku statusu
        open_action.triggered.connect(lambda: self.statusBar().showMessage("Kliknięto: Otwórz")) #Pokazanie komunikatu w pasku statusu, LAMBDA - SKRÓCONA WERSJA, ZAMIAST FUNKCJI.
        file_menu.addAction(open_action) #dodanie akcji Otworz do penu Plik

        file_menu.addSeparator() #Separator pomiedzy akcjami

        #Akcja zamknij:
        exit_action = QAction(QIcon("C:/Users/lechowski_sz/Desktop/STUDIA UP/SEMESTR 4/PROGRAMOWANIE OBIEKTOWE II/Zamknij.png"), "Zamknij", self) #Dodanie akcji zamknij
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Zamknij aplikację") #podpowiedz w pasku statusu
        exit_action.triggered.connect(self.close) #po kliknieciu aplikacja zostanie zamknieta
        file_menu.addAction(exit_action) #Dodanie akcji do menu plik

        #Menu Pomoc
        help_menu = menu_bar.addMenu("Pomoc")

        # Akcja "O aplikacji"
        about_action = QAction("O aplikacji", self)
        about_action.setShortcut("Ctrl+I")
        about_action.setStatusTip("Informacje o aplikacji")
        about_action.triggered.connect(lambda: self.statusBar().showMessage("To jest wersja demo")) #LAMBDA - SKRÓCONA WERSJA ZAMIAST FUNKCJI
        help_menu.addAction(about_action)

        # Podmenu "Więcej"
        more_menu = QMenu("Więcej", self)
        info_action = QAction("Dodatkowe info", self)
        info_action.setStatusTip("Dodatkowe informacje")
        info_action.triggered.connect(lambda: self.statusBar().showMessage("Kliknięto: Dodatkowe info")) #LAMBDA - SKRÓCONA WERSJA ZAMIAST FUNKCJI
        more_menu.addAction(info_action)

        help_menu.addMenu(more_menu)

    def create_toolbar(self):
        toolbar = QToolBar("Główny pasek narzędzi", self)
        toolbar.setOrientation(Qt.Orientation.Vertical) #PIONOWY UKŁAD ZAD 2
        toolbar.setIconSize(QSize(32,32)) #ROZMIAR IKON ZAD2
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbar) #DODAJEMY Z LEWEJ STRONY

        #PRZYCISK 1:
        action1 = QAction(QIcon("C:/Users/lechowski_sz/Desktop/STUDIA UP/SEMESTR 4/PROGRAMOWANIE OBIEKTOWE II/otworz.png"), "Akcja 1", self)
        action1.setStatusTip("Kliknij aby zobaczyć grafikę OK")
        action1.triggered.connect(lambda: self.statusBar().showMessage("Kliknięto: Grafikę OK")) #LAMBDA - SKRÓCONA WERSJA ZAMIAST FUNKCJI
        toolbar.addAction(action1)

        #SEPARATOR:
        toolbar.addSeparator()

        #PRZYCISK 2:
        action2 = QAction(QIcon("C:/Users/lechowski_sz/Desktop/STUDIA UP/SEMESTR 4/PROGRAMOWANIE OBIEKTOWE II/Zamknij.png"), "Akcja 2", self)
        action2.setStatusTip("Kliknij aby zobaczyć grafikę X")
        action2.triggered.connect(lambda: self.statusBar().showMessage("Kliknięto: Grafika X")) #LAMBDA - SKRÓCONA WERSJA ZAMIAST FUNKCJI
        toolbar.addAction(action2)

        #PRZYCISK MODALNY ZADANIE 3:
        dialog_action = QAction("Pokaż dialog", self)
        dialog_action.setStatusTip("Otwiera okno modalne")
        dialog_action.triggered.connect(self.show_dialog)
        toolbar.addAction(dialog_action)

        #PRZYCISK DO ALERTU - ZADANIE 3
        alert_action = QAction("Pokaż alert", self)
        alert_action.setStatusTip("Pokazuje alert QMessageBox")
        alert_action.triggered.connect(self.show_alert)
        toolbar.addAction(alert_action)
         
    #ZADANIE 3 MODAL - SHOW DIALOG
    def show_dialog(self):
        dialog = MyDialog(self)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted and dialog.checkbox.isChecked():
            self.statusBar().showMessage("Użytkownik zaakceptował i zaznaczył checkbox")
        elif result == QDialog.DialogCode.Accepted:
            self.statusBar().showMessage("Użytkownik zaakceptował, ale nie zaznaczył checkbox")
        else:
            self.statusBar().showMessage("Użytkownik anulował")
    
    #ZADANIE 3 MODAL - SHOW ALERT
    def show_alert(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Uwaga")
        msg.setText("Czy na pewno chcesz kontynować?")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)

        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            self.statusBar().showMessage("Kliknięto TAK")
        else:
            self.statusBar().showMessage("Kliknięto NIE")

#KLASA MODALA -  ZADANIE 3
class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Okno modalne")
        self.setModal(True) #USTAWIENIE MODALNOŚCI ZADANIE 3
        self.setFixedSize(250, 150)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Czy chcesz kontynuować?"))

        self.checkbox = QCheckBox("Zaznacz, jeśli się zgadzasz")
        layout.addWidget(self.checkbox)

        self.button_ok = QPushButton("OK")
        self.button_cancel = QPushButton("Anuluj")

        self.button_ok.clicked.connect(self.accept) #KOŃCZY DIALOG Z KODEM ACCEPTED
        self.button_cancel.clicked.connect(self.reject) #KOŃCZY DIALOG Z KODEM REJECTED

        layout.addWidget(self.button_ok)
        layout.addWidget(self.button_cancel)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QCheckBox
from PySide6.QtGui import QPixmap, QTransform, QImage
from PySide6.QtCore import Qt
import sys

class PersistentImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persistent Image Window")
        self.setWindowFlags(self.windowFlags() | Qt.Tool | Qt.WindowStaysOnTopHint) #Ustawienie flag, żeby okno było "narzędziowe" i zawsze na wierzchu

        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)

        self.imageLabel = QLabel("Brak obrazu") #Etykieta wyświetlana na środku
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.imageLabel)

    def updateImage(self, pixmap): #Funkcja do aktualizacji obrazu
        if pixmap:
            scaled = pixmap.scaled(self.imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imageLabel.setPixmap(scaled) #Jeśli pixmap jest podany - przesakaluj go do rozmiaru etykiety i wyświetl.
        else:
            self.imageLabel.clear()
            self.imageLabel.setText("Brak obrazu") #W przeciwnym razie wyczyść obraz i pokaż tekst domyślny

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.imageLabel.pixmap():
            self.updateImage(self.imageLabel.pixmap()) #Po zmianie rozmiaru przeskaluj obraz ponownie

class ImageSettingsWindow(QMainWindow):
    def __init__(self, main_app):
        super().__init__() #Drugie okno do zmiany ustawień obrazu. Nadanie referencji do MainWindow
        self.setWindowTitle("Image Settings Window")
        self.main_app = main_app  #Referencja do glownego okna, dostep do biezacego pixmap

        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)

        self.grayscaleCheckBox = QCheckBox("Konwertuj do szarego") #Przelacznik na skale szarosci
        self.grayscaleCheckBox.stateChanged.connect(self.applySettings)
        self.layout.addWidget(self.grayscaleCheckBox)

        self.mirrorButton = QPushButton("Odbicie lustrzane") #Przycisk do odbicia lustrzanego
        self.mirrorButton.clicked.connect(self.applyMirror)
        self.layout.addWidget(self.mirrorButton)

    def applySettings(self):
        if self.main_app.pixmap:
            if self.grayscaleCheckBox.isChecked():
                image = self.main_app.original_pixmap.toImage().convertToFormat(QImage.Format_Grayscale8)
                grayscale_pixmap = QPixmap.fromImage(image)
                self.main_app.pixmap = grayscale_pixmap
            else:
                self.main_app.pixmap = QPixmap(self.main_app.original_pixmap)

            self.main_app.updateImageLabel()
            self.main_app.persistentWindow.updateImage(self.main_app.pixmap)

    def applyMirror(self):
        if self.main_app.pixmap:
            mirrored = self.main_app.pixmap.transformed(QTransform().scale(-1, 1))
            self.main_app.pixmap = mirrored  #Aktualizacja przechowanego obrazu
            self.main_app.updateImageLabel()   #Aktualizacja obrazu w glownym oknie
            self.main_app.persistentWindow.updateImage(mirrored)  #Aktualizacja presistet window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWindow 14_04_2025")
        self.pixmap = None  #Zmienna do przechowywania obrazu

        self.original_pixmap = None #Zapamiętaj orygianlny obraz

        #Utworzenie okna persistent i ustawienia jego pozycji
        self.persistentWindow = PersistentImageWindow()
        self.persistentWindow.move(self.x() + 650, self.y())

        #Okno on-demand - ustawienia obrazu, poczatkowo niewidoczne
        self.imageSettingsWindow = ImageSettingsWindow(self)

        #Glowny widget i layout
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.setCentralWidget(self.widget)

        #Etykieta obrazkowa
        self.imageLabel = QLabel("Wybierz obraz")
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.imageLabel)

        #Przycisk otwierajacy plik
        self.openButton = QPushButton("Otwórz")
        self.openButton.clicked.connect(self.openFile)
        self.layout.addWidget(self.openButton)

        #Przycisk zapisujacy plik
        self.saveButton = QPushButton("Zapisz")
        self.saveButton.clicked.connect(self.saveFile)
        self.layout.addWidget(self.saveButton)

        #Przycisk do otwierania okna ustawien
        self.settingsButton = QPushButton("Ustawienia obrazu")
        self.settingsButton.clicked.connect(self.showSettings)
        self.layout.addWidget(self.settingsButton)

    def openFile(self):
        #Wybor pliku za pomoca okna dialogowego
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Wybierz plik graficzny",
            "",  #Domyslna sciezka jako pusty ciag znakow
            "Pliki graficzne (*.jpg *.png)"
        )
        if fileName:
            self.pixmap = QPixmap(fileName)
            self.original_pixmap = QPixmap(fileName) #Zapamiętaj oryginał
            if not self.pixmap.isNull():
                self.updateImageLabel()
                self.persistentWindow.updateImage(self.pixmap)
                self.persistentWindow.show()
            else:
                self.imageLabel.setText("Nie udało się otworzyć obrazu") #Wczytanie obrazu do mapy, jeśli się uda to aktualizacja etykiety, w przeciwnym razie komunikat o błędzie.

    def saveFile(self):
        if self.pixmap is None:
            return  #Jeśli nie ma obrazu to nic nie rób
        fileName, _ = QFileDialog.getSaveFileName(
            self,
            "Zapisz jako",
            "",
            "Pliki graficzne (*.jpg *.png)" #Zapisanie pixmapy do pliku
        )
        if fileName:
            if not self.pixmap.save(fileName):
                print("Nie udalo sie zapisac obrazu")

    def showSettings(self):
        self.imageSettingsWindow.show() #Wyświetlenie okna ustawień

    def updateImageLabel(self):
        if self.pixmap:
            self.imageLabel.setPixmap(self.pixmap.scaled(
                self.imageLabel.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )) #Aktualizacja głównej etykiety obrazowej.

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateImageLabel()
        if self.persistentWindow.isVisible():
            self.persistentWindow.updateImage(self.pixmap) #Przy zmianie obrazu przeskalowanie obrazu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())

    # python "C:\Users\lechowski_sz\Desktop\PO_14_04_2025.py"
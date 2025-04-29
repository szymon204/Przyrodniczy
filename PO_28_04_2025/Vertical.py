import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Wczytanie pliku .ui
        loadUi("C:\\Users\\lechowski_sz\\Desktop\\QGrid.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



# python "C:\Users\lechowski_sz\Desktop\Vertical.py"
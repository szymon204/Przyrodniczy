import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("C:\\Users\\lechowski_sz\\Desktop\\Qgrid.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())




#python "C:\Users\lechowski_sz\Desktop\QGrid.py"
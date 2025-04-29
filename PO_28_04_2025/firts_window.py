from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\\Users\\lechowski_sz\\Desktop\\firts_window.ui", self)          
        # Zwiazanie funkcji z przyciskiem
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.label.setText("Tekst zmieniony po kliknieciu")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
# python "C:\Users\lechowski_sz\Desktop\firts_window.py"
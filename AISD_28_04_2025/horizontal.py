import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class LayoutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\\Users\\lechowski_sz\\Desktop\\horizontal.ui", self)

app = QApplication(sys.argv)
window = LayoutWindow()
window.show()
sys.exit(app.exec())
#python "C:\Users\lechowski_sz\Desktop\horizontal.py"   
#Layout Horizontally
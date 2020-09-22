import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUiType

form_class = loadUiType("Image Viewer.ui")[0]

class IVClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.b_prev.clicked.connect(self.b_prevClick)
        self.b_next.clicked.connect(self.b_nextClick)


    def b_precClick(self):









app = QApplication(sys.argv)
myWindow = IVClass(None)
myWindow.show()
app.exec()

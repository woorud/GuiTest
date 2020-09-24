import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUiType

form_class = loadUiType("table.ui")[0]

class ViewerClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.tableWidget.insertColumn(1)
        self.tableWidget.setHorizontalHeaderLabels(["A", "B", "C", "D", "E", "F"])
        self.tableWidget.setItem(0, 0, QTableWidgetItem("value00"))
        self.tableWidget.insertRow(0)
        self.tableWidget.verticalHeader().setVisible(False)

app = QApplication(sys.argv)
myWindow = ViewerClass(None)
myWindow.show()
app.exec()
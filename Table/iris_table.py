import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUiType
import pymysql
import pandas as pd

form_class = loadUiType("iris_table.ui")[0]

class ViewerClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        dbConn = pymysql.connect(user='######', passwd='######~', host='######', db='iris', charset='utf8')
        cursor = dbConn.cursor(pymysql.cursors.DictCursor)
        sql = "select a.SL, a.SW, a.PL, a.PW, b.Species_name from dataset a " \
              "left join flower b on a.species = b.species;"
        cursor.execute(sql)
        result = cursor.fetchall()
        result = pd.DataFrame(result)

        self.tableWidget.setColumnCount(len(result.columns))
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(result.columns)
        for i in range(len(result)):
            for j in range(len(result.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(result.iloc[i, j])))


app = QApplication(sys.argv)
myWindow = ViewerClass(None)
myWindow.show()
app.exec()
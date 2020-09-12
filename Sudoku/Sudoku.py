import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
import random

form_class = loadUiType("Sudoku.ui")[0]

class SudokuUi(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        global AVal, ButtonList

        ButtonList = [[self.b00, self.b01, self.b02, self.b03, self.b04, self.b05, self.b06, self.b07, self.b08],
                      [self.b10, self.b11, self.b12, self.b13, self.b14, self.b15, self.b16, self.b17, self.b18],
                      [self.b20, self.b21, self.b22, self.b23, self.b24, self.b25, self.b26, self.b27, self.b28],
                      [self.b30, self.b31, self.b32, self.b33, self.b34, self.b35, self.b36, self.b37, self.b38],
                      [self.b40, self.b41, self.b42, self.b43, self.b44, self.b45, self.b46, self.b47, self.b48],
                      [self.b50, self.b51, self.b52, self.b53, self.b54, self.b55, self.b56, self.b57, self.b58],
                      [self.b60, self.b61, self.b62, self.b63, self.b64, self.b65, self.b66, self.b67, self.b68],
                      [self.b70, self.b71, self.b72, self.b73, self.b74, self.b75, self.b76, self.b77, self.b78],
                      [self.b80, self.b81, self.b82, self.b83, self.b84, self.b85, self.b86, self.b87, self.b88]]

        for i in range(0, 9):
            for number in self.ButtonList[i]:
                number.clicked.connect(self.NumClick())

        self.AVal = []

        for i in range(0, 9):
            tmp = []
            for j in range(0, 9):
                tmp.append(str(self.ButtonList[i][j].text()))
            self.AVal.append(tmp)

        self.ShuffleClick()
        self.ShuffleButton.clicked.connect(self.ShuffleClick)
        self.FinishButoon.clicked.connedt(self.CompleteTextClick)

    def ShuffleClick(self):
        random19 = list(range(1, 10))
        random.shuffle(random19)

        for i in range(0, 9):
            for j in range(0, 9):
                self.ButtonList[i][j].setText(str(random19[int(self.AVal[i][j])-1]))

        for i in range(0, 9):
            for j in range(0, 9):
                if random.random() > float(self.pedit.text()):
                    self.ButtonList[i][j].setText("")




    def NumClick(self): # 내가 누른 위치의 키보드 값을 저장한다.
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sender() == self.ButtonList[i][j]:
                    self.xloc = i
                    self.yloc = j
                    print(self.xloc, self.yloc)

    def KeyPressEvent(self, event):
        if type(event) == QKeyEvent: # 키보드에 key를 입력
            if event.key() == Qt.Key_1:
                self.ButtonList[self.xloc][self.yloc].setText("1")
            elif event.key() == Qt.Key_2:
                self.ButtonList[self.xloc][self.yloc].setText("2")
            elif event.key() == Qt.Key_3:
                self.ButtonList[self.xloc][self.yloc].setText("3")
            elif event.key() == Qt.Key_4:
                self.ButtonList[self.xloc][self.yloc].setText("4")
            elif event.key() == Qt.Key_5:
                self.ButtonList[self.xloc][self.yloc].setText("5")
            elif event.key() == Qt.Key_6:
                self.ButtonList[self.xloc][self.yloc].setText("6")
            elif event.key() == Qt.Key_7:
                self.ButtonList[self.xloc][self.yloc].setText("7")
            elif event.key() == Qt.Key_8:
                self.ButtonList[self.xloc][self.yloc].setText("8")
            elif event.key() == Qt.Key_9:
                self.ButtonList[self.xloc][self.yloc].setText("9")




app = QApplication(sys.argv)
myGame = SudokuUi(None)
myGame.show()
app.exec()
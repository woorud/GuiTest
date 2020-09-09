import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType
import math

form_class = loadUiType("my_calc.ui")[0]

class CalcClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        numbers = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        for num in numbers:
            num.clicked.connect(self.Nums)
        self.b_del.clicked.connect(self.b_delClick)
        self.b_clear.clicked.connect(self.b_clearClick)
        self.b_run.clicked.connect(self.b_runClick)
        self.b_plus.clicked.connect(self.b_plusClick)
        self.b_minus.clicked.connect(self.b_minusClick)
        self.b_mul.clicked.connect(self.b_mulClick)
        self.b_divide.clicked.connect(self.b_devideClick)
        self.b_dot.clicked.connect(self.b_dotClick)
        self.b_lb.clicked.connect(self.b_lbClick)
        self.b_rb.clicked.connect(self.b_rbClick)
        self.b_percentage.clicked.connect(self.b_percentageClick)
        self.b_factorial.clicked.connect(self.b_factorialClick)
        self.b_pi.clicked.connect(self.b_piClick)
        self.b_rec.clicked.connect(self.b_recClick)
        self.b_sin.clicked.connect(self.b_sinClick)
        self.b_cos.clicked.connect(self.b_cosClick)
        self.b_tan.clicked.connect(self.b_tanClick)
        self.b_ln.clicked.connect(self.b_lnClick)
        self.b_log.clicked.connect(self.b_logClick)
        self.b_route.clicked.connect(self.b_routeClick)
        self.b_inch.clicked.connect(self.b_inchClick)
        self.b_feet.clicked.connect(self.b_feetClick)
        self.b_lbs.clicked.connect(self.b_lbsClick)

    def Nums(self):
        global num
        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)
        if self.result.text() == "0":
            self.result.setText(setNum)
        else:
            self.result.setText(self.result.text() + setNum)

    def b_delClick(self):
        n = len(self.result.text())
        self.result.setText(self.result.text()[0:-1])
        if self.result.text() == '':
            self.result.setText("0")

    def b_clearClick(self):
        self.result.setText("0")

    def b_runClick(self):
        self.result.setText(str(eval(self.result.text())))

    def b_plusClick(self):
        self.result.setText(self.result.text() + "+")

    def b_minusClick(self):
        self.result.setText(self.result.text() + "-")

    def b_mulClick(self):
        self.result.setText(self.result.text() + "*")

    def b_devideClick(self):
        self.result.setText(self.result.text() + "/")

    def b_dotClick(self):
        self.result.setText(self.result.text() + ".")

    def b_lbClick(self):
        if self.result.text() == "0":
            self.result.setText("(")
        else:
            self.result.setText(self.result.text() + "(")

    def b_rbClick(self):
        if self.result.text() == "0":
            self.result.setText(")")
        else:
            self.result.setText(self.result.text() + ")")

    def b_percentageClick(self):
        self.result.setText(str(int(self.result.text()) * 0.01))

    def b_factorialClick(self):
        tmp = int(self.result.text())
        res = 1
        while tmp:
            res *= tmp
            tmp -= 1
        self.result.setText(str(res))

    def b_piClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(tmp*math.pi))

    def b_recClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(1/tmp))

    def b_sinClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(math.sin(tmp)))

    def b_cosClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(math.cos(tmp)))

    def b_tanClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(math.tan(tmp)))


    def b_lnClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(math.log(tmp)))

    def b_logClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(math.log10(tmp)))

    def b_routeClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(tmp**0.5))

    def b_inchClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(tmp/2.54))

    def b_feetClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(tmp/30.48))

    def b_lbsClick(self):
        tmp = int(self.result.text())
        self.result.setText(str(tmp*2.205))

app = QApplication(sys.argv)
myWindow = CalcClass(None)
myWindow.show()
app.exec()



























import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt

form_class = loadUiType("Sudoku.ui")[0]

class SudokuUi(QMainWindow, form_class):
    def __init__(self, parent=None):

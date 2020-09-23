import sys
import cv2
import glob
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog, QApplication
from PyQt5.uic import loadUiType

form_class = loadUiType("Image Viewer.ui")[0]
valid_format = (".PNG", ".JPEG", ".JPG", ".BMP", ".GIF")

def getImgs(folder):
    img_list = []
    if os.path.isdir(folder):
        for file in os.listdir(folder):
            if file.upper().endswith(valid_format):
                im_path = os.path.join(folder, file)
                img_list.append(im_path)
    return img_list
# print(getImgs("C:/Users/82102/Desktop/woorud/Github/GuiTest/Image Viewer/chelsea"))

class ImageViewer(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.a_fileselect.triggered.connect(self.fileselect)
        self.a_folderselect.triggered.connect(self.folderselect)
        self.a_exit.triggered.connect(self.exit)

        self.b_prev.clicked.connect(self.prev)
        self.b_next.clicked.connect(self.next)

    def fileselect(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  'Select File',
                                                  '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)',
                                                  options=options)
        if fileName:
            img = QImage(fileName).scaled(640, 640, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            if img.isNull():
                QMessageBox.warnig(self, "Image Viewer", "Can't Load %s." % fileName)
                return

        self.l_image.setPixmap(QPixmap.fromImage(img))
        print(img)

    def folderselect(self):
        self.folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if not self.folder:
            QMessageBox.warning(self, "Image Viewer", "Can't Load this directory.")
            return

        self.logs = getImgs(self.folder)
        self.numImgs = len(self.logs)
        self.imgs = []
        for file in self.logs:
            img = QImage(file).scaled(640, 640, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.imgs.append(img)

        self.idx = 0
        self.l_image.setPixmap(QPixmap.fromImage(self.imgs[self.idx]))

    def exit(self):
        reply = QMessageBox.question(self,
                                     "Quit",
                                     "Are you sure?",
                                     QMessageBox.Yes|QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def prev(self):
        if self.idx > 0:
            self.idx -= 1
            self.l_image.setPixmap(QPixmap.fromImage(self.imgs[self.idx]))
        else:
            QMessageBox.warning(self, 'Sorry', 'No more images!')

    def next(self):
        if self.idx < self.numImgs-1:
            self.idx += 1
            self.l_image.setPixmap(QPixmap.fromImage(self.imgs[self.idx]))
        else:
            QMessageBox.warning(self, 'Sorry', 'No more images!')


app = QApplication(sys.argv)
my_window = ImageViewer(None)
my_window.show()
app.exec()

import sys
import cv2
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QTransform
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QApplication
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

        self.scaleFactor = 0.0
        # file
        self.a_fileselect.triggered.connect(self.fileselect)
        self.a_folderselect.triggered.connect(self.folderselect)
        self.a_exit.triggered.connect(self.exit)

        # button
        self.b_prev.clicked.connect(self.prev)
        self.b_next.clicked.connect(self.next)

        # edit
        self.a_togray.triggered.connect(self.togray)
        self.a_zi.triggered.connect(self.zoomin)
        self.a_zo.triggered.connect(self.zoomout)
        self.a_rotate.triggered.connect(self.rotate)

    def fileselect(self):
        global fileName
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
        self.scaleFactor = 1.0
        self.b_prev.setEnabled(False)
        self.b_next.setEnabled(False)

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
        self.scaleFactor = 1.0

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

    def togray(self):
        global fileName
        img = cv2.imread(fileName)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        r_img = img[:,:,0]
        g_img = img[:,:,1]
        b_img = img[:,:,2]
        imgGray = 0.21*r_img + 0.72*g_img + 0.07*b_img
        img[:, :, 0] = imgGray
        img[:, :, 1] = imgGray
        img[:, :, 2] = imgGray
        img = QImage(img, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888).scaled(640, 640,  Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.qPixmapVar = QPixmap(img)
        self.l_image.setPixmap(self.qPixmapVar)

    def rotate(self):
        global fileName
        angle = 90
        self.pixmap = QPixmap(fileName).scaled(640, 640, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        rotated = self.pixmap.transformed(QTransform().rotate(angle))
        self.l_image.setPixmap(rotated)

    def zoomin(self):
        self.sclaleImage(1.25)

    def zoomout(self):
        self.scaleImage(0.75)

    def scaleImage(self, factor):
        global fileName
        self.scaleFactor *= factor


app = QApplication(sys.argv)
my_window = ImageViewer(None)
my_window.show()
app.exec()

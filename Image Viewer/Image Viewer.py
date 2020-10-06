from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from PyQt5.QtGui import QImage, QPixmap, QTransform
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QApplication, QRubberBand
from PyQt5.uic import loadUiType
import sys
import cv2
import os

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

        # origin
        self.hh = 640
        self.ww = 640
        self.idx = 0
        self.origin = QPoint()
        self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
        self.cropEnable = False

        # file
        self.a_fileselect.triggered.connect(self.fileselect)
        self.a_folderselect.triggered.connect(self.folderselect)
        self.a_exit.triggered.connect(self.exit)

        # button
        self.b_prev.clicked.connect(self.prev)
        self.b_next.clicked.connect(self.next)

        # edit
        self.a_togray.triggered.connect(self.togray)
        self.a_rotate.triggered.connect(self.rotate)
        self.a_crop.triggered.connect(self.crop)
        self.a_original.triggered.connect(self.original)

    def fileselect(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self,
                                                  'Select File',
                                                  '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)',
                                                  options=options)

        self.img = cv2.imread(self.fileName)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img_height_origin = self.img.shape[0]
        self.img_width_origin = self.img.shape[1]
        # print(self.img_height_origin, self.img_width_origin)
        self.image2Label(self.img)
        self.b_prev.setEnabled(False)
        self.b_next.setEnabled(False)

    def folderselect(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.logs = getImgs(directory)
        self.numImgs = len(self.logs)
        # ['C:/Users/82102/Desktop/woorud/Github/GuiTest/picture\\IMG_0782.jpg',
        #  'C:/Users/82102/Desktop/woorud/Github/GuiTest/picture\\IMG_0783.jpg',
        #  'C:/Users/82102/Desktop/woorud/Github/GuiTest/picture\\IMG_2189.JPG',
        #  'C:/Users/82102/Desktop/woorud/Github/GuiTest/picture\\IMG_5186.jpg',
        #  'C:/Users/82102/Desktop/woorud/Github/GuiTest/picture\\IMG_5232.jpg']
        self.img = cv2.imread(self.logs[self.idx])
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img_height_origin = self.img.shape[0]
        self.img_width_origin = self.img.shape[1]
        self.image2Label(self.img)


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
            self.img = cv2.imread(self.logs[self.idx])
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.fileName = self.logs[self.idx]
            self.image2Label(self.img)
        else:
            QMessageBox.warning(self, 'Sorry', 'No more images!')

    def next(self):
        if self.idx < self.numImgs-1:
            self.idx += 1
            self.img = cv2.imread(self.logs[self.idx])
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.fileName = self.logs[self.idx]
            self.image2Label(self.img)
        else:
            QMessageBox.warning(self, 'Sorry', 'No more images!')

    def togray(self):
        r_img = self.img[:,:,0]
        g_img = self.img[:,:,1]
        b_img = self.img[:,:,2]
        imgGray = 0.21*r_img + 0.72*g_img + 0.07*b_img
        self.img[:, :, 0] = imgGray
        self.img[:, :, 1] = imgGray
        self.img[:, :, 2] = imgGray
        self.image2Label(self.img)

    def rotate(self):
        self.img = cv2.rotate(self.img, cv2.ROTATE_90_CLOCKWISE)
        self.image2Label(self.img)

    def crop(self):
        self.cropEnable = True
        self.hw_ratio = self.img_height_origin / self.img_width_origin
        # print(self.hw_ratio)

        if self.hw_ratio > 1: # 세로사진이라면 높이가 최대 길이, 너비가 비례로 축소
            self.img_height_tran = self.hh
            self.img_width_tran = int(self.img_height_tran / self.img_height_origin * self.img_width_origin)
        else: # 가로사진이라면 너비가 최대 너비, 높이가 비례로 축소
            self.img_width_tran = self.ww
            self.img_height_tran = int(self.img_width_tran / self.img_width_origin * self.img_height_origin)
        # print(self.img_height_tran, self.img_width_tran)

        if self.img_width_tran < self.ww: # 너비가 축소되었다면, 상대 좌표 구하기
            self.startpos = QPoint((self.ww - self.img_width_tran) // 2, 0)
            self.endpos = QPoint(self.startpos.x() + self.img_width_tran, self.ww)
            # print(self.startpos, self.endpos)
        else: # 높이가 축소되었다면, 상대 좌표 구하기
            self.startpos = QPoint(0, (self.hh - self.img_height_tran))
            self.endpos = QPoint(self.hh, self.startpos.y() + self.img_height_tran)
            # print(self.startpos, self.endpos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = QPoint(event.pos())
            self.rubberband.setGeometry(QRect(self.origin, QSize()))
            self.rubberband.show()

    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            self.rubberband.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rubberband.hide()

        if self.cropEnable == True:
            self.selStart = self.origin - self.startpos - QPoint(0, 20)
            self.selEnd = event.pos() - self.startpos - QPoint(0, 20)
            # print(self.selStart, self.selEnd)

            cut_begin_x = int(self.img_width_origin * self.selStart.x() / self.img_width_tran)
            cut_begin_y = int(self.img_height_origin * self.selStart.y() / self.img_height_tran)
            cut_end_x = int(self.img_width_origin * self.selEnd.x() / self.img_width_tran)
            cut_end_y = int(self.img_height_origin * self.selEnd.y() / self.img_height_tran)
            # print(cut_begin_x, cut_begin_y, cut_end_x, cut_end_y)

            # self.img = cv2.imread(self.fileName)
            # self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.img = self.img[cut_begin_y:cut_end_y, cut_begin_x:cut_end_x, :].astype("uint8")
            self.image2Label(self.img)
            self.cropEnable = False

    def image2Label(self, img):
        self.qPixmapVar = QPixmap(self.image2QImage(img))
        self.qPixmapVar = self.qPixmapVar.scaled(self.hh, self.ww, aspectRatioMode=True)
        self.l_image.setPixmap(self.qPixmapVar)

    def file2QImage(self, fileName):
        img = cv2.imread(fileName)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return QImage(img, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888)

    def image2QImage(self, img):
        return QImage(img, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888)

    def original(self):
        self.img = cv2.imread(self.fileName)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.image2Label(self.img)

app = QApplication(sys.argv)
my_window = ImageViewer(None)
my_window.show()
app.exec()
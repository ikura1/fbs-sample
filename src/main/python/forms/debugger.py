import os
from forms.ui.window import Ui_MainWindow
from forms.image_widget import ImageWidget

from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QImage, QPalette, QColor, QPixmap
from PySide2.QtWidgets import (
    QSizePolicy,
    QMainWindow,
    QFileDialog,
)
import cv2


class Debugger(QMainWindow):
    target_file = ""
    kijyun_file = ""

    def __init__(self):
        super(Debugger, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_image_widget()

    def init_image_widget(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(220, 220, 222))
        self.image_widget = ImageWidget(self)
        self.image_widget.setPalette(palette)
        self.image_widget.setBackgroundRole(QPalette.Background)
        self.image_widget.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_widget.setScaledContents(True)
        self.image_widget.setAlignment(Qt.AlignCenter)
        # self.image_widget.mouse_pressed.connect(self.data.receive_position)

        self.ui.mainScrollArea.setWidgetResizable(False)
        self.ui.mainScrollArea.setAlignment(Qt.AlignCenter)
        self.ui.mainScrollArea.setWidget(self.image_widget)
        print("END INIT_IMAGE_WIDGET")

    @Slot()
    def on_targetPushButton_clicked(self):
        self.target_file = self.file_select(self.ui.targetLineEdit) or self.target_file

    @Slot()
    def on_kijunPushButton_clicked(self):
        self.kijyun_file = self.file_select(self.ui.kijunLineEdit) or self.kijyun_file

    def file_select(self, widget):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Files (*.*)")
        if filename:
            widget.setText(os.path.basename(filename))
        return filename

    @Slot()
    def on_pushButton_3_clicked(self):
        print("clicked")
        img = cv2.imread(self.target_file)
        # img2qimage
        qimg = QImage(
            img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888
        )
        self.image_widget.set_image(qimg)

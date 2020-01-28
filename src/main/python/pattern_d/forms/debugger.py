import os
from forms.ui.window import Ui_MainWindow
from forms.image_widget import ImageWidget

from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QImage, QPalette, QColor
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
        self.image_widget = ImageWidget(self)
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(220, 220, 222))
        self.image_widget.setPalette(palette)
        self.image_widget.setBackgroundRole(QPalette.Background)
        self.image_widget.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_widget.setScaledContents(True)
        self.image_widget.setAlignment(Qt.AlignCenter)

        self.ui.mainScrollArea.setWidgetResizable(False)
        self.ui.mainScrollArea.setAlignment(Qt.AlignCenter)
        self.ui.mainScrollArea.setWidget(self.image_widget)

    @Slot()
    def on_targetPushButton_clicked(self):
        self.target_file = self.file_select(self.ui.targetLineEdit) or self.target_file

    def file_select(self, widget):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Files (*.*)")
        if filename:
            widget.setText(os.path.basename(filename))
        return filename

    @Slot()
    def on_pushButton_3_clicked(self):
        img = cv2.imread(self.target_file)
        qimg = QImage(
            img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888
        )
        # qimg = QImage(self.target_file)
        self.image_widget.set_image(qimg)

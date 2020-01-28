from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QLabel


class ImageWidget(QLabel):
    def __init__(self, parent=None):
        super(ImageWidget, self).__init__(parent)
        self.image = QImage()

    def set_image(self, image):
        print("set_image")
        self.image = image
        self.resize(self.image.size())
        pixmap = QPixmap.fromImage(self.image)
        self.setPixmap(pixmap)

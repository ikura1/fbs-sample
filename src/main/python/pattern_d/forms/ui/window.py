# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(677, 491)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainBoxLayout = QGridLayout()
        self.MainBoxLayout.setObjectName(u"MainBoxLayout")
        self.horizontalSpacer = QSpacerItem(600, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MainBoxLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.MainBoxLayout.addWidget(self.pushButton_3, 4, 1, 1, 1)

        self.mainScrollArea = QScrollArea(self.centralwidget)
        self.mainScrollArea.setObjectName(u"mainScrollArea")
        self.mainScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 655, 397))
        self.mainScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.MainBoxLayout.addWidget(self.mainScrollArea, 1, 0, 1, 2)

        self.targetLayout = QHBoxLayout()
        self.targetLayout.setObjectName(u"targetLayout")
        self.targetLabel = QLabel(self.centralwidget)
        self.targetLabel.setObjectName(u"targetLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetLabel.sizePolicy().hasHeightForWidth())
        self.targetLabel.setSizePolicy(sizePolicy)

        self.targetLayout.addWidget(self.targetLabel)

        self.targetLineEdit = QLineEdit(self.centralwidget)
        self.targetLineEdit.setObjectName(u"targetLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.targetLineEdit.sizePolicy().hasHeightForWidth())
        self.targetLineEdit.setSizePolicy(sizePolicy1)

        self.targetLayout.addWidget(self.targetLineEdit)

        self.targetPushButton = QPushButton(self.centralwidget)
        self.targetPushButton.setObjectName(u"targetPushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.targetPushButton.sizePolicy().hasHeightForWidth())
        self.targetPushButton.setSizePolicy(sizePolicy2)

        self.targetLayout.addWidget(self.targetPushButton)


        self.MainBoxLayout.addLayout(self.targetLayout, 0, 0, 1, 2)


        self.horizontalLayout.addLayout(self.MainBoxLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.targetLabel.setText(QCoreApplication.translate("MainWindow", u"Target", None))
        self.targetPushButton.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecognitionWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 798)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 181, 761))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.RealTimeDetectButton = QPushButton(self.frame)
        self.RealTimeDetectButton.setObjectName(u"RealTimeDetectButton")

        self.verticalLayout.addWidget(self.RealTimeDetectButton)

        self.ImageDetectButton = QPushButton(self.frame)
        self.ImageDetectButton.setObjectName(u"ImageDetectButton")

        self.verticalLayout.addWidget(self.ImageDetectButton)

        self.VideoDetectButton = QPushButton(self.frame)
        self.VideoDetectButton.setObjectName(u"VideoDetectButton")

        self.verticalLayout.addWidget(self.VideoDetectButton)

        self.SaveResultButton = QPushButton(self.frame)
        self.SaveResultButton.setObjectName(u"SaveResultButton")

        self.verticalLayout.addWidget(self.SaveResultButton)

        self.SignOutButton = QPushButton(self.frame)
        self.SignOutButton.setObjectName(u"SignOutButton")

        self.verticalLayout.addWidget(self.SignOutButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 10, 1061, 65))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MainDisplay = QLabel(self.centralwidget)
        self.MainDisplay.setObjectName(u"MainDisplay")
        self.MainDisplay.setGeometry(QRect(180, 90, 761, 471))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainDisplay.sizePolicy().hasHeightForWidth())
        self.MainDisplay.setSizePolicy(sizePolicy)
        self.MainDisplay.setMinimumSize(QSize(569, 454))
        self.MainDisplay.setMaximumSize(QSize(1152, 648))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(16)
        self.MainDisplay.setFont(font)
        self.MainDisplay.setLayoutDirection(Qt.LeftToRight)
        self.MainDisplay.setStyleSheet(u"border-image: url(:/images/icons/ini-image.png);")
        self.MainDisplay.setPixmap(QPixmap(u"resourse/VehicleLicense_SIXU_A00326.jpg"))
        self.MainDisplay.setScaledContents(True)
        self.MainDisplay.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(950, 90, 291, 471))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ZoomDisplay = QLabel(self.widget)
        self.ZoomDisplay.setObjectName(u"ZoomDisplay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ZoomDisplay.sizePolicy().hasHeightForWidth())
        self.ZoomDisplay.setSizePolicy(sizePolicy1)
        self.ZoomDisplay.setMinimumSize(QSize(0, 0))
        self.ZoomDisplay.setMaximumSize(QSize(1152, 648))
        self.ZoomDisplay.setFont(font)
        self.ZoomDisplay.setLayoutDirection(Qt.LeftToRight)
        self.ZoomDisplay.setStyleSheet(u"border-image: url(:/images/icons/ini-image.png);")
        self.ZoomDisplay.setPixmap(QPixmap(u"resourse/ExampleCarPlate.png"))
        self.ZoomDisplay.setScaledContents(True)
        self.ZoomDisplay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ZoomDisplay)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_char = QLabel(self.widget)
        self.label_char.setObjectName(u"label_char")
        font1 = QFont()
        font1.setFamilies([u"\u534e\u6587\u4eff\u5b8b"])
        font1.setPointSize(14)
        self.label_char.setFont(font1)
        self.label_char.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_char)

        self.label_plate_str = QLabel(self.widget)
        self.label_plate_str.setObjectName(u"label_plate_str")
        font2 = QFont()
        font2.setFamilies([u"SimSun"])
        font2.setPointSize(14)
        self.label_plate_str.setFont(font2)
        self.label_plate_str.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_plate_str.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_plate_str)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_char_2 = QLabel(self.widget)
        self.label_char_2.setObjectName(u"label_char_2")
        self.label_char_2.setFont(font1)
        self.label_char_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_char_2)

        self.label_plate_str_2 = QLabel(self.widget)
        self.label_plate_str_2.setObjectName(u"label_plate_str_2")
        self.label_plate_str_2.setFont(font2)
        self.label_plate_str_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_plate_str_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_plate_str_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1258, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RealTimeDetectButton.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u5b9e\u65f6\u68c0\u6d4b\u8f66\u724c", None))
        self.ImageDetectButton.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u56fe\u7247\u8bc6\u522b\u8f66\u724c", None))
        self.VideoDetectButton.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u89c6\u9891\u8bc6\u522b\u8f66\u724c", None))
        self.SaveResultButton.setText(QCoreApplication.translate("MainWindow", u"\u50a8\u5b58\u8bc6\u522b\u7ed3\u679c", None))
        self.SignOutButton.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5165", None))
        self.MainDisplay.setText("")
        self.ZoomDisplay.setText("")
        self.label_char.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u8bc6\u522b\u8f66\u724c\uff1a</span></p></body></html>", None))
        self.label_plate_str.setText(QCoreApplication.translate("MainWindow", u"B 126 NTB", None))
        self.label_char_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u8f66\u724c\u989c\u8272</span></p></body></html>", None))
        self.label_plate_str_2.setText(QCoreApplication.translate("MainWindow", u"\u9ed1\u8272", None))
    # retranslateUi


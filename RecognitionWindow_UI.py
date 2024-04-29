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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.ImageDetectButton = QPushButton(self.frame)
        self.ImageDetectButton.setObjectName(u"ImageDetectButton")

        self.verticalLayout.addWidget(self.ImageDetectButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.VideoDetectButton = QPushButton(self.frame)
        self.VideoDetectButton.setObjectName(u"VideoDetectButton")

        self.verticalLayout.addWidget(self.VideoDetectButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.RealTimeDetectButton = QPushButton(self.frame)
        self.RealTimeDetectButton.setObjectName(u"RealTimeDetectButton")

        self.verticalLayout.addWidget(self.RealTimeDetectButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.SaveResultButton = QPushButton(self.frame)
        self.SaveResultButton.setObjectName(u"SaveResultButton")

        self.verticalLayout.addWidget(self.SaveResultButton)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.SignOutButton = QPushButton(self.frame)
        self.SignOutButton.setObjectName(u"SignOutButton")

        self.verticalLayout.addWidget(self.SignOutButton)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 10, 1061, 65))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.verticalLayoutWidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u65b0\u9b4f"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_title)

        self.MainDisplay = QLabel(self.centralwidget)
        self.MainDisplay.setObjectName(u"MainDisplay")
        self.MainDisplay.setGeometry(QRect(180, 90, 701, 471))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainDisplay.sizePolicy().hasHeightForWidth())
        self.MainDisplay.setSizePolicy(sizePolicy)
        self.MainDisplay.setMinimumSize(QSize(569, 454))
        self.MainDisplay.setMaximumSize(QSize(1152, 648))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(16)
        self.MainDisplay.setFont(font1)
        self.MainDisplay.setLayoutDirection(Qt.LeftToRight)
        self.MainDisplay.setStyleSheet(u"border-image: url(:/images/icons/ini-image.png);")
        self.MainDisplay.setPixmap(QPixmap(u"resourse/ExampleCar.jpg"))
        self.MainDisplay.setScaledContents(True)
        self.MainDisplay.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(890, 90, 351, 471))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ZoomDisplay = QLabel(self.layoutWidget)
        self.ZoomDisplay.setObjectName(u"ZoomDisplay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ZoomDisplay.sizePolicy().hasHeightForWidth())
        self.ZoomDisplay.setSizePolicy(sizePolicy1)
        self.ZoomDisplay.setMinimumSize(QSize(0, 0))
        self.ZoomDisplay.setMaximumSize(QSize(1152, 648))
        self.ZoomDisplay.setFont(font1)
        self.ZoomDisplay.setLayoutDirection(Qt.LeftToRight)
        self.ZoomDisplay.setStyleSheet(u"border-image: url(:/images/icons/ini-image.png);")
        self.ZoomDisplay.setPixmap(QPixmap(u"resourse/ExampleCarPlate.png"))
        self.ZoomDisplay.setScaledContents(True)
        self.ZoomDisplay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ZoomDisplay)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_char = QLabel(self.layoutWidget)
        self.label_char.setObjectName(u"label_char")
        font2 = QFont()
        font2.setFamilies([u"\u534e\u6587\u4eff\u5b8b"])
        font2.setPointSize(14)
        self.label_char.setFont(font2)
        self.label_char.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_char)

        self.label_plate_str = QLabel(self.layoutWidget)
        self.label_plate_str.setObjectName(u"label_plate_str")
        font3 = QFont()
        font3.setFamilies([u"SimSun"])
        font3.setPointSize(14)
        self.label_plate_str.setFont(font3)
        self.label_plate_str.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_plate_str.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_plate_str)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.DataTable = QTableWidget(self.centralwidget)
        if (self.DataTable.columnCount() < 5):
            self.DataTable.setColumnCount(5)
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(9)
        font4.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0, 0));
        self.DataTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.DataTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.DataTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.DataTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.DataTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.DataTable.rowCount() < 6):
            self.DataTable.setRowCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.DataTable.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.DataTable.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.DataTable.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.DataTable.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.DataTable.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.DataTable.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.DataTable.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.DataTable.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.DataTable.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.DataTable.setItem(2, 2, __qtablewidgetitem14)
        self.DataTable.setObjectName(u"DataTable")
        self.DataTable.setGeometry(QRect(180, 570, 1061, 180))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DataTable.sizePolicy().hasHeightForWidth())
        self.DataTable.setSizePolicy(sizePolicy2)
        self.DataTable.setMinimumSize(QSize(569, 150))
        self.DataTable.setMaximumSize(QSize(1152, 180))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei UI"])
        font6.setPointSize(10)
        self.DataTable.setFont(font6)
        self.DataTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.DataTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DataTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.DataTable.setAlternatingRowColors(True)
        self.DataTable.setWordWrap(False)
        self.DataTable.setRowCount(6)
        self.DataTable.horizontalHeader().setVisible(True)
        self.DataTable.horizontalHeader().setCascadingSectionResizes(False)
        self.DataTable.horizontalHeader().setDefaultSectionSize(210)
        self.DataTable.horizontalHeader().setStretchLastSection(False)
        self.DataTable.verticalHeader().setVisible(True)
        self.DataTable.verticalHeader().setCascadingSectionResizes(False)
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
        self.ImageDetectButton.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u56fe\u7247\u8bc6\u522b\u8f66\u724c", None))
        self.VideoDetectButton.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u89c6\u9891\u8bc6\u522b\u8f66\u724c", None))
        self.RealTimeDetectButton.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u5b9e\u65f6\u68c0\u6d4b\u8f66\u724c", None))
        self.SaveResultButton.setText(QCoreApplication.translate("MainWindow", u"\u50a8\u5b58\u8bc6\u522b\u7ed3\u679c", None))
        self.SignOutButton.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5165", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8eYOLOv5 & LPRNet\u7684\u8f66\u724c\u68c0\u6d4b\u7cfb\u7edf", None))
        self.MainDisplay.setText("")
        self.ZoomDisplay.setText("")
        self.label_char.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u8bc6\u522b\u8f66\u724c\uff1a</span></p></body></html>", None))
        self.label_plate_str.setText(QCoreApplication.translate("MainWindow", u"B 126 NTB", None))
        ___qtablewidgetitem = self.DataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None));
        ___qtablewidgetitem1 = self.DataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u6233", None));
        ___qtablewidgetitem2 = self.DataTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u5750\u6807", None));
        ___qtablewidgetitem3 = self.DataTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6", None));
        ___qtablewidgetitem4 = self.DataTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7\u7801", None));
        ___qtablewidgetitem5 = self.DataTable.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem6 = self.DataTable.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.DataTable.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.DataTable.isSortingEnabled()
        self.DataTable.setSortingEnabled(False)
        self.DataTable.setSortingEnabled(__sortingEnabled)

    # retranslateUi


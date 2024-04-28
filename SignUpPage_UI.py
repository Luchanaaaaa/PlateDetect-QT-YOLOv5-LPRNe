# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignUpPage.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

from StyleSetter import StyleSetter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(886, 625)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UserNameInputBox = QPlainTextEdit(self.centralwidget)
        self.UserNameInputBox.setObjectName(u"UserNameInputBox")
        self.UserNameInputBox.setGeometry(QRect(480, 230, 301, 31))
        self.PassWordInputBox = QPlainTextEdit(self.centralwidget)
        self.PassWordInputBox.setObjectName(u"PassWordInputBox")
        self.PassWordInputBox.setGeometry(QRect(480, 270, 301, 31))
        self.SignUpButton = QPushButton(self.centralwidget)
        self.SignUpButton.setObjectName(u"SignUpButton")
        self.SignUpButton.setGeometry(QRect(480, 350, 301, 24))
        self.BackGroundGraphicsView = QGraphicsView(self.centralwidget)
        self.BackGroundGraphicsView.setObjectName(u"BackGroundGraphicsView")
        self.BackGroundGraphicsView.setGeometry(QRect(0, 0, 391, 581))
        self.PassWordInputBox_Confirm = QPlainTextEdit(self.centralwidget)
        self.PassWordInputBox_Confirm.setObjectName(u"PassWordInputBox_Confirm")
        self.PassWordInputBox_Confirm.setGeometry(QRect(480, 310, 301, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 886, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        StyleSetter.setBackgroundImage(self.BackGroundGraphicsView, "resources/SignUpLogIn.png")


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.UserNameInputBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u7528\u6237\u540d", None))
        self.PassWordInputBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u7684\u5bc6\u7801", None))
        self.SignUpButton.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.PassWordInputBox_Confirm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u91cd\u590d\u8bbe\u7f6e\u7684\u5bc6\u7801", None))
    # retranslateUi


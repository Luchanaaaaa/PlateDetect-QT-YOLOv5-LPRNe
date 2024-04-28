# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogInPage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

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
        self.AutoLogInCheckBox = QCheckBox(self.centralwidget)
        self.AutoLogInCheckBox.setObjectName(u"AutoLogInCheckBox")
        self.AutoLogInCheckBox.setGeometry(QRect(480, 310, 81, 22))
        self.LogInButton = QPushButton(self.centralwidget)
        self.LogInButton.setObjectName(u"LogInButton")
        self.LogInButton.setGeometry(QRect(480, 350, 301, 24))
        self.ForgetPassWordTextLabel = QLabel(self.centralwidget)
        self.ForgetPassWordTextLabel.setObjectName(u"ForgetPassWordTextLabel")
        self.ForgetPassWordTextLabel.setGeometry(QRect(730, 310, 54, 16))
        self.SignUpLinkLabel = QLabel(self.centralwidget)
        self.SignUpLinkLabel.setObjectName(u"SignUpLinkLabel")
        self.SignUpLinkLabel.setGeometry(QRect(480, 400, 54, 16))
        self.BackGroundGraphicsView = QGraphicsView(self.centralwidget)
        self.BackGroundGraphicsView.setObjectName(u"BackGroundGraphicsView")
        self.BackGroundGraphicsView.setGeometry(QRect(0, 0, 391, 581))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 886, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.UserNameInputBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.PassWordInputBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.AutoLogInCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.LogInButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
        self.ForgetPassWordTextLabel.setText(QCoreApplication.translate("MainWindow", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.SignUpLinkLabel.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u8d26\u53f7", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(885, 625)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UserNameInputBox = QPlainTextEdit(self.centralwidget)
        self.UserNameInputBox.setObjectName(u"UserNameInputBox")
        self.UserNameInputBox.setGeometry(QRect(480, 230, 301, 31))
        self.PassWordInputBox = QPlainTextEdit(self.centralwidget)
        self.PassWordInputBox.setObjectName(u"PassWordInputBox")
        self.PassWordInputBox.setGeometry(QRect(480, 270, 301, 31))
        self.LogInButton = QPushButton(self.centralwidget)
        self.LogInButton.setObjectName(u"LogInButton")
        self.LogInButton.setGeometry(QRect(480, 350, 301, 24))
        self.BackGroundLabel_2 = QLabel(self.centralwidget)
        self.BackGroundLabel_2.setObjectName(u"BackGroundLabel_2")
        self.BackGroundLabel_2.setGeometry(QRect(0, 0, 391, 581))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackGroundLabel_2.sizePolicy().hasHeightForWidth())
        self.BackGroundLabel_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(16)
        self.BackGroundLabel_2.setFont(font)
        self.BackGroundLabel_2.setLayoutDirection(Qt.LeftToRight)
        self.BackGroundLabel_2.setStyleSheet(u"QLabel{\n"
"border-image: url(:/login/icons/sign.png);\n"
"}")
        self.BackGroundLabel_2.setPixmap(QPixmap(u"resourse/SignUpLogIn.png"))
        self.BackGroundLabel_2.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(480, 320, 301, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.AutoLogInCheckBox = QCheckBox(self.layoutWidget)
        self.AutoLogInCheckBox.setObjectName(u"AutoLogInCheckBox")

        self.horizontalLayout.addWidget(self.AutoLogInCheckBox)

        self.SignUpLinkLabel = QLabel(self.layoutWidget)
        self.SignUpLinkLabel.setObjectName(u"SignUpLinkLabel")
        self.SignUpLinkLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.SignUpLinkLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 885, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u767b\u5165\u754c\u9762", None))
        self.UserNameInputBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.PassWordInputBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.LogInButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
#if QT_CONFIG(tooltip)
        self.BackGroundLabel_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u601d\u7eea\u65e0\u9650</p><p>CSDN\uff1a<a href=\"htps:wuxian.blog.csdn.net\"><span style=\" text-decoration: underline; color:#0000ff;\">wuxian.blog.csdn.net</span></a></p><p>B\u7ad9\uff1a<a href=\"https://space.bilibili.com/456667721\"><span style=\" text-decoration: underline; color:#0000ff;\">\u601d\u7eea\u4ea6\u65e0\u9650</span></a></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BackGroundLabel_2.setText("")
        self.AutoLogInCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4f4f\u7528\u6237\u540d", None))
        self.SignUpLinkLabel.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u8d26\u53f7", None))
    # retranslateUi


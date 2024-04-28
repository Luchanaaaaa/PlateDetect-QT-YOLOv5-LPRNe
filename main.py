import subprocess
import sys

from PySide6.QtGui import QPixmap, QImage, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from LogInPage_UI import Ui_MainWindow as LogInPage_UI
from SignUpPage_UI import Ui_MainWindow as SignUpPage_UI
from OperationDB import checkUserExists, addNewUser, checkLogin, getStoredToken, generateAndStoreToken
from SelectPage_UI import  Ui_MainWindow as SelectPage_UI

class MainWindow(QMainWindow):
    def __init__(self):
        subprocess.run(['python', 'OperationDB.py'], check=True)
        super().__init__()
        self.signUpUi = SignUpPage_UI()
        self.logInUi = LogInPage_UI()
        self.selectUi = SelectPage_UI()
        self.currentUi = self.logInUi
        self.initUi()

    def initUi(self):
        self.currentUi.setupUi(self)
        self.setupConnections()
        username, token = getStoredToken()
        if username and token:
            self.logInUi.UserNameInputBox.setPlainText(username)
            self.logInUi.AutoLogInCheckBox.setChecked(True)


    def setupConnections(self):
        if self.currentUi == self.logInUi:
            self.logInUi.SignUpLinkLabel.mousePressEvent = self.switchToSignIn
            self.logInUi.LogInButton.clicked.connect(self.checkAndLogIn)
        elif self.currentUi == self.signUpUi:
            self.signUpUi.SignUpButton.clicked.connect(self.checkAndRegister)
        elif self.currentUi == self.selectUi:
            self.selectUi.ImageDetectButton.clicked.connect(self.detectImage())
            self.selectUi.VideoDetectButton.clicked.connect(self.detectVideo())
            self.selectUi.RealTimeDetectButton.clicked.connect(self.detectRealTime())

    def detectImage(self):
        pass

    def detectVideo(self):
        pass

    def detectRealTime(self):
        pass

    def checkAndLogIn(self):
        username = self.logInUi.UserNameInputBox.toPlainText()
        password = self.logInUi.PassWordInputBox.toPlainText()

        if (username == '') or (password == ''):
            QMessageBox.warning(self, 'Warning', '用户名或密码不能为空')
            return
        if not checkUserExists(username):
            QMessageBox.warning(self, 'Warning', '用户不存在')
            return
        if not checkLogin(username, password):
            QMessageBox.warning(self, 'Warning', '密码错误')
            return
        if self.logInUi.AutoLogInCheckBox.isChecked():
            generateAndStoreToken(username)
        self.switchToSelect()

    def checkAndRegister(self):
        username = self.signUpUi.UserNameInputBox.toPlainText()
        password = self.signUpUi.PassWordInputBox.toPlainText()
        password_confirm = self.signUpUi.PassWordInputBox_Confirm.toPlainText()

        if password != password_confirm:
            QMessageBox.warning(self, 'Warning', '两次输入的密码不一致')
            return

        if checkUserExists(username):
            QMessageBox.warning(self, 'Warning', '用户名已存在')
            return

        addNewUser(username, password)
        QMessageBox.information(self, 'Info', '注册成功')
        self.switchToLogIn()

    def switchToSignIn(self, event):
        self.currentUi = self.signUpUi
        self.initUi()

    def switchToLogIn(self):
        self.currentUi = self.logInUi
        self.initUi()

    def switchToSelect(self):
        self.currentUi = self.selectUi
        self.initUi()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


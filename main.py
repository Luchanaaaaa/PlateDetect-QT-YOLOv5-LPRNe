import subprocess
import sys
import cv2
import numpy as np
import onnxruntime
import torch
from PySide6.QtGui import QPixmap, QImage, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from LogInPage_UI import Ui_MainWindow as LogInPage_UI
from SignUpPage_UI import Ui_MainWindow as SignUpPage_UI
from OperationDB import checkUserExists, addNewUser, checkLogin, getStoredToken, generateAndStoreToken
from SelectPage_UI import Ui_MainWindow as SelectPage_UI
from RecognitionWindow_UI import Ui_MainWindow as RecognitionWindow_UI
from myDetector import YOLOv5Detector
from utils.plots import colors, plot_one_box


class MainWindow(QMainWindow):
    def __init__(self):
        subprocess.run(['python', 'OperationDB.py'], check=True)
        super().__init__()
        self.signUpUi = SignUpPage_UI()
        self.logInUi = LogInPage_UI()
        self.selectUi = SelectPage_UI()
        self.recogUi = RecognitionWindow_UI()
        self.currentUi = self.logInUi
        ####################################### Model & ML Process #######################################
        self.yolo_detector = YOLOv5Detector(weights='weights/YOLOv5/weight/best.pt', imgsz=640, conf_thres=0.5, iou_thres=0.5, device='cpu')
        ####################################### Model & ML Process #######################################

        self.initUi()

    def initUi(self):
        self.currentUi.setupUi(self)
        self.setupConnections()
        if self.currentUi == self.logInUi:
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
            self.selectUi.ImageDetectButton.clicked.connect(self.detectImage)
            self.selectUi.VideoDetectButton.clicked.connect(self.detectVideo)
            self.selectUi.RealTimeDetectButton.clicked.connect(self.detectRealTime)
        elif self.currentUi == self.recogUi:
            self.recogUi.ImageDetectButton.clicked.connect(self.detectImage)
            self.recogUi.VideoDetectButton.clicked.connect(self.detectVideo)
            self.recogUi.RealTimeDetectButton.clicked.connect(self.detectRealTime)
            pass

    @staticmethod
    def get_key_from_value(d, val):
        for key, value in d.items():
            if value == val:
                return key
        return None

    def process_frame(self, image):
        # 执行推理
        dets = self.yolo_detector.detect(image)
        print("dets = "+str(dets))
        # 绘制检测结果到图像上
        for *xyxy, conf, cls in dets:
            print(f"Class index (cls): {cls}")
            print(f"Names: {self.yolo_detector.names}")
            cls_index = int(cls)
            label_name = MainWindow.get_key_from_value(self.yolo_detector.names, cls_index)
            if label_name is not None:
                label = f'{label_name} {conf:.2f}'
                plot_one_box(xyxy, image, label=label, color=colors(cls_index, True), line_thickness=3)
            else:
                print(f"Class index {cls_index} not found in names dictionary.")
        return image

    def detectImage(self):
        img_path, _ = QFileDialog.getOpenFileName(self, '选择图片', '', '图片文件(*.jpg *.png *.jpeg *.bmp)')
        if img_path:
            if self.currentUi != self.recogUi:
                self.switchToRecog()
            image = cv2.imread(img_path)
            processed_image = self.process_frame(image)

            # 转换颜色空间以适应 QPixmap
            processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            height, width, channel = processed_image.shape
            bytesPerLine = 3 * width
            qImg = QImage(processed_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            ############### Debug PrintOut###
            if qImg.isNull():
                print("Failed to create QImage from image data.")
            if pixmap.isNull():
                print("Failed to create QPixmap from QImage.")
            ################################
            self.recogUi.MainDisplay.setPixmap(
                pixmap.scaled(self.recogUi.MainDisplay.width(), self.recogUi.MainDisplay.height(), Qt.KeepAspectRatio))
            self.recogUi.MainDisplay.show()
            # pixmap = QPixmap(img_path)
            # self.recogUi.MainDisplay.setPixmap(pixmap.scaled(self.recogUi.MainDisplay.width(), self.recogUi.MainDisplay.height(), Qt.KeepAspectRatio))


    def detectVideo(self):
        self.switchToRecog()
        pass

    def detectRealTime(self):
        self.switchToRecog()
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

    def switchToRecog(self):
        self.currentUi = self.recogUi
        self.initUi()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

import os
import subprocess
import sys
import cv2
from PySide6.QtGui import QPixmap, QImage, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from LogInPage_UI import Ui_MainWindow as LogInPage_UI
from SignUpPage_UI import Ui_MainWindow as SignUpPage_UI
from OperationDB import checkUserExists, addNewUser, checkLogin, getStoredToken, generateAndStoreToken
from SelectPage_UI import Ui_MainWindow as SelectPage_UI
from RecognitionWindow_UI import Ui_MainWindow as RecognitionWindow_UI
from myYOLODetector import YOLOv5Detector
from myLPRNeDetector import Recognizer, PLATE_TABLE
from utils.plots import colors, plot_one_box
from PySide6.QtCore import Signal, Slot
import csv
from datetime import datetime




class MainWindow(QMainWindow):

    # 从视频捕获循环中更新 GUI，可能会导致程序崩溃或不稳定, 所以创建一个信号来发送处理过的帧
    frame_processed = Signal(QImage)
    def __init__(self):
        subprocess.run(['python', 'OperationDB.py'], check=True)
        super().__init__()
        self.signUpUi = SignUpPage_UI()
        self.logInUi = LogInPage_UI()
        self.selectUi = SelectPage_UI()
        self.recogUi = RecognitionWindow_UI()
        self.currentUi = self.logInUi
        self.isCaturing = False
        ##########data##########
        self.data = []
        self.isRecording = True
        ####################################### Model & ML Process #######################################
        self.yolo_detector = YOLOv5Detector(weights='weights/YOLOv5/weight/best.pt', imgsz=640, conf_thres=0.5, iou_thres=0.5, device='cpu')
        self.lprnet_detector = Recognizer(
            model_file='weights/LPRnet/best_model_011_0.9393.pth',
            net_type='LPRNet',  # 模型类型
            class_name='',  # 车牌字符表
            use_detector=False,  # 您已经使用 YOLO 进行车牌检测
            input_size=(94, 24),  # 模型输入尺寸
            alignment=True,  # 是否进行车牌矫正
            export=False,  # 已经导出 ONNX，不需要再次导出
            device='cpu'  # 使用 CPU 进行推理
        )
        ######################################################################

        self.initUi()
        self.frame_processed.connect(self.updateMainDisplay)


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
            self.recogUi.SaveResultButton.clicked.connect(self.saveButtonClicked)


    #################### Record Data ####################

    def saveButtonClicked(self):
        if self.recogUi.SaveResultButton.text() == "开始记录数据":
            self.recogUi.SaveResultButton.setText("储存识别结果")
            self.start_recording_data()
        else:
            self.recogUi.SaveResultButton.setText("开始记录数据")
            self.save_data_to_csv()

    def start_recording_data(self):
        # 开始记录数据
        self.recording = True
        self.data = []  # 清空之前的数据

    def record_data(self, filename, bbox, confidence, plate_text):
        # 如果正在记录，将数据添加到列表
        if self.isRecording:
            # 将bbox和confidence转换为标准Python数据类型
            bbox = [int(coord) for coord in bbox]  # 如果bbox是tensor，确保转换为int
            confidence = float(confidence)  # 确保confidence是float
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.data.append((filename, timestamp, *bbox, confidence, plate_text))


    def save_data_to_csv(self):
        # 结束记录数据并保存到CSV
        self.recording = False
        directory = 'results'
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f'recognition_results_{date_str}.csv'  # 设置文件名，加上今天的日期
        path = os.path.join(directory, filename)

        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"目录 {directory} 不存在，已创建。")

        # 检查是否有数据需要保存
        if self.data:
            with open(path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data)
            print("Data saved to CSV on" + str(path))
        else:
            print("No data to save.")
    #####################################################

    ######################### LPRNe： Zoomed Plate Detect & Display #########################
    def show_zoomed_plate_and_recognize(self, image, bbox, filename, confidence):
        x1, y1, x2, y2 = map(int, bbox)
        plate_image = image[y1:y2, x1:x2]

        # 将裁剪的车牌图像转换为 QImage
        plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2RGB)
        height, width, channel = plate_image.shape
        bytesPerLine = 3 * width
        qImg_plate = QImage(plate_image.data, width, height, bytesPerLine, QImage.Format_RGB888)

        # 将 QImage 转换为 QPixmap 并展示在 ZoomDisplay QLabel 中
        pixmap_plate = QPixmap.fromImage(qImg_plate)
        self.recogUi.ZoomDisplay.setPixmap(pixmap_plate.scaled(
            self.recogUi.ZoomDisplay.width(),
            self.recogUi.ZoomDisplay.height(),
            Qt.KeepAspectRatio))
        self.recogUi.ZoomDisplay.show()

        plate_image = image[y1:y2, x1:x2]

        # 使用 LPRNet 进行车牌识别
        recognition_result = self.lprnet_detector.plates_recognize(plate_image)
        recognized_plate = recognition_result['plates'][0] if recognition_result['plates'] else "未识别"

        # 打印识别结果
        print("识别的车牌号码是: ", recognized_plate)


        self.recogUi.label_plate_str.setText(recognized_plate)
        if self.isRecording:
            self.record_data(filename, bbox, confidence, recognized_plate)


    #################################################################################

    ############################## YOLOv5: Detect & Display ###########################
    def stopCapture(self):
        self.isCapturing  = False

    @Slot(QImage)
    def updateMainDisplay(self, qImg):
        # 在 MainDisplay 上显示 QImage
        pixmap = QPixmap.fromImage(qImg)
        self.recogUi.MainDisplay.setPixmap(pixmap.scaled(
            self.recogUi.MainDisplay.width(),
            self.recogUi.MainDisplay.height(),
            Qt.KeepAspectRatio))
        self.recogUi.MainDisplay.show()

    @staticmethod
    def get_key_from_value(d, val):
        for key, value in d.items():
            if value == val:
                return key
        return None
    def process_frame(self, image, filename):
        # 执行推理
        dets = self.yolo_detector.detect(image)
        print("dets = "+str(dets))
        # 绘制检测结果到图像上
        # cls: class index
        for *xyxy, conf, cls in dets:
            print(f"Class index (cls): {cls}")
            print(f"Names: {self.yolo_detector.names}")
            cls_index = int(cls)
            label_name = MainWindow.get_key_from_value(self.yolo_detector.names, cls_index)
            print("label_name = "+str(label_name))
            ###### cut and display the detected plate ######

            if label_name == 'plate':
                self.show_zoomed_plate_and_recognize(image, xyxy, filename,conf)

            if label_name is not None:
                label = f'{label_name} {conf:.2f}'
                plot_one_box(xyxy, image, label=label, color=colors(cls_index, True), line_thickness=3)
            else:
                print(f"Class index {cls_index} not found in names dictionary.")
        return image



    #################################################################################


    ############################## Picture /Video / Webcam Capture & Display ###########################
    def detectVideo(self):
        # Stop previous capture  before starting a new one
        self.stopCapture()
        self.isCapturing = True

        video_path, _ = QFileDialog.getOpenFileName(self, '选择视频', '', '视频文件(*.mp4 *.avi)')
        if video_path:
            if self.currentUi != self.recogUi:
                self.switchToRecog()

            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                QMessageBox.warning(self, 'Warning', '无法打开视频文件')
                return

            while self.isCapturing:
                ret, frame = cap.read()
                if not ret:
                    self.stopCapture()
                    break  # 视频结束或读取错误

                # 处理帧
                processed_frame = self.process_frame(frame, video_path)

                # 转换颜色空间以适应 QPixmap
                processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
                height, width, channel = processed_frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(processed_frame.data, width, height, bytesPerLine, QImage.Format_RGB888)

                # 通过信号发送处理过的 QImage
                self.frame_processed.emit(qImg)

                # 控制视频播放速度
                cv2.waitKey(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

            cap.release()

    def detectRealTime(self):
        # Stop previous capture before starting a new one
        self.stopCapture()
        self.isCapturing = True

        if self.currentUi != self.recogUi:
            self.switchToRecog()
        cap = cv2.VideoCapture(0)  # 打开摄像头
        if not cap.isOpened():
            print("Error: Could not open video device.")
            return

        while self.isCapturing:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from video device.")
                self.stopCapture()
                break

            # 处理帧
            processed_frame = self.process_frame(frame, 'Webcam')

            # 转换颜色空间以适应 QPixmap
            processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            height, width, channel = processed_frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(processed_frame.data, width, height, bytesPerLine, QImage.Format_RGB888)

            # 通过信号发送处理过的 QImage
            self.frame_processed.emit(qImg)

            # 按 'q' 退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stopCapture()
                break

        cap.release()
        cv2.destroyAllWindows()

    def detectImage(self):
        # Stop previous capture
        self.stopCapture()

        img_path, _ = QFileDialog.getOpenFileName(self, '选择图片', '', '图片文件(*.jpg *.png *.jpeg *.bmp)')
        if img_path:
            if self.currentUi != self.recogUi:
                self.switchToRecog()
            image = cv2.imread(img_path)
            processed_image = self.process_frame(image, img_path)

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

    #################### LogIn & SignUp  ####################
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

    ####################################################

    #################### Switch UI ####################
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
    ####################################################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

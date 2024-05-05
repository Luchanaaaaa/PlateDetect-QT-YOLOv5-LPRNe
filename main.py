import os
import subprocess
import sys
import cv2
from PySide6.QtGui import QPixmap, QImage, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTabWidget, QTableWidgetItem
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

    # To update the GUI from the video capture loop, which may cause crashes or instability, create a signal to send the processed frame
    frame_processed = Signal(QImage)
    update_table_signal = Signal(tuple)

    def __init__(self):
        subprocess.run(['python', 'OperationDB.py'], check=True)
        super().__init__()
        self.update_table_signal.connect(self.add_row_to_table)
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
            net_type='LPRNet',  # Model type
            class_name='',  #  License plate character table
            use_detector=False,
            input_size=(94, 24),  # Model input size
            alignment=True,  #  Whether to align the license plate
            export=False,
            device='cpu'  #  Use CPU for inference
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
            self.recogUi.SignOutButton.clicked.connect(self.switchToLogIn)
    ############Update Table##########
    def add_row_to_table(self, data):
        filename, timestamp, bbox, confidence, plate_text = data
        row_count = self.recogUi.DataTable.rowCount()
        self.recogUi.DataTable.insertRow(row_count)
        self.recogUi.DataTable.setItem(row_count, 0, QTableWidgetItem(filename))
        self.recogUi.DataTable.setItem(row_count, 1, QTableWidgetItem(timestamp))
        self.recogUi.DataTable.setItem(row_count, 2, QTableWidgetItem(str(bbox)))  # 转换bbox为字符串
        self.recogUi.DataTable.setItem(row_count, 3, QTableWidgetItem(str(confidence)))
        self.recogUi.DataTable.setItem(row_count, 4, QTableWidgetItem(plate_text))
        # Automatically scroll to the newest row
        self.recogUi.DataTable.scrollToBottom()
    #################################
    def saveButtonClicked(self):
        if self.recogUi.SaveResultButton.text() == "Start Recording Data":
            self.recogUi.SaveResultButton.setText("Save Recognition Results")
            self.start_recording_data()
        else:
            self.recogUi.SaveResultButton.setText("Start Recording Data")
            self.save_data_to_csv()

    def start_recording_data(self):
        # Start recording data
        self.recording = True
        self.data = []  # Clear previous data

    def record_data(self, filename, bbox, confidence, plate_text):
        #  If recording, add data to the list
        if self.isRecording:
            # Convert bbox and confidence to standard Python data types
            bbox = [int(coord) for coord in bbox]  # If bbox is a tensor, ensure it is converted to int
            confidence = float(confidence)  # Ensure confidence is float
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.data.append((filename, timestamp, *bbox, confidence, plate_text))
            self.update_table_signal.emit((filename, timestamp, bbox, confidence, plate_text))


    def save_data_to_csv(self):
        # End data recording and save to CSV
        self.recording = False
        directory = 'results'
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f'recognition_results_{date_str}.csv'  # Set filename, including today's date
        path = os.path.join(directory, filename)

        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"目录 {directory} 不存在，已创建。")

        #  Check if there is data to save
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

        # Convert the cropped license plate image to QImage
        plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2RGB)
        height, width, channel = plate_image.shape
        bytesPerLine = 3 * width
        qImg_plate = QImage(plate_image.data, width, height, bytesPerLine, QImage.Format_RGB888)

        # Convert QImage to QPixmap and display in ZoomDisplay QLabel
        pixmap_plate = QPixmap.fromImage(qImg_plate)
        self.recogUi.ZoomDisplay.setPixmap(pixmap_plate.scaled(
            self.recogUi.ZoomDisplay.width(),
            self.recogUi.ZoomDisplay.height(),
            Qt.KeepAspectRatio))
        self.recogUi.ZoomDisplay.show()

        plate_image = image[y1:y2, x1:x2]

        # Use LPRNet for license plate recognition
        recognition_result = self.lprnet_detector.plates_recognize(plate_image)
        recognized_plate = recognition_result['plates'][0] if recognition_result['plates'] else "未识别"

        # Print recognition result
        print("Recognized license plate number is: ", recognized_plate)


        self.recogUi.label_plate_str.setText(recognized_plate)
        if self.isRecording:
            self.record_data(filename, bbox, confidence, recognized_plate)


    #################################################################################

    ############################## YOLOv5: Detect & Display ###########################
    def stopCapture(self):
        self.isCapturing  = False

    @Slot(QImage)
    def updateMainDisplay(self, qImg):
        # Display QImage on MainDisplay
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
        # Perform inference
        dets = self.yolo_detector.detect(image)
        print("dets = "+str(dets))
        # Draw detection results on the image
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

        video_path, _ = QFileDialog.getOpenFileName(self, 'Select Video', '', 'Video files(*.mp4 *.avi)')
        if video_path:
            if self.currentUi != self.recogUi:
                self.switchToRecog()
            self.recogUi.DataTable.setRowCount(0)
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                QMessageBox.warning(self, 'Warning', 'Cannot open video file')
                return

            while self.isCapturing:
                ret, frame = cap.read()
                if not ret:
                    self.stopCapture()
                    break  # Video ended or read error

                # Process frame
                processed_frame = self.process_frame(frame, video_path)

                # Convert color space to fit QPixmap
                processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
                height, width, channel = processed_frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(processed_frame.data, width, height, bytesPerLine, QImage.Format_RGB888)

                #  Send processed QImage through signal
                self.frame_processed.emit(qImg)

                # Control video playback speed
                cv2.waitKey(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

            cap.release()

    def detectRealTime(self):
        # Stop previous capture before starting a new one
        self.stopCapture()
        self.isCapturing = True

        if self.currentUi != self.recogUi:
            self.switchToRecog()
        self.recogUi.DataTable.setRowCount(0)

        cap = cv2.VideoCapture(0)  # Open camera
        if not cap.isOpened():
            print("Error: Could not open video device.")
            return

        while self.isCapturing:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from video device.")
                self.stopCapture()
                break

            # Process frame
            processed_frame = self.process_frame(frame, 'Webcam')

            # Convert color space to fit QPixmap
            processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            height, width, channel = processed_frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(processed_frame.data, width, height, bytesPerLine, QImage.Format_RGB888)

            # Send processed QImage through signal
            self.frame_processed.emit(qImg)

            # Press 'q' to exit loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stopCapture()
                break

        cap.release()
        cv2.destroyAllWindows()

    def detectImage(self):
        # Stop previous capture
        self.stopCapture()

        img_path, _ = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image files(*.jpg *.png *.jpeg *.bmp)')
        if img_path:
            if self.currentUi != self.recogUi:
                self.switchToRecog()
            self.recogUi.DataTable.setRowCount(0)

            image = cv2.imread(img_path)
            processed_image = self.process_frame(image, img_path)

            # Convert color space to fit QPixmap
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
            QMessageBox.warning(self, 'Warning', 'Username or password cannot be empty')
            return
        if not checkUserExists(username):
            QMessageBox.warning(self, 'Warning', 'User does not exist')
            return
        if not checkLogin(username, password):
            QMessageBox.warning(self, 'Warning', 'Incorrect password')
            return
        if self.logInUi.AutoLogInCheckBox.isChecked():
            generateAndStoreToken(username)
        self.switchToSelect()

    def checkAndRegister(self):
        username = self.signUpUi.UserNameInputBox.toPlainText()
        password = self.signUpUi.PassWordInputBox.toPlainText()
        password_confirm = self.signUpUi.PassWordInputBox_Confirm.toPlainText()

        if password != password_confirm:
            QMessageBox.warning(self, 'Warning', 'Passwords do not match')
            return

        if checkUserExists(username):
            QMessageBox.warning(self, 'Warning', 'Username already exists')
            return

        addNewUser(username, password)
        QMessageBox.information(self, 'Info', 'Registration successful')
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

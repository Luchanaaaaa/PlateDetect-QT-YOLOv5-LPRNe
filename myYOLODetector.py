# ... 其他导入 ...
import cv2
import numpy as np
import torch
from PySide6.QtGui import QImage, QPixmap, Qt
from PySide6.QtWidgets import QFileDialog

from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords
from utils.plots import plot_one_box, colors
from utils.torch_utils import select_device
from utils.datasets import letterbox

class YOLOv5Detector:
    def __init__(self, weights, imgsz, conf_thres, iou_thres, device):
        self.device = select_device(device)
        self.model = attempt_load(weights, map_location=self.device)
        self.imgsz = imgsz
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.stride = int(self.model.stride.max())
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        print("self.names=" + str(self.names))

    def preprocess(self, img):
        img = letterbox(img, new_shape=self.imgsz, stride=self.stride)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.float()
        img /= 255.0  # scale (0, 255) to (0, 1)
        img = img.unsqueeze(0)
        return img

    def postprocess(self, pred):
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres)[0]
        pred[:, :4] = scale_coords(self.img.shape[2:], pred[:, :4], self.im0s.shape).round()
        return pred

    def detect(self, img):
        self.im0s = img.copy()
        img = self.preprocess(img)
        self.img = img
        pred = self.model(img, augment=False)[0]
        det = self.postprocess(pred)
        return det

# ... MainWindow 类 ...

    def detectImage(self):
        img_path, _ = QFileDialog.getOpenFileName(self, '选择图片', '', '图片文件(*.jpg *.png *.jpeg *.bmp)')
        if img_path:
            if self.currentUi != self.recogUi:
                self.switchToRecog()

            # 读取图像
            image = cv2.imread(img_path)
            # 执行推理
            dets = self.yolo_detector.detect(image)
            # 绘制检测结果到图像上
            for *xyxy, conf, cls in dets:
                label = f'{self.yolo_detector.names[int(cls)]} {conf:.2f}'
                plot_one_box(xyxy, image, label=label, color=colors(int(cls), True), line_thickness=3)

            # 转换颜色空间以适应 QPixmap
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.recogUi.MainDisplay.setPixmap(
                pixmap.scaled(self.recogUi.MainDisplay.width(), self.recogUi.MainDisplay.height(), Qt.KeepAspectRatio))

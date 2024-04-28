# -*- coding: utf-8 -*-
import cv2  # 导入OpenCV库，用于处理图像和视频
import numpy as np
import torch
from QtFusion.models import Detector, HeatmapGenerator  # 从QtFusion库中导入Detector抽象基类
from QtFusion.path import abs_path
from QtFusion.utils import cv_imread

from LPRNet import LPRNet, CHARS
from PlateColorModel import detect_dominant_color
from datasets.VehicleLicense.label_name import Chinese_name  # 从datasets库中导入Chinese_name字典，用于获取类别的中文名称
from ultralytics import YOLO  # 从ultralytics库中导入YOLO类，用于加载YOLO模型
from ultralytics.utils.torch_utils import select_device  # 从ultralytics库中导入select_device函数，用于选择设备

device = "cuda:0" if torch.cuda.is_available() else "cpu"

ini_params = {
    'device': device,  # 设备类型，这里设置为CPU
    'conf': 0.25,  # 物体置信度阈值
    'iou': 0.5,  # 用于非极大值抑制的IOU阈值
    'classes': None,  # 类别过滤器，这里设置为None表示不过滤任何类别
    'verbose': False
}


def count_classes(det_info, class_names):
    count_dict = {name: 0 for name in class_names}  # 创建一个字典，用于存储每个类别的数量
    for info in det_info:  # 遍历检测信息
        class_name = info['class_name']  # 获取类别名称
        if class_name in count_dict:  # 如果类别名称在字典中
            count_dict[class_name] += 1  # 将该类别的数量加1

    # Convert the dictionary to a list in the same order as class_names
    count_list = [count_dict[name] for name in class_names]  # 将字典转换为列表，列表的顺序与class_names相同
    return count_list  # 返回列表


def transform(img):
    img = img.astype('float32')
    img -= 127.5
    img *= 0.0078125
    img = np.transpose(img, (2, 0, 1))

    return img


class YOLOv8v5PlateDetector(Detector):  # 定义YOLOv8Detector类，继承自Detector类
    def __init__(self, params=None):  # 定义构造函数
        super().__init__(params)  # 调用父类的构造函数
        self.model = None
        self.lpr_model = None
        self.img = None  # 初始化图像为None
        self.names = list(Chinese_name.values())  # 获取所有类别的中文名称
        self.params = params if params else ini_params  # 如果提供了参数则使用提供的参数，否则使用默认参数

    def load_model(self, *model_paths):  # 定义加载模型的方法
        if len(model_paths) != 2:
            raise ValueError("Two model paths required: one for YOLO and one for LPRNet.")
        yolo_model_path, lpr_model_path = model_paths  # 解析出YOLO和LPRNet模型的路径

        self.device = select_device(self.params['device'])  # 选择设备
        self.model = YOLO(yolo_model_path, )
        self.lpr_model = LPRNet(lpr_max_len=8, phase=False, class_num=len(CHARS), dropout_rate=0).to(self.device)  # 初始化LPRNet模型
        self.lpr_model.load_state_dict(torch.load(lpr_model_path, map_location=self.device))  # 加载LPRNet模型权重
        self.lpr_model.eval()  # 设置LPRNet模型为评估模式

        # 获取类别名称字典并将其转换为中文（如果适用）
        names_dict = self.model.names
        self.names = [Chinese_name[v] if v in Chinese_name else v for v in names_dict.values()]

        self.model(torch.zeros(1, 3, *[self.imgsz] * 2).to(self.device).
                   type_as(next(self.model.model.parameters())))  # 预热
        self.model(torch.rand(1, 3, *[self.imgsz] * 2).to(self.device).
                   type_as(next(self.model.model.parameters())))  # 预热
        # LPRNet模型预热
        self.lpr_model(torch.zeros(1, 3, 24, 94).to(self.device).type_as(next(self.lpr_model.parameters())))

    def preprocess(self, img):  # 定义预处理方法
        self.img = img  # 保存原始图像
        return img  # 返回处理后的图像

    def predict(self, img):  # 定义预测方法
        results = self.model(img, **ini_params)
        return results

    def postprocess(self, pred):
        results = []  # 初始化结果列表
        for res in pred[0].boxes:
            for box in res:
                class_id = int(box.cls.cpu())
                bbox = box.xyxy.cpu().squeeze().tolist()
                bbox = [int(coord) for coord in bbox]  # 转换边界框坐标为整数

                if self.names[class_id] == '车牌':  # 假设车牌类别名称为'车牌'
                    cutout = self.img[bbox[1]:bbox[3], bbox[0]:bbox[2]]  # 从原图中切割出车牌区域
                    im = cv2.resize(cutout, (94, 24))  # 调整车牌图像大小以符合LPRNet输入
                    plate_color = detect_dominant_color(im)  # 检测主体颜色
                    im = transform(im)  # 对车牌图像进行必要的预处理

                    im_array = np.array([im])  # 首先将列表转换为numpy数组
                    preds = self.lpr_model(torch.from_numpy(im_array).float().to(self.device))  # 使用LPRNet进行车牌字符识别

                    # 解码LPRNet输出为车牌字符
                    prebs = preds.cpu().detach().numpy()
                    preb_labels = []
                    for w in range(prebs.shape[0]):
                        preb = prebs[w, :, :]
                        preb_label = [np.argmax(preb[:, j], axis=0) for j in range(preb.shape[1])]

                        # 去除重复和空白字符
                        no_repeat_blank_label = []
                        pre_c = preb_label[0]
                        if pre_c != len(CHARS) - 1:
                            no_repeat_blank_label.append(pre_c)
                        for c in preb_label:
                            if (pre_c == c) or (c == len(CHARS) - 1):
                                if c == len(CHARS) - 1:
                                    pre_c = c
                                continue
                            no_repeat_blank_label.append(c)
                            pre_c = c
                        preb_labels.append(no_repeat_blank_label)

                    # 转换车牌字符索引为实际字符
                    plat_num = ''.join([CHARS[label] for label in preb_labels[0]])

                    result = {
                        "class_name": self.names[class_id],  # 类别名称
                        "bbox": bbox,  # 边界框
                        "score": box.conf.cpu().squeeze().item(),  # 置信度
                        "class_id": class_id,  # 类别ID
                        "plate_number": plat_num,  # 识别的车牌号
                        "plate_color": plate_color
                    }
                else:
                    result = {
                        "class_name": self.names[class_id],
                        "bbox": bbox,
                        "score": box.conf.cpu().squeeze().item(),
                        "class_id": class_id,
                        "plate_number": "",  # 识别的车牌号
                        "plate_color": ""
                    }

                results.append(result)  # 将结果添加到列表

        return results  # 返回结果列表

    def set_param(self, params):
        self.params.update(params)


if __name__ == "__main__":
    # 初始化检测器
    detector = YOLOv8v5PlateDetector()

    # 加载模型，这里需要替换成你的模型文件路径
    yolo_model_path = abs_path('weights/best-yolov8n.pt')
    lpr_model_path = abs_path('weights/Final_LPRNet_model.pth')
    detector.load_model(yolo_model_path, lpr_model_path)

    # 加载要测试的图像
    image_path = 'test_media/冀BAY665.jpg'
    img = cv_imread(image_path)

    # 预处理图像
    processed_img = detector.preprocess(img)

    # 进行预测
    results = detector.predict(processed_img)

    # 后处理结果，获取检测到的车牌和识别结果
    processed_results = detector.postprocess(results)

    # 打印结果
    for result in processed_results:
        if 'plate_number' in result:
            print(f"检测到车牌: {result['plate_number']}, 颜色: {result['plate_color']}，位置: {result['bbox']}")
        else:
            print(f"检测到 {result['class_name']}，位置: {result['bbox']}")


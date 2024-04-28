import cv2
import numpy as np
from QtFusion.path import abs_path


def detect_dominant_color(img):
    # 将BGR图像转换为HSV颜色空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 定义颜色范围
    color_ranges = {
        '黑色': ((0, 0, 0), (180, 255, 30)),
        '蓝色': ((100, 150, 0), (140, 255, 255)),
        '绿色': ((40, 70, 50), (80, 255, 255)),
        '白色': ((0, 0, 231), (180, 18, 255)),
        '黄色': ((25, 70, 120), (35, 255, 255))
    }

    # 初始化颜色占比字典
    color_ratios = {}

    # 为每种颜色应用阈值并计算占比
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # 生成颜色掩码
        mask = cv2.inRange(hsv, lower, upper)

        # 计算掩码中的白色像素占比
        ratio = cv2.countNonZero(mask) / (img.size / 3)
        color_ratios[color] = ratio

    # 确定占比最高的颜色
    dominant_color = max(color_ratios, key=color_ratios.get)

    return dominant_color


# 使用示例
if __name__ == "__main__":
    img_path = abs_path("test_media/color-test2.png")  # 替换为您的图片路径
    img = cv2.imread(img_path)  # 读取图像
    dominant_color = detect_dominant_color(img)  # 检测主体颜色
    print(f"Dominant Color: {dominant_color}")  # 打印主体颜色

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
import os
class StyleSetter:
    @staticmethod
    def setBackgroundImage(view, image_path):
        scene = QGraphicsScene()

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Failed to load image from {image_path}")
            return
            print(os.path.exists(image_path))

        pixmap_item = QGraphicsPixmapItem(pixmap)

        scene.addItem(pixmap_item)

        view.setScene(scene)
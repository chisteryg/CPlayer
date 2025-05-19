from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt


class EventFilterDemo(QLabel):
    def __init__(self):
        super().__init__("自由移动鼠标试试")
        self.setMouseTracking(True)  # 仍然需要启用跟踪

        self.press_flag = False
        # 进入边界的标志
        self.cursor_shape_flag = False
        self.resize_flag = False

    def mousePressEvent(self, event):
        # 设置按压状态
        self.press_flag = True
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # 恢复按压状态和调整大小标准
        self.press_flag = False
        self.resize_flag = False
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        # print(event.pos())

        width = self.width()
        height = self.height()
        if event.x() > width - 10 and event.x() < width + 10 and event.y() > height - 10 and event.y() < height + 10:
            # print('进入边界')
            if not self.cursor_shape_flag:
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)
                self.cursor_shape_flag = True

            if self.cursor_shape_flag and self.press_flag:
                # 图标形状改变，并且按压，设置调整大小标志
                self.resize_flag = True
        else:
            # 移出边界，恢复鼠标形状
            if self.cursor_shape_flag:
                self.unsetCursor()
                self.cursor_shape_flag = False

        if self.resize_flag:
            geo = self.geometry()
            x = geo.x()
            y = geo.y()
            width = event.x()
            height = event.y()
            self.setGeometry(x, y, width, height)

        return super().mouseMoveEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    window = EventFilterDemo()
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    window.resize(400, 400)
    window.setMinimumSize(QtCore.QSize(300, 300))
    window.show()
    app.exec()

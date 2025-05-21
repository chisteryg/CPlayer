import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication

from PySide_UI.ui.tools.sub_ui.mini_page import Ui_mini_page


class MiniPage(QWidget, Ui_mini_page):

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 取消注释，启用透明背景
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # 置顶
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 保留无边框设置
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, False)

        self.setupUi(self)
        self.show()

        self.pos_x = -1
        self.pos_y = -1

    def mousePressEvent(self, event):
        # 记录点击时xy位置
        self.pos_x = event.x()
        self.pos_y = event.y()
        return super().mousePressEvent(event)


    def mouseMoveEvent(self, event):
        # 移动，原本xy + 移动的距离
        if self.pos_x != -1 and self.pos_y != -1:
            x = self.geometry().x() + event.x() - self.pos_x
            y = self.geometry().y() + event.y() - self.pos_y
            self.move(x, y)
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        # 鼠标松开时重置xy
        self.pos_x = -1
        self.pos_y = -1
        return super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MiniPage()
    sys.exit(app.exec())
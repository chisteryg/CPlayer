from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication


class MoveWidget(QWidget):
    # 移动widget，当该控件被点击时，如果存在父控件，则移动父控件
    def __init__(self, *args, **kwargs):
        super(MoveWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.pos_x = -1
        self.pos_y = -1
        self.parent_geometry = None
        self._press = False
        self.show()

    def mousePressEvent(self, event):
        # 记录点击时xy位置
        self.pos_x = event.x()
        self.pos_y = event.y()
        self._press = True
        return super().mousePressEvent(event)
    
    def moveEvent(self, event):
        return super().moveEvent(event)

    def mouseMoveEvent(self, event):
        
        # 按压状态下最大化窗口脱离顶端时，恢复原窗口大小
        if self.parent() is not None and self._press and event.globalY() != 0 and self.parent().isMaximized():
            if self.parent_geometry is not None:
                width = self.parent_geometry.width()
                height = self.parent_geometry.height()
                x = event.globalX() - width / 2
                y = event.globalY()
                # print(x, y)
                self.parent().move(x, y)
                self.parent().resize(width, height)
                # self.parent().setGeometry(x, y, width, height)

        # 移动，原本xy + 移动的距离
        if self.parent() != None and self.pos_x != -1 and self.pos_y != -1 and self._press:
            x = self.parent().geometry().x() + event.x() - self.pos_x
            y = self.parent().geometry().y() + event.y() - self.pos_y
            self.parent().move(x, y)
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        # 判断鼠标松开时是否在顶端，如果在顶端则最大化父窗口
        if self.parent() != None and event.globalY() == 0:
            # 记录窗口大小
            self.parent_geometry = self.parent().geometry()
            self.parent().showMaximized()

        # 鼠标松开时重置xy
        self.pos_x = -1
        self.pos_y = -1
        return super().mouseReleaseEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    window.resize(800, 600)
    window2 = MoveWidget(window)
    window2.setStyleSheet('background-color: rgb(255, 255, 255);')
    window2.resize(1800, 40)
    window.show()
    app.exec()
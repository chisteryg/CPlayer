import math

from PySide6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import QIcon, QFontMetrics, QResizeEvent, QMouseEvent, QHoverEvent
from PySide6.QtCore import Qt, QSize, QEvent, Signal


class IdButton(QPushButton):
    leftclick = Signal(dict)

    # 图标跟随操作变大缩小
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setProperty('list_id', None)
        self.setProperty('music_id', None)


    def mouseReleaseEvent(self, a0):
        # 鼠标左击时发射信号，携带音乐id
        if a0.button() == Qt.LeftButton:
            id_info = {
                'list_id': self.property('list_id'),
                'music_id': self.property('music_id'),
                'self': self
            }
            self.leftclick.emit(id_info)
        super().mouseReleaseEvent(a0)

# 示例使用
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(800, 600)


    button = IdButton(window, QIcon('../1.jpg'))
    button.resize(100, 100)


    window.show()

    sys.exit(app.exec())
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import *
import sys

class IdLabel(QLabel):
    leftclick = Signal(dict)
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.setProperty('list_id', None)
        self.setProperty('music_id', None)

    def mouseReleaseEvent(self, a0):
        if a0.button() == Qt.LeftButton:
            id_info = {
                'list_id': self.property('list_id'),
                'music_id': self.property('music_id'),
                'self': self
            }
            self.leftclick.emit(id_info)

        super().mouseReleaseEvent(a0)

    def setText(self, text: str):
        self.setToolTip(text)
        self.setToolTipDuration(6000)  # 6 秒
        # if len(text) > 12:
        #     text = text[:12] + '...'
        return super().setText(text)


class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.create_ui()
        self.setWindowTitle('方法学习')
        self.resize(1000, 800)
        self.show()

    def create_ui(self):
        # 创建
        self.c()

        pass

    # 创建
    def c(self):
        label1 = ListLab(self)
        label1.resize(200, 40)
        label1.move(50, 50)
        label1.setStyleSheet("background-color: rgb(255, 255, 255);")
        label1.setWordWrap(True)
        label1.setText('哇真的是你呀哈哈哈哎呀哇真的是你呀哈哈哈哎呀')
        label1.leftclick.connect(lambda: print('左击标签'))
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec_())
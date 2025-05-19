import sys

from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QWidget, QDialog, QApplication

from PySide_UI.ui.tools.sub_ui.msg import Ui_msg
from PySide_UI.ui.tools.base.movewidget import MoveWidget


class MessagePage(QDialog, Ui_msg):
    def __init__(self, title: str = '', msg: str = ''):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setupUi(self)

        # 设置标题以及信息
        self.setWindowTitle(title)
        self.title_lab.setText(title)
        self.msg_lab.setText(msg)
        # 设置模态
        self.setModal(True)
        self.show()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(800, 600)
        self.window2 = MessagePage('123', 'djioicic')
        self.window2.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()

    window.show()
    sys.exit(app.exec_())

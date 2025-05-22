import sys

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QApplication

from PySide_UI.ui.tools.sub_ui.mini_page import Ui_mini_page


class MiniPage(QWidget, Ui_mini_page):
    mini_page_close = Signal()
    play = Signal()
    play_at = Signal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 取消注释，启用透明背景
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, False)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)  # 保留无边框设置，置顶

        self.setWindowTitle('CPlayer-Mini-Page')
        self.show()

        self.pos_x = -1
        self.pos_y = -1



    @Slot()
    def on_music_time_slider_sliderReleased(self):
        # 滑块按钮按下，设置滑块至不在实时更新
        val = self.music_time_slider.value()
        self.play_at.emit(val)
        return

    @Slot()
    def on_play_btn_clicked(self):
        self.play.emit()
        return

    def set_mini_page_time_maximum(self, maximum: int = 100):
        # 设置滑动条最大值
        self.music_time_slider.setMaximum(maximum)
        return

    def set_mini_page_time_value(self, value: int = 100):
        # 设置滑动条当前值
        self.music_time_slider.setValue(value)
        return

    def set_mini_page_time(self, time: str = ''):
        # 设置当前时间
        self.now_time_lab.setText(time)
        return

    def set_mini_page_lrc(self, lrc: str = ''):
        # 设置当前歌词
        self.lrc_lab.setText(lrc)
        return

    def set_mini_page_play_icon(self, qss: str = ''):
        # 设置图标
        self.play_btn.setStyleSheet(qss)
        return

    def close(self):
        self.mini_page_close.emit()
        super().close()
        return


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
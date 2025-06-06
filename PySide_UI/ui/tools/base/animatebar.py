from PySide6.QtCore import Qt, QPropertyAnimation, QByteArray, QEasingCurve
from PySide6.QtWidgets import QProgressBar


class AnimatedBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._current_value = 0
        self.setOrientation(Qt.Orientation.Vertical)
        self.setMaximum(100)

        # 上升动画配置（快速到达峰值）
        self.rise_anim = QPropertyAnimation(self, QByteArray(b"value"))
        self.rise_anim.setDuration(400)  # 更快的上升速度
        self.rise_anim.setEasingCurve(QEasingCurve.Type.OutBack)

        # 缓降动画配置（自动归零）
        self.fall_anim = QPropertyAnimation(self, QByteArray(b"value"))
        self.fall_anim.setDuration(800)  # 更长的缓降时间
        self.fall_anim.setEasingCurve(QEasingCurve.Type.InOutSine)  # 平滑正弦曲线

        # 连接信号
        self.rise_anim.finished.connect(self._start_fall_anim)

    def _start_fall_anim(self):
        """上升结束后自动启动缓降"""
        current_value = self.value()
        self.fall_anim.stop()
        self.fall_anim.setStartValue(current_value)
        self.fall_anim.setEndValue(0)  # 最终归零
        self.fall_anim.start()

    def setValue(self, value):
        """值更新入口"""
        value = max(0, min(200, int(value)))
        # if value < self.value():
        #     return


        self._current_value = value

        # 停止当前动画
        self.rise_anim.stop()
        self.fall_anim.stop()

        # 启动新动画
        self.rise_anim.setStartValue(self.value())
        self.rise_anim.setEndValue(value)
        self.rise_anim.start()
from PySide6.QtWidgets import QSlider


class MusicTimeSlider(QSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # # 启用鼠标跟踪以实时检测拖拽
        # self.setTracking(True)

    def setValue(self, value: int) -> None:
        """重写 setValue，仅在用户未拖拽时更新值"""
        if not self.isSliderDown():  # 检查滑块是否被按下
            super().setValue(value)
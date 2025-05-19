import sys
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaDevices

class MusicPlayer(QMediaPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_volume = 0.7
        self._is_playing = False
        self._pending_play = False  # 新增：标记待处理的播放状态
        self.device = QMediaDevices()

        # 初始化音频设备（显式传递设备参数）
        self.device_description = None
        self.audio_output = None
        self.init_audio_output()

        # 监听设备变化（延迟处理）
        self.device.audioOutputsChanged.connect(
            lambda: QTimer.singleShot(300, self.handle_audio_device_changed)
        )

        self.errorOccurred.connect(self.handle_error)  # 连接错误信号
        # 其他初始化代码...

    def handle_error(self, error, error_string):
        print(f"播放错误: {error}, 详细信息: {error_string}")

    def init_audio_output(self):
        # 显式创建新设备（关键修正点）
        device = QMediaDevices.defaultAudioOutput()
        if self.device_description == device.description():
            # 原设备与现设备相同，不替换
            return
        else:
            self.device_description = device.description()

        print(device)

        # 强制释放旧设备
        if self.audio_output:
            # self.audio_output.stop()
            self.setAudioOutput(None)
            self.audio_output.setParent(None)
            self.audio_output.deleteLater()
            self.audio_output = None



        self.audio_output = QAudioOutput(device)  # 必须传入设备对象
        self.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(self.current_volume)

        # 延迟恢复播放状态
        if self._pending_play or self._is_playing:
            QTimer.singleShot(200, self.play)

    def handle_audio_device_changed(self):
        print("检测到音频设备变化，重新初始化输出...")
        self._pending_play = self._is_playing  # 记录播放状态
        self.init_audio_output()

    def play(self):
        super().play()
        self._is_playing = True
        self._pending_play = False  # 重置标记

    def playAt(self, position: int):
        # 在指定位置播放
        self.setPosition(position)
        self.play()

    def pause(self):
        super().pause()
        self._is_playing = False

    # 其他方法保持不变...

    def setMusic(self, music_url):
        url = QUrl.fromLocalFile(music_url)
        self.setSource(url)

    def setVolume(self, volume: float):
        self.current_volume = volume
        if self.audio_output:
            self.audio_output.setVolume(volume)


    def stop(self):
        super().stop()
        self._is_playing = False


if __name__ == "__main__":
    # 创建应用实例
    app = QApplication(sys.argv)
    # 替换为你的音频文件路径
    music_file = "./1.flac"
    # music_file = "../PySide_UI/ui/music/30482460.mp3"
    p = MusicPlayer()
    p.setMusic(music_file)
    p.play()

    w = QWidget()
    w.resize(400, 400)

    btn = QPushButton(w)
    btn.setText('30s')
    # btn.clicked.connect(lambda: p.setPosition(30000))
    # btn.clicked.connect(lambda: p.play())
    btn.clicked.connect(lambda: p.playAt(40000))
    btn.move(100, 100)

    w.show()
    # 保持应用运行
    sys.exit(app.exec())

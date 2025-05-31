import sys
import time
from pprint import pprint

import librosa
import numpy as np
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

    def setMusic(self, music_url):
        url = QUrl.fromLocalFile(music_url)
        try:
            self.setSource(url)
            # 加载音频文件
            self.y, self.sr = librosa.load(music_url, sr=None, mono=True)  # sr=None保留原始采样率
            # STFT参数设置
            n_fft = 2048
            hop_length = 512
            window = 'hann'

            # 执行STFT (短时傅里叶变换)
            self.stft = librosa.stft(self.y, n_fft=n_fft, hop_length=hop_length)


            music_url = '已加载：' + music_url
        except Exception as e:
            music_url = '加载失败'
            print(e)

        return music_url

    def analyze_audio(self, target_time_ms: int, target_freqs: list[int] = []):
        """
        分析音频文件中指定时刻的多个频率成分
        :param audio_path: MP3文件路径
        :param target_time_ms: 目标时间（毫秒）
        :param target_freqs: 目标频率列表（Hz）
        :return: 结果字典 {'频率': {'振幅': xxx, '分贝': xxx}}
        """

        # 目标振幅
        target_freqs = [
            # 20Hz-40Hz称为极低频
            20, 30, 40,
            # 40Hz-80Hz称为低频
            50, 60, 70, 80,
            # 80Hz-160Hz称为中低频
            100, 120, 140, 160,
            # 160Hz-1280Hz称为中频
            200, 400, 600, 800, 1000, 1200,
            # 1280Hz-3560Hz称为中高频
            1280, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3560,
            # # 2560Hz-5120Hz称为高频
            # 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5120,
            # # 5120Hz-20000Hz称为极高频
            # 6000, 8000, 12000, 14000, 16000, 20000,
        ]

        # STFT参数设置
        n_fft = 2048
        hop_length = 512

        # 计算目标时间点对应的采样点索引
        target_sample = int((target_time_ms / 1000) * self.sr)

        # 计算目标时间对应的帧索引
        frame_index = int(target_sample / hop_length)

        # 获取目标帧的频谱
        frame_spectrum = self.stft[:, frame_index]

        # 计算频率分辨率
        freq_resolution = self.sr / n_fft

        # 准备结果字典
        result = {}

        for freq in target_freqs:
            # 计算频率对应的bin索引
            bin_index = int(round(freq / freq_resolution))

            # 确保索引在有效范围内
            if bin_index >= len(frame_spectrum):
                bin_index = len(frame_spectrum) - 1

            # 获取复数频谱值
            complex_value = frame_spectrum[bin_index]

            # 计算振幅 (复数的模)
            amplitude = np.abs(complex_value)

            # 计算分贝值 (避免log(0)错误)
            db = 20 * np.log10(amplitude + 1e-10)  # 加上极小值防止0振幅

            result[freq] = {
                'amplitude': float(amplitude),
                'db': float(db)
            }
            # result[freq] = float(db)

        return result

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
    music_file = "mp3/雷雨季节-柯柯柯啊.mp3"
    # music_file = "../PySide_UI/ui/music/30482460.mp3"
    p = MusicPlayer()
    p.setMusic(music_file)
    p.play()
    du = 0

    def ts():
        global du
        du += 200
        s = time.time()
        hr = p.analyze_audio(du)
        e = time.time()
        print(f'耗时：{e-s}', hr)


    t = QTimer()
    t.setInterval(200)
    t.timeout.connect(ts)
    t.start()

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

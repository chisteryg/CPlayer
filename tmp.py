# main.py
import sys
import wave
import numpy as np
import pyaudio
from PySide6.QtCore import Qt, QThread, Signal, QMutex
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog


class AudioVisualizer(QWidget):
    def __init__(self, bar_count=50):
        super().__init__()
        self.bar_count = bar_count
        self.amplitudes = [0] * bar_count
        self.setMinimumSize(800, 300)
        self.mutex = QMutex()
        self.bar_color = QColor(0, 255, 0)  # 初始绿色

    def update_amplitudes(self, new_amplitudes):
        if len(new_amplitudes) != self.bar_count:
            return
        self.mutex.lock()
        self.amplitudes = new_amplitudes.copy()
        self.mutex.unlock()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)

        self.mutex.lock()
        amplitudes = self.amplitudes
        self.mutex.unlock()

        bar_width = self.width() / self.bar_count
        for i, amp in enumerate(amplitudes):
            height = np.clip(amp * 2, 0, 1) * self.height()  # 调整幅度缩放
            gradient = QColor(
                int(255 * amp),  # 红色分量随振幅变化
                int(255 * (1 - amp)),  # 绿色分量反向变化
                100
            )
            painter.fillRect(
                i * bar_width + 1,  # +1 留出间隙
                self.height() - height,
                bar_width - 2,  # -2 留出间隙
                height,
                gradient
            )


class AudioThread(QThread):
    amplitude_updated = Signal(list)
    finished = Signal()

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.running = False
        self.p = None
        self.stream = None

    def run(self):
        self.running = True
        try:
            wf = wave.open(self.file_path, 'rb')
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(
                format=self.p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=self.callback,
                start=False
            )
            self.stream.start_stream()
            while self.stream.is_active() and self.running:
                pass
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.stop()
            self.finished.emit()

    def callback(self, in_data, frame_count, time_info, status):
        data = wave.open(self.file_path, 'rb').readframes(frame_count)
        if len(data) == 0:
            return (None, pyaudio.paComplete)

        # 转换为numpy数组并计算振幅
        samples = np.frombuffer(data, dtype=np.int16)
        if len(samples) == 0:
            return (data, pyaudio.paContinue)

        # 简单振幅计算（实际应使用FFT进行频域分析）
        amplitude = np.mean(np.abs(samples)) / 32768.0
        amplitudes = [amplitude * (1 + np.sin(i / 5)) for i in range(50)]  # 模拟动态效果

        self.amplitude_updated.emit(amplitudes)
        return (data, pyaudio.paContinue)

    def stop(self):
        self.running = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if self.p:
            self.p.terminate()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("音乐播放器 - 音频可视化")
        self.setGeometry(100, 100, 800, 400)

        # 可视化组件
        self.visualizer = AudioVisualizer()

        # 控制按钮
        self.btn_open = QPushButton("打开文件", self)
        self.btn_play = QPushButton("播放", self)
        self.btn_stop = QPushButton("停止", self)
        self.btn_open.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.toggle_play)
        self.btn_stop.clicked.connect(self.stop)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.visualizer)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_play)
        layout.addWidget(self.btn_stop)
        self.setLayout(layout)

        # 音频线程
        self.audio_thread = None
        self.current_file = None

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择音频文件", "", "Wave Files (*.wav);;All Files (*)"
        )
        if file_path:
            self.current_file = file_path
            self.btn_play.setEnabled(True)

    def toggle_play(self):
        if self.audio_thread and self.audio_thread.isRunning():
            self.stop()
        else:
            if self.current_file:
                self.audio_thread = AudioThread(self.current_file)
                self.audio_thread.amplitude_updated.connect(self.visualizer.update_amplitudes)
                self.audio_thread.finished.connect(lambda: self.btn_play.setText("播放"))
                self.audio_thread.start()
                self.btn_play.setText("暂停")

    def stop(self):
        if self.audio_thread:
            self.audio_thread.stop()
            self.btn_play.setText("播放")

    def closeEvent(self, event):
        self.stop()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import os

os.environ["PYTHONPY_SSIZE_T_CLEAN"] = "1"  # 解决系统兼容性问题

import sys
import numpy as np
import pyaudio
from pydub import AudioSegment
from PySide6.QtCore import Qt, QThread, Signal, QMutex
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import (QApplication, QWidget,
                               QVBoxLayout, QPushButton,
                               QFileDialog, QMessageBox)


class AudioVisualizer(QWidget):
    def __init__(self, bar_count=50):
        super().__init__()
        self.bar_count = bar_count
        self.amplitudes = [0.0] * bar_count
        self.setMinimumSize(800, 300)
        self.mutex = QMutex()

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
            # 动态颜色和高度计算
            clipped_amp = max(0.0, min(amp * 1.5, 1.0))
            height = clipped_amp * self.height()

            color = QColor(
                int(200 * clipped_amp),  # 红
                int(200 * (1 - clipped_amp)),  # 绿
                150  # 蓝
            )
            painter.fillRect(
                i * bar_width + 1,
                self.height() - height,
                bar_width - 2,
                height,
                color
            )


class AudioThread(QThread):
    amplitude_updated = Signal(list)
    finished = Signal()
    error_occurred = Signal(str)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.running = False
        self.p = None
        self.stream = None
        self.audio_data = None
        self.frame_pos = 0
        self.CHUNK = 1024 * 2  # 优化音频块大小

    def run(self):
        self.running = True
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"文件不存在: {self.file_path}")

            # 加载并预处理音频
            audio = AudioSegment.from_file(self.file_path)
            audio = audio.set_channels(1).set_frame_rate(44100)  # 标准化参数
            self.audio_data = np.array(
                audio.get_array_of_samples(),
                dtype=np.int16
            )

            # 初始化PyAudio
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                output=True,
                stream_callback=self.callback,
                start=False
            )
            self.stream.start_stream()

            # 保持线程运行
            while self.stream.is_active() and self.running:
                QThread.msleep(10)

        except Exception as e:
            self.error_occurred.emit(str(e))
        finally:
            self.stop()
            self.finished.emit()

    def callback(self, in_data, frame_count, time_info, status):
        try:
            remaining = len(self.audio_data) - self.frame_pos
            if remaining <= 0:
                return (None, pyaudio.paComplete)

            # 读取当前块数据
            frames_to_read = min(frame_count, remaining)
            chunk = self.audio_data[self.frame_pos:self.frame_pos + frames_to_read]
            self.frame_pos += frames_to_read

            # 计算振幅
            if len(chunk) > 0:
                amplitude = np.abs(chunk).mean() / 32768.0
                amplitudes = [amplitude * (1 + 0.5 * np.sin(i / 5)) for i in range(50)]
                self.amplitude_updated.emit(amplitudes)
            else:
                amplitudes = [0.0] * 50
                self.amplitude_updated.emit(amplitudes)

            return (chunk.tobytes(), pyaudio.paContinue)

        except Exception as e:
            self.error_occurred.emit(f"音频处理错误: {str(e)}")
            return (None, pyaudio.paAbort)

    def stop(self):
        self.running = False
        if self.stream:
            try:
                self.stream.stop_stream()
                self.stream.close()
            except:
                pass
        if self.p:
            try:
                self.p.terminate()
            except:
                pass


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MP3音乐播放器")
        self.setGeometry(100, 100, 800, 450)

        # 初始化界面
        self.visualizer = AudioVisualizer()

        self.btn_open = QPushButton("打开文件", self)
        self.btn_play = QPushButton("播放", self)
        self.btn_stop = QPushButton("停止", self)

        # 按钮样式
        button_style = """
        QPushButton {
            min-width: 80px;
            padding: 8px;
            font-size: 14px;
            border: 1px solid #444;
            border-radius: 4px;
        }
        """
        self.setStyleSheet(button_style)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.visualizer)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_play)
        layout.addWidget(self.btn_stop)
        self.setLayout(layout)

        # 初始化状态
        self.audio_thread = None
        self.current_file = None
        self.btn_play.setEnabled(False)
        self.btn_stop.setEnabled(False)

        # 连接信号
        self.btn_open.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.toggle_play)
        self.btn_stop.clicked.connect(self.stop)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择音频文件",
            "",
            "音频文件 (*.mp3 *.wav);;所有文件 (*.*)"
        )
        if file_path:
            self.current_file = file_path
            self.btn_play.setEnabled(True)
            self.btn_stop.setEnabled(False)
            self.setWindowTitle(f"MP3音乐播放器 - {os.path.basename(file_path)}")

    def toggle_play(self):
        if self.audio_thread and self.audio_thread.isRunning():
            self.stop()
        else:
            if self.current_file:
                self.audio_thread = AudioThread(self.current_file)
                self.audio_thread.amplitude_updated.connect(self.visualizer.update_amplitudes)
                self.audio_thread.finished.connect(self.on_playback_finished)
                self.audio_thread.error_occurred.connect(self.show_error)
                self.audio_thread.start()
                self.btn_play.setText("暂停")
                self.btn_stop.setEnabled(True)

    def stop(self):
        if self.audio_thread:
            self.audio_thread.stop()
        self.btn_play.setText("播放")
        self.btn_stop.setEnabled(False)

    def on_playback_finished(self):
        self.btn_play.setText("播放")
        self.btn_stop.setEnabled(False)

    def show_error(self, message):
        QMessageBox.critical(self, "错误", message)
        self.stop()

    def closeEvent(self, event):
        self.stop()
        super().closeEvent(event)


if __name__ == "__main__":
    # 检查必要组件
    try:
        import numpy as np
        import pyaudio
        from pydub import AudioSegment
    except ImportError as e:
        print(f"缺少依赖库: {str(e)}")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
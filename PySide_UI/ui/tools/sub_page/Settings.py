import sys

from PySide6.QtCore import Qt, QObject, QSettings, Signal, Slot, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget, QDialog, QApplication, QFileDialog

from PySide_UI.ui.tools.sub_ui.settings import Ui_settings


class SettingsPage(QDialog, Ui_settings):
    settings_save = Signal(dict)

    def __init__(self, data: dict = {}):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('设置')
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 设置标题以及信息
        self.setModal(True)
        self.show()

        self.data = data
        self.save_path_lab.setText(self.data['save_path'])
        self.cookies_textEdit.setText(self.data['cookies'])

    @Slot()
    def on_path_btn_clicked(self):
        # 设置保存路径按钮按压信号
        # 原保存路径
        path = self.save_path_lab.text()
        # 现保存路径
        save_path = QFileDialog.getExistingDirectory(self, '选择下载路径', f'{path}')

        if save_path is not None and save_path != '':
            self.save_path_lab.setText(save_path)
        print(save_path)

        self.data['save_path'] = save_path
        return

    @Slot()
    def on_github_btn_clicked(self):
        # 打开github网站
        url = QUrl(self.github_lab.text()[7:])
        print(url)
        QDesktopServices.openUrl(url)
        return



    @Slot()
    def on_save_btn_clicked(self):
        # 保存按钮被点击，
        # 加载cookies
        self.data['cookies'] = self.cookies_textEdit.toPlainText()
        self.settings_save.emit(self.data)
        pass

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(800, 600)
        self.window2 = SettingsPage({})
        self.window2.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()

    window.show()
    sys.exit(app.exec())

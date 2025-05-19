import sys
from pprint import pprint

from PySide6.QtCore import Qt, QObject, Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout

from PySide_UI.ui.tools.sub_ui.one_playlist import Ui_playlist
from PySide_UI.ui.tools.sub_ui.recommend_playlist import Ui_recommend_playlist


class OnePlayList(QWidget, Ui_playlist):
    # 单个歌单
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置顶层窗口qwidget样式生效
        self.setAttribute(Qt.WA_StyledBackground)
        self.setupUi(self)


class RecommendPlaylistPage(QWidget, Ui_recommend_playlist):
    # 设置每日推荐歌单
    add_playlists = Signal()
    load_playlist_page = Signal(dict)
    error = Signal(str)
    enable_ui = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground)
        # self.show()
        # # 插入指定数量的歌单子项
        # self.insert_plalist(self.recommend_playlist_gridLayout, 20, 0, 'playlist')

        # 设置滚动到底部的事件
        self.set_scrollbar_singl()
        # 已加载的歌单下标
        self.index = 0
        # 插入行列
        self.row = 0
        self.col = 0

    def add_recommend_playlist(self, playlist_info: dict):
        # 获取歌单信息后，插入指定数量的歌单子项并设置内容

        try:
            # 设置页面
            # 插入歌单内容
            for key in playlist_info['playlist']:
                # 将所有页数的歌单加载
                # 当前页数的歌单数据
                recommend_playlist = playlist_info['playlist'][key]
                playlist_count = len(recommend_playlist.keys())
                # 插入指定数量的歌单子项
                self.insert_plalist(self.recommend_playlist_gridLayout, playlist_count, self.index, 'playlist')

                # 设置歌单内容
                for key in recommend_playlist.keys():
                    playlist_id = recommend_playlist[key]['id']
                    # 查找指定歌单widget
                    widget = self.recommend_playlist_scroll_area.findChild(QWidget, f'playlist_{self.index}')

                    # 设置歌单图片及id
                    img_path = recommend_playlist[key]['img_path']
                    widget.list_img_btn.setStyleSheet(f'border-image: url({img_path});')
                    widget.list_img_btn.setProperty('list_id', str(playlist_id))
                    # 设置歌单名称及id
                    name = recommend_playlist[key]['name']
                    widget.list_name_lab.setText(name)
                    widget.list_name_lab.setProperty('list_id', str(playlist_id))

                    # # 左击事件
                    # widget.list_img_btn.leftclick.connect(lambda val: print(val))
                    # widget.list_name_lab.leftclick.connect(lambda val: print(val))
                    # 左击事件
                    widget.list_img_btn.leftclick.connect(lambda val: self.load_playlist_page.emit(val))
                    widget.list_name_lab.leftclick.connect(lambda val: self.load_playlist_page.emit(val))

                    self.index += 1
        except Exception as e:
            self.error.emit(str(e))
        finally:
            # 恢复ui
            self.enable_ui.emit()
        return

    def remove_recommend_playlist(self):
        # 移除推荐歌单内容
        self.remove_playlist(self.recommend_playlist_scroll_area, 'playlist')

    def insert_plalist(self, layout: QGridLayout, count: int = 10, index: int = 10, obj_name: str = 'playlist'):
        '''
        将指定数量的单个歌单插入到格子布局中
        :param layout: 要插入的布局
        :param count: 歌单数量
        :param obj_name: 歌单对象名称，用于区分不同的歌单
        :param index: 起始下标
        :return:
        '''
        for i in range(count):
            # 计算当前插入的行和列
            row = (self.index + i) // 5 + 1
            col = (self.index + i) % 5
            widget = OnePlayList()
            now_index = index + i
            widget.setObjectName(f'{obj_name}_{now_index}')
            layout.addWidget(widget, row, col)
        return

    def remove_playlist(self, obj: QObject, obj_name='playlist'):
        '''
        移除格子布局中所有的歌单子项
        '''
        # 查找该控件下所有的qwidget
        wiget_list = obj.findChildren(QWidget)
        for item in wiget_list:
            if obj_name in item.objectName():
                item.setParent(None)
                item.deleteLater()
        self.index = 0
        return

    def set_scrollbar_singl(self):
        # 滚动条滚动到底部事件
        scrollbar = self.recommend_playlist_scroll_area.verticalScrollBar()

        def scroll_down():
            if scrollbar.value() == scrollbar.maximum() and scrollbar.value() != 0:
                print('滑动到底部')
                self.add_playlists.emit()

        scrollbar.valueChanged.connect(scroll_down)
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecommendPlaylistPage()
    window.show()
    sys.exit(app.exec())
